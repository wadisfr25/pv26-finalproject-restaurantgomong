from PySide6.QtCore import Qt
from PySide6.QtGui import QColor
from PySide6.QtWidgets import (
    QCheckBox,
    QDialog,
    QHeaderView,
    QMessageBox,
    QPushButton,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
)

import database.database as database
from dialogs.pegawai_dialog import PegawaiDialog
from ui.ui_loader import load_ui

JABATAN_COLORS = {
    "Manajer": "#D1ECF1",
    "Staf": "#F8F9FA",
}

COL_CHECK = 0
COL_ID = 1
COL_NAMA = 2
COL_USER = 3
COL_JABATAN = 4


class PegawaiPage(QWidget):
    def __init__(self, refresh_manager_callback=None):
        super().__init__()
        self.refresh_manager_callback = refresh_manager_callback
        self.all_data = []
        self.init_ui()
        self.refresh()

    def init_ui(self):
        self.ui_root = load_ui(self, "pegawai_page.ui")
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.ui_root)

        self.add_btn = self.ui_root.findChild(QPushButton, "primaryButton")
        self.hapus_btn = self.ui_root.findChild(QPushButton, "dangerButton")
        self.pageHeader.setText("👥 Manajemen Pegawai")
        self.add_btn.setText("＋  Tambah Pegawai")
        self.edit_btn.setText("✏️  Edit")
        self.hapus_btn.setText("🗑️  Hapus Terpilih")
        self.filter_jabatan.addItems(["Semua Jabatan", "Manajer", "Staf"])
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["✓", "No", "Nama", "Username", "Jabatan"])
        self.table.cellDoubleClicked.connect(self.edit_pegawai)
        self.table.horizontalHeader().sectionClicked.connect(self._header_clicked)

        hv = self.table.horizontalHeader()
        hv.setSectionResizeMode(COL_CHECK, QHeaderView.ResizeToContents)
        hv.setSectionResizeMode(COL_ID, QHeaderView.ResizeToContents)
        hv.setSectionResizeMode(COL_NAMA, QHeaderView.Stretch)
        hv.setSectionResizeMode(COL_USER, QHeaderView.Stretch)
        hv.setSectionResizeMode(COL_JABATAN, QHeaderView.ResizeToContents)

        self.add_btn.clicked.connect(self.tambah_pegawai)
        self.search_input.textChanged.connect(self.apply_filter)
        self.filter_jabatan.currentTextChanged.connect(self.apply_filter)
        self.edit_btn.clicked.connect(self.edit_pegawai_selected)
        self.hapus_btn.clicked.connect(self.hapus_terpilih)

    def refresh(self, reset_filter=False, select_id=None):
        if reset_filter:
            self.search_input.clear()
            self.filter_jabatan.setCurrentText("Semua Jabatan")
        self.all_data = database.get_all_pegawai()
        self.apply_filter()
        if select_id is not None:
            self._select_row_by_id(select_id)
        if self.refresh_manager_callback:
            self.refresh_manager_callback()

    def apply_filter(self):
        search = self.search_input.text().strip().lower()
        jabatan_filter = self.filter_jabatan.currentText()
        data = [
            d for d in self.all_data
            if (not search or search in d["nama"].lower() or search in d["username"].lower())
            and (jabatan_filter == "Semua Jabatan" or d["jabatan"] == jabatan_filter)
        ]

        self.table.setSortingEnabled(False)
        self.table.setRowCount(0)
        for row, d in enumerate(data):
            self.table.insertRow(row)
            bg = QColor(JABATAN_COLORS.get(d["jabatan"], "#FFFFFF"))
            chk = QCheckBox()
            chk.setStyleSheet("margin-left:6px;")
            self.table.setCellWidget(row, COL_CHECK, chk)
            for col_offset, val in enumerate([str(row + 1), d["nama"], d["username"], d["jabatan"]]):
                item = QTableWidgetItem(val)
                item.setBackground(bg)
                if col_offset == 0:
                    item.setData(Qt.UserRole, d["id"])
                self.table.setItem(row, col_offset + 1, item)
        self.table.setSortingEnabled(True)

    def _select_row_by_id(self, pegawai_id):
        for row in range(self.table.rowCount()):
            item = self.table.item(row, COL_ID)
            if item and item.data(Qt.UserRole) == pegawai_id:
                self.table.selectRow(row)
                self.table.scrollToItem(item)
                break

    def _get_row_pegawai_id(self, row):
        item = self.table.item(row, COL_ID)
        return item.data(Qt.UserRole) if item else None

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
                ids.append(self._get_row_pegawai_id(r))
        return ids

    def _get_selected_id(self):
        selected = self.table.selectedItems()
        if not selected:
            QMessageBox.warning(self, "Peringatan", "Pilih data pegawai terlebih dahulu.")
            return None
        return self._get_row_pegawai_id(self.table.currentRow())

    def tambah_pegawai(self):
        dialog = PegawaiDialog(parent=self)
        if dialog.exec() == QDialog.Accepted:
            self.refresh(reset_filter=True, select_id=dialog.saved_pegawai_id)

    def edit_pegawai(self, row=None, col=None):
        if col == COL_CHECK:
            return
        if row is None:
            row = self.table.currentRow()
        if row < 0:
            QMessageBox.warning(self, "Peringatan", "Pilih data pegawai terlebih dahulu.")
            return
        pegawai_id = self._get_row_pegawai_id(row)
        dialog = PegawaiDialog(pegawai_id=pegawai_id, parent=self)
        if dialog.exec() == QDialog.Accepted:
            self.refresh()

    def edit_pegawai_selected(self):
        item_id = self._get_selected_id()
        if item_id:
            self.edit_pegawai(self.table.currentRow())

    def hapus_terpilih(self):
        ids = self._get_checked_ids()
        if not ids:
            item_id = self._get_selected_id()
            if not item_id:
                return
            ids = [item_id]

        conn = database.get_db_connection()
        jumlah_manajer_total = conn.execute("SELECT COUNT(*) FROM pegawai WHERE jabatan = 'Manajer'").fetchone()[0]
        manajer_terpilih = conn.execute(
            f"SELECT COUNT(*) FROM pegawai WHERE jabatan = 'Manajer' AND id IN ({','.join('?' * len(ids))})",
            ids,
        ).fetchone()[0]
        conn.close()

        if manajer_terpilih >= jumlah_manajer_total:
            QMessageBox.warning(
                self,
                "Tidak Dapat Dihapus",
                "Tidak dapat menghapus semua Manajer. Minimal satu Manajer harus tetap ada.",
            )
            return

        nama_list = []
        for r in range(self.table.rowCount()):
            w = self.table.cellWidget(r, COL_CHECK)
            if w and w.isChecked():
                nama_list.append(self.table.item(r, COL_NAMA).text())
        if not nama_list:
            nama_list = [self.table.item(self.table.currentRow(), COL_NAMA).text()]

        reply = QMessageBox.question(
            self,
            "Konfirmasi Hapus",
            f"Yakin ingin menghapus {len(ids)} pegawai berikut?\n" + "\n".join(f"- {n}" for n in nama_list),
            QMessageBox.Yes | QMessageBox.No,
        )
        if reply == QMessageBox.Yes:
            ok, err = database.hapus_banyak_pegawai(ids)
            if ok:
                self.refresh()
                QMessageBox.information(self, "Sukses", f"{len(ids)} pegawai berhasil dihapus.")
            else:
                QMessageBox.critical(self, "Error", f"Gagal menghapus: {err}")
