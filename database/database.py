import sqlite3
import hashlib
from datetime import datetime

DB_NAME = "restaurant_gomong.db"


def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def create_tables():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS pegawai (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nama TEXT NOT NULL,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            jabatan TEXT DEFAULT 'Staf'
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS meja (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nomor_meja TEXT NOT NULL UNIQUE,
            kapasitas INTEGER NOT NULL,
            lantai INTEGER NOT NULL DEFAULT 1,
            jenis TEXT NOT NULL,
            status TEXT DEFAULT 'Tersedia'
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS reservasi (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nama_tamu TEXT NOT NULL,
            no_telepon TEXT NOT NULL,
            jumlah_tamu INTEGER NOT NULL,
            tanggal TEXT NOT NULL,
            waktu TEXT NOT NULL,
            meja_id INTEGER,
            lantai INTEGER NOT NULL DEFAULT 1,
            status TEXT DEFAULT 'Menunggu',
            catatan TEXT,
            created_at TEXT NOT NULL,
            id_pegawai INTEGER,
            FOREIGN KEY (meja_id) REFERENCES meja(id),
            FOREIGN KEY (id_pegawai) REFERENCES pegawai(id)
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transaksi (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            reservasi_id INTEGER NOT NULL UNIQUE,
            total_dp REAL DEFAULT 0,
            status_bayar TEXT DEFAULT 'Belum Bayar',
            metode_bayar TEXT,
            catatan TEXT,
            waktu TEXT NOT NULL,
            FOREIGN KEY (reservasi_id) REFERENCES reservasi(id)
        )
    """)

    conn.commit()
    conn.close()


def init_pegawai():
    conn = get_db_connection()
    cursor = conn.cursor()
    if cursor.execute("SELECT COUNT(*) FROM pegawai").fetchone()[0] == 0:
        def hp(p): return hashlib.sha256(p.encode()).hexdigest()
        data = [
            ('Admin Gomong', 'admin', hp('admin123'), 'Manajer'),
            ('dest', 'dest', hp('dest123'), 'Staf'),
        ]
        cursor.executemany(
            "INSERT INTO pegawai (nama, username, password, jabatan) VALUES (?,?,?,?)", data
        )
        conn.commit()
    conn.close()


def init_meja():
    conn = get_db_connection()
    cursor = conn.cursor()
    if cursor.execute("SELECT COUNT(*) FROM meja").fetchone()[0] == 0:
        # Semua meja di lantai 1 — total 24 meja
        meja_data = [
            # Meja 2 orang (8 meja)
            ('M01', 2, 1, 'Kecil'),
            ('M02', 2, 1, 'Kecil'),
            ('M03', 2, 1, 'Kecil'),
            ('M04', 2, 1, 'Kecil'),
            ('M05', 2, 1, 'Kecil'),
            ('M06', 2, 1, 'Kecil'),
            ('M07', 2, 1, 'Kecil'),
            ('M08', 2, 1, 'Kecil'),
            # Meja 4 orang (8 meja)
            ('M09', 4, 1, 'Kecil'),
            ('M10', 4, 1, 'Kecil'),
            ('M11', 4, 1, 'Kecil'),
            ('M12', 4, 1, 'Kecil'),
            ('M13', 4, 1, 'Kecil'),
            ('M14', 4, 1, 'Kecil'),
            ('M15', 4, 1, 'Kecil'),
            ('M16', 4, 1, 'Kecil'),
            # Meja 6 orang (4 meja)
            ('M17', 6, 1, 'Besar'),
            ('M18', 6, 1, 'Besar'),
            ('M19', 6, 1, 'Besar'),
            ('M20', 6, 1, 'Besar'),
            # Meja 8 orang (4 meja)
            ('M21', 8, 1, 'Besar'),
            ('M22', 8, 1, 'Besar'),
            ('M23', 8, 1, 'Besar'),
            ('M24', 8, 1, 'Besar'),
        ]
        cursor.executemany(
            "INSERT INTO meja (nomor_meja, kapasitas, lantai, jenis, status) VALUES (?,?,?,?,?)",
            [(m[0], m[1], m[2], m[3], 'Tersedia') for m in meja_data]
        )
        conn.commit()
    conn.close()


# ── MEJA STATUS AUTO-SYNC ────────────────────────────────────────────────────

STATUS_AKTIF = ('Menunggu', 'Dikonfirmasi', 'Duduk')

def _active_status_placeholders():
    return ','.join('?' * len(STATUS_AKTIF))


def _get_konflik_reservasi(conn, meja_id, tanggal, waktu, exclude_reservasi_id=None):
    if not meja_id:
        return None

    exclude_clause = "AND r.id != ?" if exclude_reservasi_id else ""
    params = [meja_id, tanggal, waktu, *STATUS_AKTIF]
    if exclude_reservasi_id:
        params.append(exclude_reservasi_id)

    return conn.execute(f"""
        SELECT r.id, r.nama_tamu, r.tanggal, r.waktu, r.status, m.nomor_meja
        FROM reservasi r
        LEFT JOIN meja m ON r.meja_id = m.id
        WHERE r.meja_id = ?
          AND r.tanggal = ?
          AND r.waktu = ?
          AND r.status IN ({_active_status_placeholders()})
          {exclude_clause}
        ORDER BY r.id ASC
        LIMIT 1
    """, params).fetchone()


def _pesan_konflik_reservasi(konflik):
    return (
        f"Meja {konflik['nomor_meja']} sudah dipesan oleh {konflik['nama_tamu']} "
        f"pada {konflik['tanggal']} jam {konflik['waktu']} "
        f"dengan status {konflik['status']}. "
        "Meja baru bisa diberikan lagi setelah reservasi sebelumnya selesai atau dibatalkan."
    )


def sync_status_meja(conn, meja_id):
    """
    Periksa apakah meja masih punya reservasi aktif.
    Jika ya → Terisi. Jika tidak → Tersedia (kecuali Maintenance).
    Panggil ini setiap kali reservasi ditambah, diedit, atau dihapus.
    """
    if not meja_id:
        return
    # Jangan ubah jika sedang Maintenance
    current = conn.execute(
        "SELECT status FROM meja WHERE id = ?", (meja_id,)
    ).fetchone()
    if not current or current['status'] == 'Maintenance':
        return

    ada_aktif = conn.execute(
        f"SELECT COUNT(*) FROM reservasi WHERE meja_id = ? AND status IN ({_active_status_placeholders()})",
        (meja_id, *STATUS_AKTIF)
    ).fetchone()[0]

    new_status = 'Terisi' if ada_aktif > 0 else 'Tersedia'
    conn.execute("UPDATE meja SET status = ? WHERE id = ?", (new_status, meja_id))


# ── PEGAWAI ──────────────────────────────────────────────────────────────────

def get_all_pegawai():
    conn = get_db_connection()
    rows = conn.execute(
        "SELECT id, nama, username, jabatan FROM pegawai ORDER BY jabatan, nama"
    ).fetchall()
    conn.close()
    return rows


def get_pegawai_by_id(pegawai_id):
    conn = get_db_connection()
    row = conn.execute(
        "SELECT id, nama, username, jabatan FROM pegawai WHERE id = ?",
        (pegawai_id,)
    ).fetchone()
    conn.close()
    return row


def tambah_pegawai(nama, username, password_plain, jabatan):
    hashed = hashlib.sha256(password_plain.encode()).hexdigest()
    conn = get_db_connection()
    try:
        conn.execute(
            "INSERT INTO pegawai (nama, username, password, jabatan) VALUES (?,?,?,?)",
            (nama, username, hashed, jabatan)
        )
        conn.commit()
        return True, None
    except Exception as e:
        return False, str(e)
    finally:
        conn.close()


def edit_pegawai(pegawai_id, nama, username, jabatan, password_plain=None):
    conn = get_db_connection()
    try:
        if password_plain:
            hashed = hashlib.sha256(password_plain.encode()).hexdigest()
            conn.execute(
                "UPDATE pegawai SET nama=?, username=?, jabatan=?, password=? WHERE id=?",
                (nama, username, jabatan, hashed, pegawai_id)
            )
        else:
            conn.execute(
                "UPDATE pegawai SET nama=?, username=?, jabatan=? WHERE id=?",
                (nama, username, jabatan, pegawai_id)
            )
        conn.commit()
        return True, None
    except Exception as e:
        return False, str(e)
    finally:
        conn.close()


def hapus_pegawai(pegawai_id):
    conn = get_db_connection()
    try:
        conn.execute("DELETE FROM pegawai WHERE id = ?", (pegawai_id,))
        conn.commit()
        return True, None
    except Exception as e:
        return False, str(e)
    finally:
        conn.close()


def hapus_banyak_pegawai(id_list):
    conn = get_db_connection()
    try:
        placeholders = ','.join('?' for _ in id_list)
        conn.execute(f"DELETE FROM pegawai WHERE id IN ({placeholders})", id_list)
        conn.commit()
        return True, None
    except Exception as e:
        return False, str(e)
    finally:
        conn.close()


def get_jabatan_by_username(username):
    conn = get_db_connection()
    row = conn.execute(
        "SELECT jabatan FROM pegawai WHERE username = ?", (username,)
    ).fetchone()
    conn.close()
    return row['jabatan'] if row else 'Staf'


# ── RESERVASI ────────────────────────────────────────────────────────────────

def get_available_tables(jumlah_tamu, tanggal, waktu, exclude_reservasi_id=None):
    """Cari meja tersedia sesuai jumlah tamu & waktu reservasi."""
    conn = get_db_connection()

    exclude_clause = "AND r.id != ?" if exclude_reservasi_id else ""
    params = [jumlah_tamu, tanggal, waktu, *STATUS_AKTIF]
    if exclude_reservasi_id:
        params.append(exclude_reservasi_id)

    query = f"""
        SELECT m.* FROM meja m
        WHERE m.kapasitas >= ?
          AND m.status != 'Maintenance'
          AND m.id NOT IN (
              SELECT r.meja_id FROM reservasi r
              WHERE r.tanggal = ? AND r.waktu = ?
                AND r.status IN ({_active_status_placeholders()})
                AND r.meja_id IS NOT NULL
                {exclude_clause}
          )
        ORDER BY m.kapasitas ASC
    """
    tables = conn.execute(query, params).fetchall()
    conn.close()
    return tables


def simpan_reservasi(nama, telepon, jumlah, tanggal, waktu, meja_id, status, catatan,
                     reservasi_id=None):
    """
    Tambah atau edit reservasi, lalu sync status meja secara otomatis.
    Returns (True, None) atau (False, pesan_error).
    """
    conn = get_db_connection()
    try:
        if meja_id and status in STATUS_AKTIF:
            konflik = _get_konflik_reservasi(
                conn, meja_id, tanggal, waktu, reservasi_id
            )
            if konflik:
                return False, _pesan_konflik_reservasi(konflik)

        if reservasi_id:
            # Ambil meja_id lama sebelum diupdate
            lama = conn.execute(
                "SELECT meja_id FROM reservasi WHERE id = ?", (reservasi_id,)
            ).fetchone()
            old_meja_id = lama['meja_id'] if lama else None

            conn.execute("""
                UPDATE reservasi
                SET nama_tamu=?, no_telepon=?, jumlah_tamu=?, tanggal=?, waktu=?,
                    meja_id=?, lantai=1, status=?, catatan=?
                WHERE id=?
            """, (nama, telepon, jumlah, tanggal, waktu, meja_id, status, catatan, reservasi_id))

            # Sync meja lama (jika meja berganti, meja lama perlu di-cek ulang)
            if old_meja_id and old_meja_id != meja_id:
                sync_status_meja(conn, old_meja_id)
        else:
            conn.execute("""
                INSERT INTO reservasi
                    (nama_tamu, no_telepon, jumlah_tamu, tanggal, waktu,
                     meja_id, lantai, status, catatan, created_at)
                VALUES (?,?,?,?,?,?,1,?,?,?)
            """, (nama, telepon, jumlah, tanggal, waktu, meja_id, status, catatan,
                  datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        # Sync meja baru/saat-ini
        sync_status_meja(conn, meja_id)
        conn.commit()
        return True, None
    except Exception as e:
        return False, str(e)
    finally:
        conn.close()


def hapus_banyak_reservasi(id_list):
    conn = get_db_connection()
    try:
        # Kumpulkan meja_id yang terdampak sebelum dihapus
        placeholders = ','.join('?' for _ in id_list)
        meja_ids = [
            row['meja_id'] for row in conn.execute(
                f"SELECT meja_id FROM reservasi WHERE id IN ({placeholders})", id_list
            ).fetchall() if row['meja_id']
        ]

        conn.execute(f"DELETE FROM reservasi WHERE id IN ({placeholders})", id_list)

        # Sync semua meja yang terdampak
        for mid in set(meja_ids):
            sync_status_meja(conn, mid)

        conn.commit()
        return True, None
    except Exception as e:
        return False, str(e)
    finally:
        conn.close()


def update_status_reservasi(reservasi_id, new_status):
    """Update status reservasi dan sync meja otomatis."""
    conn = get_db_connection()
    try:
        row = conn.execute(
            "SELECT meja_id, tanggal, waktu FROM reservasi WHERE id = ?", (reservasi_id,)
        ).fetchone()
        meja_id = row['meja_id'] if row else None

        if row and meja_id and new_status in STATUS_AKTIF:
            konflik = _get_konflik_reservasi(
                conn, meja_id, row['tanggal'], row['waktu'], reservasi_id
            )
            if konflik:
                return False, _pesan_konflik_reservasi(konflik)

        conn.execute(
            "UPDATE reservasi SET status = ? WHERE id = ?", (new_status, reservasi_id)
        )
        sync_status_meja(conn, meja_id)
        conn.commit()
        return True, None
    except Exception as e:
        return False, str(e)
    finally:
        conn.close()


def get_all_meja():
    conn = get_db_connection()
    rows = conn.execute(
        "SELECT id, nomor_meja, kapasitas, lantai, jenis, status FROM meja ORDER BY kapasitas, nomor_meja"
    ).fetchall()
    conn.close()
    return rows


def get_meja_by_id(meja_id):
    conn = get_db_connection()
    row = conn.execute(
        "SELECT id, nomor_meja, kapasitas, lantai, jenis, status FROM meja WHERE id = ?",
        (meja_id,)
    ).fetchone()
    conn.close()
    return row


def tambah_meja(nomor_meja, kapasitas, lantai, jenis, status):
    conn = get_db_connection()
    try:
        conn.execute(
            "INSERT INTO meja (nomor_meja, kapasitas, lantai, jenis, status) VALUES (?,?,?,?,?)",
            (nomor_meja, kapasitas, lantai, jenis, status)
        )
        conn.commit()
        return True, None
    except Exception as e:
        return False, str(e)
    finally:
        conn.close()


def edit_meja(meja_id, nomor_meja, kapasitas, lantai, jenis, status):
    conn = get_db_connection()
    try:
        conn.execute(
            "UPDATE meja SET nomor_meja=?, kapasitas=?, lantai=?, jenis=?, status=? WHERE id=?",
            (nomor_meja, kapasitas, lantai, jenis, status, meja_id)
        )
        if status == 'Tersedia':
            sync_status_meja(conn, meja_id)
        conn.commit()
        return True, None
    except Exception as e:
        return False, str(e)
    finally:
        conn.close()


def hapus_meja(meja_id):
    conn = get_db_connection()
    try:
        dipakai = conn.execute(
            "SELECT COUNT(*) FROM reservasi WHERE meja_id = ?", (meja_id,)
        ).fetchone()[0]
        if dipakai:
            return False, "Meja masih terhubung dengan data reservasi."
        conn.execute("DELETE FROM meja WHERE id = ?", (meja_id,))
        conn.commit()
        return True, None
    except Exception as e:
        return False, str(e)
    finally:
        conn.close()


def init_database():
    create_tables()
    init_pegawai()
    init_meja()
