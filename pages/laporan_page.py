from PySide6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel,
                               QPushButton, QTableWidget, QTableWidgetItem,
                               QHeaderView, QComboBox, QDateEdit, QMessageBox,
                               QFileDialog, QGroupBox, QAbstractSpinBox)
from PySide6.QtCore import QDate, Qt
from PySide6.QtGui import QPdfWriter, QTextDocument
from datetime import datetime
import csv
import html

import database.database as database
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class ReportDateEdit(QDateEdit):
    def __init__(self, date):
        super().__init__(date)
        self.setCalendarPopup(True)
        self.setDisplayFormat("dd MMM yyyy")
        self.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.setKeyboardTracking(False)
        self.setFixedWidth(136)

    def wheelEvent(self, event):
        event.ignore()


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

        title = QLabel("Laporan & Statistik")
        title.setObjectName("pageHeader")
        layout.addWidget(title)

        filter_grp = QGroupBox("Filter Data")
        filter_grp.setObjectName("reportFilterGroup")
        filter_layout = QVBoxLayout(filter_grp)
        filter_layout.setContentsMargins(18, 20, 18, 16)
        filter_layout.setSpacing(12)

        f_lay = QHBoxLayout()
        f_lay.setSpacing(12)

        date_from_label = QLabel("Dari")
        date_from_label.setObjectName("reportFilterLabel")
        self.date_from = ReportDateEdit(QDate.currentDate().addDays(-30))
        self.date_from.setObjectName("reportDateInput")
        f_lay.addWidget(self._make_filter_field(date_from_label, self.date_from))

        date_to_label = QLabel("Sampai")
        date_to_label.setObjectName("reportFilterLabel")
        self.date_to = ReportDateEdit(QDate.currentDate())
        self.date_to.setObjectName("reportDateInput")
        f_lay.addWidget(self._make_filter_field(date_to_label, self.date_to))

        status_label = QLabel("Status")
        status_label.setObjectName("reportFilterLabel")
        self.filter_status = QComboBox()
        self.filter_status.setObjectName("reportStatusFilter")
        self.filter_status.setFixedWidth(150)
        self.filter_status.addItems(
            ["Semua Status", "Menunggu", "Dikonfirmasi", "Selesai", "Dibatalkan"]
        )
        f_lay.addWidget(self._make_filter_field(status_label, self.filter_status))

        apply_btn = QPushButton("Terapkan")
        apply_btn.setObjectName("reportApplyButton")
        apply_btn.setFixedWidth(108)
        apply_btn.setFixedHeight(38)
        apply_btn.clicked.connect(self.refresh)
        f_lay.addWidget(apply_btn, 0, Qt.AlignBottom)

        f_lay.addStretch(1)

        action_lay = QHBoxLayout()
        action_lay.setSpacing(10)
        action_lay.addStretch(1)

        export_btn = QPushButton("Export CSV")
        export_btn.setObjectName("primaryButton")
        export_btn.setFixedHeight(38)
        export_btn.clicked.connect(self.export_csv)
        action_lay.addWidget(export_btn)

        export_pdf_btn = QPushButton("Export PDF")
        export_pdf_btn.setObjectName("successButton")
        export_pdf_btn.setFixedHeight(38)
        export_pdf_btn.clicked.connect(self.export_pdf)
        action_lay.addWidget(export_pdf_btn)

        self.filter_summary = QLabel()
        self.filter_summary.setObjectName("reportFilterSummary")

        filter_layout.addLayout(f_lay)
        filter_layout.addLayout(action_lay)
        filter_layout.addWidget(self.filter_summary)
        layout.addWidget(filter_grp)

        ai_grp = QGroupBox("Analisis AI")
        ai_layout = QVBoxLayout(ai_grp)
        ai_layout.setContentsMargins(18, 14, 18, 14)
        self.ai_summary = QLabel()
        self.ai_summary.setWordWrap(True)
        self.ai_summary.setObjectName("reportFilterSummary")
        ai_layout.addWidget(self.ai_summary)
        layout.addWidget(ai_grp)

        content = QHBoxLayout()
        content.setSpacing(16)

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

    def _make_filter_field(self, label, field):
        wrapper = QWidget()
        wrapper.setObjectName("reportFilterField")
        wrapper_layout = QVBoxLayout(wrapper)
        wrapper_layout.setContentsMargins(0, 0, 0, 0)
        wrapper_layout.setSpacing(5)
        wrapper_layout.addWidget(label)
        wrapper_layout.addWidget(field)
        return wrapper

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
                str(d['id']), d['nama_tamu'], str(d['jumlah_tamu']),
                d['tanggal'], d['waktu'], d['status']
            ]):
                self.table.setItem(row, col, QTableWidgetItem(val))
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
        ax.set_facecolor('#F8F9FA')

        status_counts = {}
        for d in self.all_data:
            status_counts[d['status']] = status_counts.get(d['status'], 0) + 1

        if status_counts:
            colors = {
                'Menunggu': '#F39C12',
                'Dikonfirmasi': '#3498DB',
                'Selesai': '#95A5A6',
                'Dibatalkan': '#E74C3C',
            }
            labels = list(status_counts.keys())
            values = list(status_counts.values())
            bar_colors = [colors.get(label, '#BDC3C7') for label in labels]
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
            f"laporan_gomong_{datetime.now().strftime('%Y%m%d')}.csv",
            "CSV Files (*.csv)"
        )
        if not path:
            return
        if not path.lower().endswith(".csv"):
            path += ".csv"

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
            QMessageBox.critical(self, "Error", f"Gagal export CSV: {e}")

    def export_pdf(self):
        if not self.all_data:
            QMessageBox.warning(self, "Peringatan", "Tidak ada data untuk diekspor.")
            return

        path, _ = QFileDialog.getSaveFileName(
            self, "Export PDF",
            f"laporan_gomong_{datetime.now().strftime('%Y%m%d')}.pdf",
            "PDF Files (*.pdf)"
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
