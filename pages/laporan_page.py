from PySide6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel,
                               QPushButton, QTableWidget, QTableWidgetItem,
                               QHeaderView, QComboBox, QDateEdit, QMessageBox,
                               QFileDialog, QGroupBox)
from PySide6.QtCore import Qt, QDate
from datetime import datetime
import database
import csv
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class LaporanPage(QWidget):
    def __init__(self):
        super().__init__()
        self.all_data = []
        self.init_ui()
        self.refresh()

    def init_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(28, 24, 28, 24)
        layout.setSpacing(18)

        title = QLabel("📊 Laporan & Statistik")
        title.setObjectName("pageHeader")
        layout.addWidget(title)

        # Filter group — tanpa filter lantai
        filter_grp = QGroupBox("Filter Data")
        f_lay = QHBoxLayout(filter_grp)

        f_lay.addWidget(QLabel("Dari:"))
        self.date_from = QDateEdit(QDate.currentDate().addDays(-30))
        self.date_from.setCalendarPopup(True)
        f_lay.addWidget(self.date_from)

        f_lay.addWidget(QLabel("Sampai:"))
        self.date_to = QDateEdit(QDate.currentDate())
        self.date_to.setCalendarPopup(True)
        f_lay.addWidget(self.date_to)

        self.filter_status = QComboBox()
        self.filter_status.addItems(
            ["Semua Status", "Menunggu", "Dikonfirmasi", "Duduk", "Selesai", "Dibatalkan"]
        )
        f_lay.addWidget(self.filter_status)

        apply_btn = QPushButton("🔍  Terapkan")
        apply_btn.clicked.connect(self.refresh)
        f_lay.addWidget(apply_btn)

        f_lay.addStretch()

        export_btn = QPushButton("📥  Export CSV")
        export_btn.setObjectName("primaryButton")
        export_btn.clicked.connect(self.export_csv)
        f_lay.addWidget(export_btn)

        layout.addWidget(filter_grp)

        # Content
        content = QHBoxLayout()
        content.setSpacing(16)

        # Table — tanpa kolom Lantai
        self.table = QTableWidget()
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels(
            ["ID", "Nama Tamu", "Tamu", "Tanggal", "Waktu", "Status"]
        )
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.table.setSelectionBehavior(QTableWidget.SelectRows)
        self.table.verticalHeader().setVisible(False)
        self.table.setSortingEnabled(True)
        hdr = self.table.horizontalHeader()
        hdr.setSectionResizeMode(1, QHeaderView.Stretch)
        for i in [0, 2, 3, 4, 5]:
            hdr.setSectionResizeMode(i, QHeaderView.ResizeToContents)

        self.figure = Figure(figsize=(5, 4), dpi=90, facecolor='none')
        self.canvas = FigureCanvas(self.figure)
        self.canvas.setMinimumWidth(320)

        content.addWidget(self.table, 3)
        content.addWidget(self.canvas, 2)
        layout.addLayout(content)

    def refresh(self):
        date_from = self.date_from.date().toString("yyyy-MM-dd")
        date_to   = self.date_to.date().toString("yyyy-MM-dd")
        status_filter = self.filter_status.currentText()

        query = """
            SELECT r.id, r.nama_tamu, r.jumlah_tamu, r.tanggal, r.waktu, r.status
            FROM reservasi r
            WHERE r.tanggal BETWEEN ? AND ?
        """
        params = [date_from, date_to]
        if status_filter != "Semua Status":
            query += " AND r.status = ?"
            params.append(status_filter)
        query += " ORDER BY r.tanggal DESC, r.waktu ASC"

        conn = database.get_db_connection()
        self.all_data = conn.execute(query, params).fetchall()
        conn.close()

        self.table.setRowCount(0)
        for row, d in enumerate(self.all_data):
            self.table.insertRow(row)
            for col, val in enumerate([
                str(d['id']), d['nama_tamu'], str(d['jumlah_tamu']),
                d['tanggal'], d['waktu'], d['status']
            ]):
                self.table.setItem(row, col, QTableWidgetItem(val))

        self._update_chart()

    def _update_chart(self):
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.set_facecolor('#F8F9FA')

        status_counts = {}
        for d in self.all_data:
            status_counts[d['status']] = status_counts.get(d['status'], 0) + 1

        if status_counts:
            colors = {
                'Menunggu': '#F39C12', 'Dikonfirmasi': '#3498DB',
                'Duduk': '#27AE60', 'Selesai': '#95A5A6', 'Dibatalkan': '#E74C3C',
            }
            labels = list(status_counts.keys())
            values = list(status_counts.values())
            bar_colors = [colors.get(l, '#BDC3C7') for l in labels]
            bars = ax.bar(labels, values, color=bar_colors, width=0.5)
            ax.set_title('Distribusi Status Reservasi', fontsize=11)
            ax.bar_label(bars, padding=3, fontsize=9)
            ax.tick_params(axis='x', labelrotation=15)
        else:
            ax.text(0.5, 0.5, 'Tidak ada data', ha='center', va='center',
                    transform=ax.transAxes)

        self.figure.tight_layout()
        self.canvas.draw()

    def export_csv(self):
        if not self.all_data:
            QMessageBox.warning(self, "Peringatan", "Tidak ada data untuk diekspor.")
            return
        path, _ = QFileDialog.getSaveFileName(
            self, "Export CSV",
            f"laporan_wadis_{datetime.now().strftime('%Y%m%d')}.csv",
            "CSV Files (*.csv)"
        )
        if path:
            try:
                with open(path, 'w', newline='', encoding='utf-8') as f:
                    writer = csv.writer(f)
                    writer.writerow(["ID", "Nama Tamu", "Jumlah Tamu", "Tanggal", "Waktu", "Status"])
                    for d in self.all_data:
                        writer.writerow([
                            d['id'], d['nama_tamu'], d['jumlah_tamu'],
                            d['tanggal'], d['waktu'], d['status']
                        ])
                QMessageBox.information(self, "Sukses", f"Data berhasil diekspor:\n{path}")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Gagal export: {e}")
