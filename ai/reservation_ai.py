from datetime import datetime


STATUS_AKTIF_DEFAULT = ("Menunggu", "Dikonfirmasi")


def _placeholders(total):
    return ",".join("?" * total)


def rekomendasi_meja(conn, jumlah_tamu, tanggal, waktu, exclude_reservasi_id=None,
                     status_aktif=STATUS_AKTIF_DEFAULT):
    """Ranking meja tersedia berdasarkan kapasitas, konflik jadwal, dan riwayat."""
    exclude_clause = "AND r.id != ?" if exclude_reservasi_id else ""
    params = [jumlah_tamu, tanggal, waktu, *status_aktif]
    if exclude_reservasi_id:
        params.append(exclude_reservasi_id)

    query = f"""
        SELECT
            m.id, m.nomor_meja, m.kapasitas, m.lantai, m.jenis, m.status,
            COUNT(hist.id) AS jumlah_pemakaian,
            (m.kapasitas - ?) AS sisa_kursi
        FROM meja m
        LEFT JOIN reservasi hist
          ON hist.meja_id = m.id
         AND hist.status != 'Dibatalkan'
        WHERE m.kapasitas >= ?
          AND m.status NOT IN ('Maintenance', 'Dibereskan')
          AND m.id NOT IN (
              SELECT r.meja_id FROM reservasi r
              WHERE r.tanggal = ? AND r.waktu = ?
                AND r.status IN ({_placeholders(len(status_aktif))})
                AND r.meja_id IS NOT NULL
                {exclude_clause}
          )
        GROUP BY m.id
        ORDER BY sisa_kursi ASC, jumlah_pemakaian ASC, m.nomor_meja ASC
    """

    return [dict(row) for row in conn.execute(query, [jumlah_tamu, *params]).fetchall()]


def prediksi_jam_ramai(conn, tanggal=None):
    """Prediksi jam paling ramai dari rata-rata reservasi pada hari yang sama."""
    target = tanggal or datetime.now().strftime("%Y-%m-%d")
    try:
        target_dt = datetime.strptime(target, "%Y-%m-%d")
    except ValueError:
        target_dt = datetime.now()
        target = target_dt.strftime("%Y-%m-%d")

    sqlite_weekday = str((target_dt.weekday() + 1) % 7)

    row = conn.execute("""
        SELECT waktu, ROUND(AVG(total_tamu), 1) AS estimasi_tamu, COUNT(*) AS jumlah_data
        FROM (
            SELECT tanggal, waktu, SUM(jumlah_tamu) AS total_tamu
            FROM reservasi
            WHERE status != 'Dibatalkan'
              AND strftime('%w', tanggal) = ?
            GROUP BY tanggal, waktu
        )
        GROUP BY waktu
        ORDER BY estimasi_tamu DESC, waktu ASC
        LIMIT 1
    """, (sqlite_weekday,)).fetchone()

    sumber = "Berdasarkan rata-rata reservasi pada hari yang sama."
    if not row:
        row = conn.execute("""
            SELECT waktu, ROUND(AVG(total_tamu), 1) AS estimasi_tamu, COUNT(*) AS jumlah_data
            FROM (
                SELECT tanggal, waktu, SUM(jumlah_tamu) AS total_tamu
                FROM reservasi
                WHERE status != 'Dibatalkan'
                GROUP BY tanggal, waktu
            )
            GROUP BY waktu
            ORDER BY estimasi_tamu DESC, waktu ASC
            LIMIT 1
        """).fetchone()
        sumber = "Berdasarkan seluruh data reservasi yang tersedia."

    if not row:
        return {
            "tanggal": target,
            "waktu": None,
            "estimasi_tamu": 0,
            "jumlah_data": 0,
            "saran_staf": "Data belum cukup",
            "keterangan": "Belum ada data reservasi untuk membuat prediksi.",
        }

    estimasi = row["estimasi_tamu"] or 0
    estimasi_fmt = int(estimasi) if float(estimasi).is_integer() else estimasi

    if estimasi >= 24:
        saran_staf = "Tambah 3 staf"
    elif estimasi >= 16:
        saran_staf = "Tambah 2 staf"
    elif estimasi >= 8:
        saran_staf = "Tambah 1 staf"
    else:
        saran_staf = "Staf normal"

    return {
        "tanggal": target,
        "waktu": row["waktu"],
        "estimasi_tamu": estimasi_fmt,
        "jumlah_data": row["jumlah_data"],
        "saran_staf": saran_staf,
        "keterangan": sumber,
    }
