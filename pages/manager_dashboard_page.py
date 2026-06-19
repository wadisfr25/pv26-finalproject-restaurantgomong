from PySide6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel,
                               QTableWidget, QTableWidgetItem, QHeaderView,
                               QFrame, QGroupBox)
from PySide6.QtCore import Qt
from datetime import datetime
import database.database as database
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class StatCard(QFrame):
    def __init__(self, title, value, emoji="📌", color="#3498DB"):
        super().__init__()

        self.setObjectName("dashCard")
        self.setFixedHeight(80)  # tinggi card

        self.setStyleSheet(f"""
            QFrame#dashCard {{
                background: white;
                border: 1px solid #DDE4EC;
                border-left: 4px solid {color};
                border-radius: 10px;
            }}

            QLabel#cardValue {{
                background: transparent;
                border: none;
                color: #1E293B;
                font-size: 20px;
                font-weight: 700;
            }}

            QLabel#cardTitle {{
                background: transparent;
                border: none;
                color: #64748B;
                font-size: 10px;
            }}
        """)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(8, 4, 8, 4)
        layout.setSpacing(2)

        self.value_lbl = QLabel(str(value))
        self.value_lbl.setObjectName("cardValue")
        self.value_lbl.setAlignment(Qt.AlignCenter)

        title_lbl = QLabel(f"{emoji} {title}")
        title_lbl.setObjectName("cardTitle")
        title_lbl.setAlignment(Qt.AlignCenter)

        layout.addWidget(self.value_lbl)
        layout.addWidget(title_lbl)

    def update_value(self, val):
        self.value_lbl.setText(str(val))


class ManagerDashboardPage(QWidget):
    def __init__(self, nama_pegawai):
        super().__init__()
        self.nama_pegawai = nama_pegawai
        self.init_ui()
        self.refresh()

    def init_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(28, 24, 28, 24)
        layout.setSpacing(18)

        header = QLabel(f"Selamat Datang, {self.nama_pegawai}! 👋")
        header.setObjectName("pageHeader")
        layout.addWidget(header)

        date_lbl = QLabel(f"📅  {datetime.now().strftime('%A, %d %B %Y')}  ·  Dashboard Manajer")
        date_lbl.setObjectName("dateLabel")
        layout.addWidget(date_lbl)

        # ── Row 1: Statistik Reservasi ───────────────────────────────
        res_grp = QGroupBox("📋  Statistik Reservasi")
        res_row = QHBoxLayout(res_grp)
        res_row.setSpacing(12)
        self.card_total      = StatCard("Total Reservasi",         "0", "📋", "#3498DB")
        self.card_hari_ini   = StatCard("Reservasi Hari Ini",      "0", "📅", "#27AE60")
        self.card_menunggu   = StatCard("Menunggu Konfirmasi",      "0", "⏳", "#F39C12")
        self.card_dibatalkan = StatCard("Dibatalkan (Bulan Ini)",   "0", "❌", "#E74C3C")
        for c in [self.card_total, self.card_hari_ini,
                  self.card_menunggu, self.card_dibatalkan]:
            res_row.addWidget(c)
        layout.addWidget(res_grp)

        # ── Row 2: Statistik Meja & Pegawai ──────────────────────────
        info_row = QHBoxLayout()
        info_row.setSpacing(16)

        meja_grp = QGroupBox("🪑  Statistik Meja")
        meja_row = QHBoxLayout(meja_grp)
        meja_row.setSpacing(12)
        self.card_meja_tersedia   = StatCard("Meja Tersedia", "0", "✅", "#27AE60")
        self.card_meja_terisi     = StatCard("Meja Terisi",   "0", "🔴", "#E74C3C")
        self.card_meja_maintenance= StatCard("Maintenance",   "0", "🔧", "#F39C12")
        for c in [self.card_meja_tersedia, self.card_meja_terisi,
                  self.card_meja_maintenance]:
            meja_row.addWidget(c)

        pegawai_grp = QGroupBox("👥  Statistik Pegawai")
        peg_row = QHBoxLayout(pegawai_grp)
        peg_row.setSpacing(12)
        self.card_total_pegawai = StatCard("Total Pegawai", "0", "👤", "#9B59B6")
        self.card_manajer       = StatCard("Manajer",       "0", "🔑", "#E67E22")
        self.card_staf          = StatCard("Staf",          "0", "👔", "#16A085")
        for c in [self.card_total_pegawai, self.card_manajer, self.card_staf]:
            peg_row.addWidget(c)

        info_row.addWidget(meja_grp, 3)
        info_row.addWidget(pegawai_grp, 3)
        layout.addLayout(info_row)

        # ── Row 3: Tabel + chart ──────────────────────────────────────
        bottom = QHBoxLayout()
        bottom.setSpacing(16)

        tbl_grp = QGroupBox("📋  Reservasi Hari Ini")
        tbl_layout = QVBoxLayout(tbl_grp)
        self.today_table = QTableWidget()
        self.today_table.setColumnCount(5)
        self.today_table.setHorizontalHeaderLabels(
            ["Nama Tamu", "Telepon", "Tamu", "Waktu", "Status"]
        )
        self.today_table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.today_table.setSelectionBehavior(QTableWidget.SelectRows)
        self.today_table.verticalHeader().setVisible(False)
        hdr = self.today_table.horizontalHeader()
        hdr.setSectionResizeMode(0, QHeaderView.Stretch)
        for i in range(1, 5):
            hdr.setSectionResizeMode(i, QHeaderView.ResizeToContents)
        tbl_layout.addWidget(self.today_table)

        self.figure = Figure(figsize=(4, 3), dpi=90, facecolor='none')
        self.canvas = FigureCanvas(self.figure)
        self.canvas.setMinimumWidth(280)

        bottom.addWidget(tbl_grp, 3)
        bottom.addWidget(self.canvas, 2)
        layout.addLayout(bottom)

    def refresh(self):
        today = datetime.now().strftime("%Y-%m-%d")
        month_start = datetime.now().strftime("%Y-%m-01")
        conn = database.get_db_connection()

        total = conn.execute(
            "SELECT COUNT(*) FROM reservasi WHERE status != 'Dibatalkan'"
        ).fetchone()[0]
        hari_ini = conn.execute(
            "SELECT COUNT(*) FROM reservasi WHERE tanggal = ? AND status != 'Dibatalkan'",
            (today,)
        ).fetchone()[0]
        menunggu = conn.execute(
            "SELECT COUNT(*) FROM reservasi WHERE status = 'Menunggu'"
        ).fetchone()[0]
        dibatalkan = conn.execute(
            "SELECT COUNT(*) FROM reservasi WHERE status = 'Dibatalkan' AND tanggal >= ?",
            (month_start,)
        ).fetchone()[0]

        self.card_total.update_value(total)
        self.card_hari_ini.update_value(hari_ini)
        self.card_menunggu.update_value(menunggu)
        self.card_dibatalkan.update_value(dibatalkan)

        def meja_count(status):
            return conn.execute(
                "SELECT COUNT(*) FROM meja WHERE status = ?", (status,)
            ).fetchone()[0]

        self.card_meja_tersedia.update_value(meja_count('Tersedia'))
        self.card_meja_terisi.update_value(meja_count('Terisi'))
        self.card_meja_maintenance.update_value(meja_count('Maintenance'))

        total_peg   = conn.execute("SELECT COUNT(*) FROM pegawai").fetchone()[0]
        jml_manajer = conn.execute(
            "SELECT COUNT(*) FROM pegawai WHERE jabatan = 'Manajer'"
        ).fetchone()[0]
        jml_staf    = conn.execute(
            "SELECT COUNT(*) FROM pegawai WHERE jabatan = 'Staf'"
        ).fetchone()[0]

        self.card_total_pegawai.update_value(total_peg)
        self.card_manajer.update_value(jml_manajer)
        self.card_staf.update_value(jml_staf)

        rows = conn.execute("""
            SELECT r.nama_tamu, r.no_telepon, r.jumlah_tamu, r.waktu, r.status
            FROM reservasi r
            WHERE r.tanggal = ?
            ORDER BY r.waktu ASC
        """, (today,)).fetchall()

        status_data = conn.execute("""
            SELECT status, COUNT(*) as total FROM reservasi
            GROUP BY status
        """).fetchall()

        conn.close()

        self.today_table.setRowCount(0)
        for row, d in enumerate(rows):
            self.today_table.insertRow(row)
            self.today_table.setItem(row, 0, QTableWidgetItem(d['nama_tamu']))
            self.today_table.setItem(row, 1, QTableWidgetItem(d['no_telepon']))
            self.today_table.setItem(row, 2, QTableWidgetItem(str(d['jumlah_tamu'])))
            self.today_table.setItem(row, 3, QTableWidgetItem(d['waktu']))
            self.today_table.setItem(row, 4, QTableWidgetItem(d['status']))

        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.set_facecolor('#F8F9FA')
        if status_data:
            colors_map = {
                'Menunggu': '#F39C12', 'Dikonfirmasi': '#3498DB',
                'Duduk': '#27AE60', 'Selesai': '#95A5A6', 'Dibatalkan': '#E74C3C',
            }
            labels = [d['status'] for d in status_data]
            values = [d['total'] for d in status_data]
            bar_colors = [colors_map.get(l, '#BDC3C7') for l in labels]
            bars = ax.bar(labels, values, color=bar_colors, width=0.5)
            ax.set_title('Distribusi Status Reservasi', fontsize=10)
            ax.bar_label(bars, padding=3, fontsize=9)
            ax.tick_params(axis='x', labelrotation=15, labelsize=8)
        else:
            ax.text(0.5, 0.5, 'Tidak ada data', ha='center', va='center',
                    transform=ax.transAxes)
        self.figure.tight_layout()
        self.canvas.draw()
