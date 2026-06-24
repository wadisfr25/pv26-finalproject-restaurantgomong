from datetime import datetime

from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PySide6.QtWidgets import QFrame, QHeaderView, QLabel, QTableWidgetItem, QVBoxLayout, QWidget

import database.database as database
from ui.ui_loader import load_ui


def _style_card(card, color):
    card.setStyleSheet(f"""
        QFrame#dashCard {{
            background: white;
            border: 1px solid #DDE4EC;
            border-left: 4px solid {color};
            border-radius: 10px;
            min-height: 80px;
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


class ManagerDashboardPage(QWidget):
    def __init__(self, nama_pegawai):
        super().__init__()
        self.nama_pegawai = nama_pegawai
        self.init_ui()
        self.refresh()

    def init_ui(self):
        self.ui_root = load_ui(self, "manager_dashboard_page.ui")
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.ui_root)

        self.header_label = self.ui_root.findChild(QLabel, "pageHeader")
        self.date_label = self.ui_root.findChild(QLabel, "dateLabel")
        values = [card.findChild(QLabel, "cardValue") for card in self.ui_root.findChildren(QFrame, "dashCard")]
        (
            self.card_total_value,
            self.card_hari_ini_value,
            self.card_menunggu_value,
            self.card_dibatalkan_value,
            self.card_meja_tersedia_value,
            self.card_meja_terisi_value,
            self.card_meja_maintenance_value,
            self.card_total_pegawai_value,
            self.card_manajer_value,
            self.card_staf_value,
            self.card_ai_jam_value,
            self.card_ai_tamu_value,
            self.card_ai_staf_value,
        ) = values
        self.header_label.setText(f"Selamat Datang, {self.nama_pegawai}! 👋")
        self.date_label.setText(f"📅  {datetime.now().strftime('%A, %d %B %Y')}  ·  Dashboard Manajer")
        self.reservasi_group.setTitle("📋  Statistik Reservasi")
        self.meja_group.setTitle("🪑  Statistik Meja")
        self.pegawai_group.setTitle("👥  Statistik Pegawai")
        self.today_group.setTitle("📋  Reservasi Hari Ini")
        titles = [
            "📋 Total Reservasi",
            "📅 Reservasi Hari Ini",
            "⏳ Menunggu Konfirmasi",
            "❌ Dibatalkan (Bulan Ini)",
            "✅ Meja Tersedia",
            "🔴 Meja Terisi",
            "🔧 Maintenance",
            "👤 Total Pegawai",
            "🔑 Manajer",
            "👔 Staf",
            "AI Jam Ramai Hari Ini",
            "AI Estimasi Tamu",
            "AI Saran Staf",
        ]
        colors = [
            "#3498DB", "#27AE60", "#F39C12", "#E74C3C",
            "#27AE60", "#E74C3C", "#F39C12",
            "#9B59B6", "#E67E22", "#16A085",
            "#8E44AD", "#16A085", "#D35400",
        ]
        for card, title, color in zip(self.ui_root.findChildren(QFrame, "dashCard"), titles, colors):
            card.findChild(QLabel, "cardTitle").setText(title)
            _style_card(card, color)
        self.today_table.setColumnCount(5)
        self.today_table.setHorizontalHeaderLabels(["Nama Tamu", "Telepon", "Tamu", "Waktu", "Status"])
        hdr = self.today_table.horizontalHeader()
        hdr.setSectionResizeMode(0, QHeaderView.Stretch)
        for i in range(1, 5):
            hdr.setSectionResizeMode(i, QHeaderView.ResizeToContents)

        self.figure = Figure(figsize=(4, 3), dpi=90, facecolor="none")
        self.canvas = FigureCanvas(self.figure)
        self.chart_layout.addWidget(self.canvas)

    def refresh(self):
        database.auto_update_reservasi_lewat_waktu()
        today = datetime.now().strftime("%Y-%m-%d")
        month_start = datetime.now().strftime("%Y-%m-01")
        conn = database.get_db_connection()

        total = conn.execute("SELECT COUNT(*) FROM reservasi WHERE status != 'Dibatalkan'").fetchone()[0]
        hari_ini = conn.execute(
            "SELECT COUNT(*) FROM reservasi WHERE tanggal = ? AND status != 'Dibatalkan'", (today,)
        ).fetchone()[0]
        menunggu = conn.execute("SELECT COUNT(*) FROM reservasi WHERE status = 'Menunggu'").fetchone()[0]
        dibatalkan = conn.execute(
            "SELECT COUNT(*) FROM reservasi WHERE status = 'Dibatalkan' AND tanggal >= ?", (month_start,)
        ).fetchone()[0]

        self.card_total_value.setText(str(total))
        self.card_hari_ini_value.setText(str(hari_ini))
        self.card_menunggu_value.setText(str(menunggu))
        self.card_dibatalkan_value.setText(str(dibatalkan))

        def meja_count(status):
            return conn.execute("SELECT COUNT(*) FROM meja WHERE status = ?", (status,)).fetchone()[0]

        self.card_meja_tersedia_value.setText(str(meja_count("Tersedia")))
        self.card_meja_terisi_value.setText(str(meja_count("Terisi")))
        self.card_meja_maintenance_value.setText(str(meja_count("Maintenance")))

        total_peg = conn.execute("SELECT COUNT(*) FROM pegawai").fetchone()[0]
        jml_manajer = conn.execute("SELECT COUNT(*) FROM pegawai WHERE jabatan = 'Manajer'").fetchone()[0]
        jml_staf = conn.execute("SELECT COUNT(*) FROM pegawai WHERE jabatan = 'Staf'").fetchone()[0]
        self.card_total_pegawai_value.setText(str(total_peg))
        self.card_manajer_value.setText(str(jml_manajer))
        self.card_staf_value.setText(str(jml_staf))

        prediksi = database.get_prediksi_jam_ramai(today)
        self.card_ai_jam_value.setText(prediksi["waktu"] or "-")
        self.card_ai_tamu_value.setText(f"{prediksi['estimasi_tamu']} orang")
        self.card_ai_staf_value.setText(prediksi.get("saran_staf", "-"))

        rows = conn.execute("""
            SELECT r.nama_tamu, r.no_telepon, r.jumlah_tamu, r.waktu, r.status
            FROM reservasi r
            WHERE r.tanggal = ?
            ORDER BY r.waktu ASC
        """, (today,)).fetchall()
        status_data = conn.execute("SELECT status, COUNT(*) as total FROM reservasi GROUP BY status").fetchall()
        conn.close()

        self.today_table.setRowCount(0)
        for row, d in enumerate(rows):
            self.today_table.insertRow(row)
            self.today_table.setItem(row, 0, QTableWidgetItem(d["nama_tamu"]))
            self.today_table.setItem(row, 1, QTableWidgetItem(d["no_telepon"]))
            self.today_table.setItem(row, 2, QTableWidgetItem(str(d["jumlah_tamu"])))
            self.today_table.setItem(row, 3, QTableWidgetItem(d["waktu"]))
            self.today_table.setItem(row, 4, QTableWidgetItem(d["status"]))

        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.set_facecolor("#F8F9FA")
        if status_data:
            colors_map = {
                "Menunggu": "#F39C12",
                "Dikonfirmasi": "#3498DB",
                "Selesai": "#95A5A6",
                "Dibatalkan": "#E74C3C",
            }
            labels = [d["status"] for d in status_data]
            values = [d["total"] for d in status_data]
            bars = ax.bar(labels, values, color=[colors_map.get(l, "#BDC3C7") for l in labels], width=0.5)
            ax.set_title("Distribusi Status Reservasi", fontsize=10)
            ax.bar_label(bars, padding=3, fontsize=9)
            ax.tick_params(axis="x", labelrotation=15, labelsize=8)
        else:
            ax.text(0.5, 0.5, "Tidak ada data", ha="center", va="center", transform=ax.transAxes)
        self.figure.tight_layout()
        self.canvas.draw()
