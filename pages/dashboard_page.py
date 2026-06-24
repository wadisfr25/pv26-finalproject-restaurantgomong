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
            border-radius: 14px;
            border: 1.5px solid #DDE4EC;
            border-left: 4px solid {color};
            min-height: 86px;
        }}
    """)


class DashboardPage(QWidget):
    def __init__(self, nama_pegawai):
        super().__init__()
        self.nama_pegawai = nama_pegawai
        self.init_ui()
        self.refresh()

    def init_ui(self):
        self.ui_root = load_ui(self, "dashboard_page.ui")
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.ui_root)

        self.header_label = self.ui_root.findChild(QLabel, "pageHeader")
        self.date_label = self.ui_root.findChild(QLabel, "dateLabel")
        cards = self.ui_root.findChildren(QFrame, "dashCard")
        values = [card.findChild(QLabel, "cardValue") for card in cards]
        (
            self.card_hari_ini_value,
            self.card_menunggu_value,
            self.card_selesai_value,
            self.card_total_value,
        ) = values
        self.header_label.setText(f"Selamat Datang, {self.nama_pegawai}! 👋")
        self.date_label.setText(f"📅  {datetime.now().strftime('%A, %d %B %Y')}")
        titles = [
            "📋 Reservasi Hari Ini",
            "⏳ Menunggu Konfirmasi",
            "✅ Selesai Hari Ini",
            "📊 Total Reservasi Aktif",
        ]
        colors = ["#3498DB", "#F39C12", "#27AE60", "#9B59B6"]
        for card, title, color in zip(cards, titles, colors):
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
        conn = database.get_db_connection()

        today_count = conn.execute(
            "SELECT COUNT(*) FROM reservasi WHERE tanggal = ? AND status != 'Dibatalkan'", (today,)
        ).fetchone()[0]
        menunggu_count = conn.execute("SELECT COUNT(*) FROM reservasi WHERE status = 'Menunggu'").fetchone()[0]
        selesai_count = conn.execute(
            "SELECT COUNT(*) FROM reservasi WHERE tanggal = ? AND status = 'Selesai'", (today,)
        ).fetchone()[0]
        total_aktif = conn.execute(
            "SELECT COUNT(*) FROM reservasi WHERE status IN ('Menunggu','Dikonfirmasi')"
        ).fetchone()[0]

        self.card_hari_ini_value.setText(str(today_count))
        self.card_menunggu_value.setText(str(menunggu_count))
        self.card_selesai_value.setText(str(selesai_count))
        self.card_total_value.setText(str(total_aktif))

        rows = conn.execute("""
            SELECT r.nama_tamu, r.no_telepon, r.jumlah_tamu, r.waktu, r.status
            FROM reservasi r
            WHERE r.tanggal = ?
            ORDER BY r.waktu ASC
        """, (today,)).fetchall()

        pie_data = conn.execute("""
            SELECT status, COUNT(*) as total
            FROM reservasi WHERE status != 'Dibatalkan'
            GROUP BY status
        """).fetchall()
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
        if pie_data:
            labels = [f"{d['status']}\n({d['total']})" for d in pie_data]
            values = [d["total"] for d in pie_data]
            colors = ["#F39C12", "#3498DB", "#27AE60", "#E2E3E5", "#E74C3C"]
            ax.pie(values, labels=labels, colors=colors[:len(values)], autopct="%1.0f%%", startangle=90)
            ax.set_title("Distribusi Status Reservasi", fontsize=10)
        self.figure.tight_layout()
        self.canvas.draw()
