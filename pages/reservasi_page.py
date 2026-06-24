from PySide6.QtCore import Qt
from PySide6.QtGui import QColor
from PySide6.QtWidgets import (
    QCheckBox,
    QDialog,
    QHeaderView,
    QMessageBox,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
    QPushButton,
)

import database.database as database
from dialogs.reservasi_dialog import ReservasiDialog
from ui.ui_loader import load_ui

STATUS_COLORS = {
    "Menunggu": "#FFF3CD",
    "Dikonfirmasi": "#D1ECF1",
    "Selesai": "#E2E3E5",
    "Dibatalkan": "#F8D7DA",
}

COL_CHECK = 0
COL_ID = 1
COL_NAMA = 2
COL_TELP = 3
COL_TAMU = 4
COL_TGL = 5
COL_WAKTU = 6
COL_MEJA = 7
COL_STATUS = 8


class NumericTableWidgetItem(QTableWidgetItem):
    def __lt__(self, other):
        left = self.data(Qt.UserRole + 1)
        right = other.data(Qt.UserRole + 1)
        if left is not None and right is not None:
            return int(left) < int(right)
        return super().__lt__(other)


class ReservasiPage(QWidget):
    def __init__(self, nama_pegawai, refresh_callback=None):
        super().__init__()
        self.nama_pegawai = nama_pegawai
        self.refresh_callback = refresh_callback
        self.all_data = []
        self.init_ui()
        self.load_data()

    def init_ui(self):
        self.ui_root = load_ui(self, "reservasi_page.ui")
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.ui_root)

        self.add_btn = self.ui_root.findChild(QPushButton, "primaryButton")
        self.konfirmasi_btn = self.ui_root.findChild(QPushButton, "successButton")
        self.hapus_btn = self.ui_root.findChild(QPushButton, "dangerButton")
        self.pageHeader.setText("📋 Manajemen Reservasi")
        self.add_btn.setText("＋  Tambah Reservasi")
        self.edit_btn.setText("✏️  Edit")
        self.konfirmasi_btn.setText("✅  Konfirmasi")
        self.selesai_btn.setText("🏁  Tandai Selesai")
        self.hapus_btn.setText("🗑️  Hapus Terpilih")
        self.search_input.setPlaceholderText("🔍  Cari nama tamu atau nomor telepon...")
        self.filter_status.addItems(["Semua Status", "Menunggu", "Dikonfirmasi", "Selesai", "Dibatalkan"])
        self.table.setColumnCount(9)
        self.table.setHorizontalHeaderLabels(["✓", "ID", "Nama Tamu", "Telepon", "Tamu", "Tanggal", "Waktu", "Meja", "Status"])
        self.table.cellDoubleClicked.connect(self.edit_reservasi)
        self.table.horizontalHeader().sectionClicked.connect(self._header_clicked)

        hv = self.table.horizontalHeader()
        hv.setSectionResizeMode(COL_CHECK, QHeaderView.ResizeToContents)
        hv.setSectionResizeMode(COL_ID, QHeaderView.ResizeToContents)
        hv.setSectionResizeMode(COL_NAMA, QHeaderView.Stretch)
        hv.setSectionResizeMode(COL_TELP, QHeaderView.ResizeToContents)
        for i in [COL_TAMU, COL_TGL, COL_WAKTU, COL_MEJA, COL_STATUS]:
            hv.setSectionResizeMode(i, QHeaderView.ResizeToContents)

        self.add_btn.clicked.connect(self.tambah_reservasi)
        self.search_input.textChanged.connect(self.apply_filter)
        self.filter_status.currentTextChanged.connect(self.apply_filter)
        self.edit_btn.clicked.connect(self.edit_reservasi_selected)
        self.konfirmasi_btn.clicked.connect(self.konfirmasi_reservasi)
        self.selesai_btn.clicked.connect(lambda: self.update_status("Selesai"))
        self.hapus_btn.clicked.connect(self.hapus_terpilih)

    def load_data(self):
        database.auto_update_reservasi_lewat_waktu()
        conn = database.get_db_connection()
        self.all_data = conn.execute("""
            SELECT r.id, r.nama_tamu, r.no_telepon, r.jumlah_tamu,
                   r.tanggal, r.waktu, m.nomor_meja, r.status
            FROM reservasi r
            LEFT JOIN meja m ON r.meja_id = m.id
            ORDER BY r.tanggal DESC, r.waktu ASC
        """).fetchall()
        conn.close()
        self._populate_table(self.all_data)

    def _populate_table(self, data):
        self.table.setSortingEnabled(False)
        self.table.setRowCount(0)
        for row, d in enumerate(data):
            self.table.insertRow(row)
            bg = QColor(STATUS_COLORS.get(d["status"], "#FFFFFF"))
            chk = QCheckBox()
            chk.setStyleSheet("margin-left:6px;")
            self.table.setCellWidget(row, COL_CHECK, chk)
            items = [
                str(row + 1), d["nama_tamu"], d["no_telepon"], str(d["jumlah_tamu"]),
                d["tanggal"], d["waktu"], d["nomor_meja"] or "-", d["status"],
            ]
            for col_offset, val in enumerate(items):
                item = NumericTableWidgetItem(val) if col_offset == 0 else QTableWidgetItem(val)
                item.setBackground(bg)
                if col_offset == 0:
                    item.setData(Qt.DisplayRole, row + 1)
                    item.setData(Qt.UserRole, d["id"])
                    item.setData(Qt.UserRole + 1, row + 1)
                self.table.setItem(row, col_offset + 1, item)
        self.table.setSortingEnabled(True)

    def _get_row_reservasi_id(self, row):
        item = self.table.item(row, COL_ID)
        if not item:
            return None
        return item.data(Qt.UserRole) or int(item.text())

    def _header_clicked(self, logical_index):
        if logical_index != COL_CHECK:
            return
        any_checked = any(
            self.table.cellWidget(r, COL_CHECK).isChecked()
            for r in range(self.table.rowCount())
            if self.table.cellWidget(r, COL_CHECK)
        )
        for r in range(self.table.rowCount()):
            w = self.table.cellWidget(r, COL_CHECK)
            if w:
                w.setChecked(not any_checked)

    def _get_checked_ids(self):
        ids = []
        for r in range(self.table.rowCount()):
            w = self.table.cellWidget(r, COL_CHECK)
            if w and w.isChecked():
                item_id = self._get_row_reservasi_id(r)
                if item_id:
                    ids.append(int(item_id))
        return ids

    def apply_filter(self):
        search = self.search_input.text().lower()
        status_f = self.filter_status.currentText()
        filtered = [
            d for d in self.all_data
            if (not search or search in d["nama_tamu"].lower() or search in d["no_telepon"].lower())
            and (status_f == "Semua Status" or d["status"] == status_f)
        ]
        self._populate_table(filtered)

    def _get_selected_id(self):
        selected = self.table.selectedItems()
        if not selected:
            QMessageBox.warning(self, "Peringatan", "Pilih data reservasi terlebih dahulu.")
            return None
        return int(self._get_row_reservasi_id(self.table.currentRow()))

    def _do_refresh(self):
        self.load_data()
        if self.refresh_callback:
            self.refresh_callback()

    def tambah_reservasi(self):
        dialog = ReservasiDialog(parent=self)
        if dialog.exec() == QDialog.Accepted:
            self._do_refresh()

    def edit_reservasi(self, row, col):
        if col == COL_CHECK:
            return
        item_id = int(self._get_row_reservasi_id(row))
        dialog = ReservasiDialog(reservasi_id=item_id, parent=self)
        if dialog.exec() == QDialog.Accepted:
            self._do_refresh()

    def edit_reservasi_selected(self):
        item_id = self._get_selected_id()
        if item_id:
            self.edit_reservasi(self.table.currentRow(), COL_ID)

    def hapus_terpilih(self):
        ids = self._get_checked_ids()
        if not ids:
            item_id = self._get_selected_id()
            if not item_id:
                return
            ids = [item_id]
        reply = QMessageBox.question(
            self,
            "Konfirmasi Hapus",
            f"Yakin ingin menghapus {len(ids)} data reservasi yang dipilih?\n"
            "Status meja terkait akan otomatis diperbarui.",
            QMessageBox.Yes | QMessageBox.No,
        )
        if reply == QMessageBox.Yes:
            ok, err = database.hapus_banyak_reservasi(ids)
            if ok:
                self._do_refresh()
            else:
                QMessageBox.critical(self, "Error", f"Gagal menghapus: {err}")

    def konfirmasi_reservasi(self):
        self.update_status("Dikonfirmasi", from_status="Menunggu")

    def update_status(self, new_status, from_status=None):
        item_id = self._get_selected_id()
        if not item_id:
            return
        current_status = self.table.item(self.table.currentRow(), COL_STATUS).text()
        if from_status and current_status != from_status:
            QMessageBox.warning(self, "Peringatan", f"Aksi ini hanya untuk reservasi berstatus '{from_status}'.")
            return
        ok, err = database.update_status_reservasi(item_id, new_status)
        if ok:
            self._do_refresh()
            QMessageBox.information(self, "Sukses", f"Status diubah menjadi '{new_status}'.")
        else:
            QMessageBox.critical(self, "Error", f"Gagal update status: {err}")
