from PySide6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel,
                               QTableWidget, QTableWidgetItem, QHeaderView, QFrame)
from PySide6.QtCore import Qt
from datetime import datetime
import database.database as database
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class CardWidget(QFrame):
    def __init__(self, title, value, emoji="📌", color="#3498DB"):
        super().__init__()
        self.setObjectName("dashCard")
        self.setFrameShape(QFrame.NoFrame)
        self.setStyleSheet(f"""
            #dashCard {{
                background: white;
                border-radius: 14px;
                border: 1.5px solid #DDE4EC;
                border-left: 4px solid {color};
                min-height: 86px;
            }}
        """)
        layout = QVBoxLayout(self)
        layout.setContentsMargins(18, 12, 18, 12)

        self.value_lbl = QLabel(str(value))
        self.value_lbl.setObjectName("cardValue")
        self.value_lbl.setAlignment(Qt.AlignCenter)

        title_lbl = QLabel(f"{emoji} {title}")
        title_lbl.setObjectName("cardTitle")
        title_lbl.setAlignment(Qt.AlignCenter)
        title_lbl.setWordWrap(True)

        layout.addWidget(self.value_lbl)
        layout.addWidget(title_lbl)

    def update_value(self, val):
        self.value_lbl.setText(str(val))


class DashboardPage(QWidget):
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

        date_lbl = QLabel(f"📅  {datetime.now().strftime('%A, %d %B %Y')}")
        date_lbl.setObjectName("dateLabel")
        layout.addWidget(date_lbl)

        # Cards row — hanya 2 kartu (tanpa lantai)
        cards_row = QHBoxLayout()
        cards_row.setSpacing(16)
        self.card_hari_ini = CardWidget("Reservasi Hari Ini", "0", "📋", "#3498DB")
        self.card_menunggu = CardWidget("Menunggu Konfirmasi", "0", "⏳", "#F39C12")
        self.card_selesai  = CardWidget("Selesai Hari Ini",    "0", "✅", "#27AE60")
        self.card_total    = CardWidget("Total Reservasi Aktif","0", "📊", "#9B59B6")
        for card in [self.card_hari_ini, self.card_menunggu,
                     self.card_selesai, self.card_total]:
            cards_row.addWidget(card)
        layout.addLayout(cards_row)

        # Bottom: table + chart
        bottom = QHBoxLayout()
        bottom.setSpacing(16)

        # Today's table
        table_wrap = QWidget()
        tw_layout = QVBoxLayout(table_wrap)
        tw_layout.setContentsMargins(0, 0, 0, 0)
        tw_layout.setSpacing(8)

        section_lbl = QLabel("Reservasi Hari Ini")
        section_lbl.setObjectName("sectionTitle")
        tw_layout.addWidget(section_lbl)

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
        tw_layout.addWidget(self.today_table)

        # Status pie chart
        self.figure = Figure(figsize=(4, 3), dpi=90, facecolor='none')
        self.canvas = FigureCanvas(self.figure)
        self.canvas.setMinimumWidth(280)

        bottom.addWidget(table_wrap, 3)
        bottom.addWidget(self.canvas, 2)
        layout.addLayout(bottom)

    def refresh(self):
        today = datetime.now().strftime("%Y-%m-%d")
        conn = database.get_db_connection()

        today_count = conn.execute(
            "SELECT COUNT(*) FROM reservasi WHERE tanggal = ? AND status != 'Dibatalkan'",
            (today,)
        ).fetchone()[0]

        menunggu_count = conn.execute(
            "SELECT COUNT(*) FROM reservasi WHERE status = 'Menunggu'"
        ).fetchone()[0]

        selesai_count = conn.execute(
            "SELECT COUNT(*) FROM reservasi WHERE tanggal = ? AND status = 'Selesai'",
            (today,)
        ).fetchone()[0]

        total_aktif = conn.execute(
            "SELECT COUNT(*) FROM reservasi WHERE status IN ('Menunggu','Dikonfirmasi','Duduk')"
        ).fetchone()[0]

        self.card_hari_ini.update_value(today_count)
        self.card_menunggu.update_value(menunggu_count)
        self.card_selesai.update_value(selesai_count)
        self.card_total.update_value(total_aktif)

        # Today's table
        rows = conn.execute("""
            SELECT r.nama_tamu, r.no_telepon, r.jumlah_tamu, r.waktu, r.status
            FROM reservasi r
            WHERE r.tanggal = ?
            ORDER BY r.waktu ASC
        """, (today,)).fetchall()

        # Status distribution pie
        pie_data = conn.execute("""
            SELECT status, COUNT(*) as total
            FROM reservasi WHERE status != 'Dibatalkan'
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

        # Update chart — distribusi status
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        if pie_data:
            labels = [f"{d['status']}\n({d['total']})" for d in pie_data]
            values = [d['total'] for d in pie_data]
            colors = ['#F39C12', '#3498DB', '#27AE60', '#E2E3E5', '#E74C3C']
            ax.pie(values, labels=labels, colors=colors[:len(values)],
                   autopct='%1.0f%%', startangle=90)
            ax.set_title('Distribusi Status Reservasi', fontsize=10)
        self.figure.tight_layout()
        self.canvas.draw()
        
