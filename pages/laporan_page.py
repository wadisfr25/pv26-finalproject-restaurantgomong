import csv
import html
from datetime import datetime

from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PySide6.QtCore import QDate, Qt
from PySide6.QtGui import QPdfWriter, QTextDocument
from PySide6.QtWidgets import (
    QFileDialog,
    QComboBox,
    QDateEdit,
    QHeaderView,
    QLabel,
    QMessageBox,
    QPushButton,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
)

import database.database as database
from ui.ui_loader import load_ui


class NumericTableWidgetItem(QTableWidgetItem):
    def __lt__(self, other):
        left = self.data(Qt.UserRole + 1)
        right = other.data(Qt.UserRole + 1)
        if left is not None and right is not None:
            return int(left) < int(right)
        return super().__lt__(other)


class LaporanPage(QWidget):
    def __init__(self):
        super().__init__()
        self.all_data = []
        self.init_ui()
        self.refresh()

    def init_ui(self):
        self.ui_root = load_ui(self, "laporan_page.ui")
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.ui_root)

        date_edits = self.ui_root.findChildren(QDateEdit, "reportDateInput")
        self.date_from, self.date_to = date_edits
        self.filter_status = self.ui_root.findChild(QComboBox, "reportStatusFilter")
        self.apply_btn = self.ui_root.findChild(QPushButton, "reportApplyButton")
        self.export_btn = self.ui_root.findChild(QPushButton, "primaryButton")
        self.export_pdf_btn = self.ui_root.findChild(QPushButton, "successButton")
        summaries = self.ui_root.findChildren(QLabel, "reportFilterSummary")
        self.filter_summary, self.ai_summary = summaries
        self.pageHeader.setText("Laporan & Statistik")
        self.date_from.setDate(QDate.currentDate().addDays(-30))
        self.date_to.setDate(QDate.currentDate())
        self.filter_status.addItems(["Semua Status", "Menunggu", "Dikonfirmasi", "Selesai", "Dibatalkan"])

        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels(["ID", "Nama Tamu", "Tamu", "Tanggal", "Waktu", "Status"])
        hdr = self.table.horizontalHeader()
        hdr.setSectionResizeMode(0, QHeaderView.Fixed)
        hdr.resizeSection(0, 56)
        hdr.setSectionResizeMode(1, QHeaderView.Stretch)
        for i in [2, 3, 4, 5]:
            hdr.setSectionResizeMode(i, QHeaderView.ResizeToContents)

        self.figure = Figure(figsize=(5, 4), dpi=90, facecolor="none")
        self.canvas = FigureCanvas(self.figure)
        self.chart_layout.addWidget(self.canvas)

        self.apply_btn.clicked.connect(self.refresh)
        self.export_btn.clicked.connect(self.export_csv)
        self.export_pdf_btn.clicked.connect(self.export_pdf)

    def refresh(self):
        database.auto_update_reservasi_lewat_waktu()
        date_from = self.date_from.date().toString("yyyy-MM-dd")
        date_to = self.date_to.date().toString("yyyy-MM-dd")
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

        self.table.setSortingEnabled(False)
        self.table.setRowCount(0)
        for row, d in enumerate(self.all_data):
            self.table.insertRow(row)
            for col, val in enumerate([
                str(row + 1), d["nama_tamu"], str(d["jumlah_tamu"]),
                d["tanggal"], d["waktu"], d["status"],
            ]):
                item = NumericTableWidgetItem(val) if col == 0 else QTableWidgetItem(val)
                if col == 0:
                    item.setData(Qt.DisplayRole, row + 1)
                    item.setData(Qt.UserRole, d["id"])
                    item.setData(Qt.UserRole + 1, row + 1)
                    item.setTextAlignment(Qt.AlignCenter)
                self.table.setItem(row, col, item)
        self.table.setSortingEnabled(True)

        self.filter_summary.setText(
            f"Menampilkan {len(self.all_data)} data reservasi dari {date_from} sampai {date_to}"
            + ("" if status_filter == "Semua Status" else f" dengan status {status_filter}")
        )
        prediksi = database.get_prediksi_jam_ramai(date_to)
        if prediksi["waktu"]:
            self.ai_summary.setText(
                f"Prediksi jam ramai untuk {date_to}: {prediksi['waktu']} | "
                f"Estimasi tamu: {prediksi['estimasi_tamu']} orang | "
                f"Rekomendasi staf: {prediksi.get('saran_staf', '-')} | "
                f"{prediksi['keterangan']}"
            )
        else:
            self.ai_summary.setText(prediksi["keterangan"])
        self._update_chart()

    def _update_chart(self):
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.set_facecolor("#F8F9FA")
        status_counts = {}
        for d in self.all_data:
            status_counts[d["status"]] = status_counts.get(d["status"], 0) + 1

        if status_counts:
            colors = {
                "Menunggu": "#F39C12",
                "Dikonfirmasi": "#3498DB",
                "Selesai": "#95A5A6",
                "Dibatalkan": "#E74C3C",
            }
            labels = list(status_counts.keys())
            values = list(status_counts.values())
            bars = ax.bar(labels, values, color=[colors.get(label, "#BDC3C7") for label in labels], width=0.5)
            ax.set_title("Distribusi Status Reservasi", fontsize=11)
            ax.bar_label(bars, padding=3, fontsize=9)
            ax.tick_params(axis="x", labelrotation=15)
        else:
            ax.text(0.5, 0.5, "Tidak ada data", ha="center", va="center", transform=ax.transAxes)
        self.figure.tight_layout()
        self.canvas.draw()

    def export_csv(self):
        if not self.all_data:
            QMessageBox.warning(self, "Peringatan", "Tidak ada data untuk diekspor.")
            return
        path, _ = QFileDialog.getSaveFileName(
            self, "Export CSV", f"laporan_gomong_{datetime.now().strftime('%Y%m%d')}.csv", "CSV Files (*.csv)"
        )
        if not path:
            return
        if not path.lower().endswith(".csv"):
            path += ".csv"
        try:
            with open(path, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(["ID", "Nama Tamu", "Jumlah Tamu", "Tanggal", "Waktu", "Status"])
                for d in self.all_data:
                    writer.writerow([d["id"], d["nama_tamu"], d["jumlah_tamu"], d["tanggal"], d["waktu"], d["status"]])
            QMessageBox.information(self, "Sukses", f"Data berhasil diekspor:\n{path}")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Gagal export CSV: {e}")

    def export_pdf(self):
        if not self.all_data:
            QMessageBox.warning(self, "Peringatan", "Tidak ada data untuk diekspor.")
            return
        path, _ = QFileDialog.getSaveFileName(
            self, "Export PDF", f"laporan_gomong_{datetime.now().strftime('%Y%m%d')}.pdf", "PDF Files (*.pdf)"
        )
        if not path:
            return
        if not path.lower().endswith(".pdf"):
            path += ".pdf"

        date_from = self.date_from.date().toString("yyyy-MM-dd")
        date_to = self.date_to.date().toString("yyyy-MM-dd")
        status_filter = self.filter_status.currentText()
        rows_html = ""
        for d in self.all_data:
            rows_html += (
                "<tr>"
                f"<td>{html.escape(str(d['id']))}</td>"
                f"<td>{html.escape(d['nama_tamu'])}</td>"
                f"<td>{html.escape(str(d['jumlah_tamu']))}</td>"
                f"<td>{html.escape(d['tanggal'])}</td>"
                f"<td>{html.escape(d['waktu'])}</td>"
                f"<td>{html.escape(d['status'])}</td>"
                "</tr>"
            )

        doc = QTextDocument()
        doc.setHtml(f"""
            <html>
            <head>
                <style>
                    body {{ font-family: Arial, sans-serif; color: #1E2D3D; }}
                    h1 {{ font-size: 20px; margin-bottom: 4px; }}
                    p {{ color: #566573; font-size: 11px; }}
                    table {{ border-collapse: collapse; width: 100%; margin-top: 12px; }}
                    th {{ background: #F0F2F5; font-weight: bold; }}
                    th, td {{ border: 1px solid #D6DBDF; padding: 6px; font-size: 10px; }}
                </style>
            </head>
            <body>
                <h1>Laporan Reservasi Restaurant Gomong</h1>
                <p>Periode: {date_from} sampai {date_to} | Status: {html.escape(status_filter)}</p>
                <table>
                    <tr>
                        <th>ID</th><th>Nama Tamu</th><th>Jumlah Tamu</th>
                        <th>Tanggal</th><th>Waktu</th><th>Status</th>
                    </tr>
                    {rows_html}
                </table>
            </body>
            </html>
        """)
        try:
            writer = QPdfWriter(path)
            writer.setTitle("Laporan Reservasi Restaurant Gomong")
            doc.print_(writer)
            QMessageBox.information(self, "Sukses", f"Data berhasil diekspor:\n{path}")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Gagal export PDF: {e}")
