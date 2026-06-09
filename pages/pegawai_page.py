from PySide6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel,
                               QPushButton, QTableWidget, QTableWidgetItem,
                               QHeaderView, QMessageBox, QDialog, QCheckBox)
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor
import database
from dialogs.pegawai_dialog import PegawaiDialog

JABATAN_COLORS = {
    'Manajer': '#D1ECF1',
    'Staf':    '#F8F9FA',
}

COL_CHECK   = 0
COL_ID      = 1
COL_NAMA    = 2
COL_USER    = 3
COL_JABATAN = 4


class PegawaiPage(QWidget):
    def __init__(self, refresh_manager_callback=None):
        super().__init__()
        self.refresh_manager_callback = refresh_manager_callback
        self.init_ui()
        self.refresh()

    def init_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(25, 20, 25, 20)
        layout.setSpacing(12)

        # Header
        hdr = QHBoxLayout()
        title = QLabel("👥 Manajemen Pegawai")
        title.setObjectName("pageHeader")
        add_btn = QPushButton("＋  Tambah Pegawai")
        add_btn.setObjectName("primaryButton")
        add_btn.setCursor(Qt.PointingHandCursor)
        add_btn.clicked.connect(self.tambah_pegawai)
        hdr.addWidget(title)
        hdr.addStretch()
        hdr.addWidget(add_btn)
        layout.addLayout(hdr)

        # Tabel
        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["✓", "ID", "Nama", "Username", "Jabatan"])
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.table.setSelectionBehavior(QTableWidget.SelectRows)
        self.table.verticalHeader().setVisible(False)
        self.table.setSortingEnabled(True)
        self.table.cellDoubleClicked.connect(self.edit_pegawai)

        hv = self.table.horizontalHeader()
        hv.setSectionResizeMode(COL_CHECK,   QHeaderView.ResizeToContents)
        hv.setSectionResizeMode(COL_ID,      QHeaderView.ResizeToContents)
        hv.setSectionResizeMode(COL_NAMA,    QHeaderView.Stretch)
        hv.setSectionResizeMode(COL_USER,    QHeaderView.Stretch)
        hv.setSectionResizeMode(COL_JABATAN, QHeaderView.ResizeToContents)

        self.table.horizontalHeader().sectionClicked.connect(self._header_clicked)
        layout.addWidget(self.table)

        # Action buttons
        action_row = QHBoxLayout()
        edit_btn = QPushButton("✏️  Edit")
        edit_btn.clicked.connect(self.edit_pegawai_selected)

        self.hapus_btn = QPushButton("🗑️  Hapus Terpilih")
        self.hapus_btn.setObjectName("dangerButton")
        self.hapus_btn.clicked.connect(self.hapus_terpilih)

        action_row.addWidget(edit_btn)
        action_row.addStretch()
        action_row.addWidget(self.hapus_btn)
        layout.addLayout(action_row)

    def refresh(self):
        data = database.get_all_pegawai()
        self.table.setSortingEnabled(False)
        self.table.setRowCount(0)
        for row, d in enumerate(data):
            self.table.insertRow(row)
            bg = QColor(JABATAN_COLORS.get(d['jabatan'], '#FFFFFF'))

            chk = QCheckBox()
            chk.setStyleSheet("margin-left:6px;")
            self.table.setCellWidget(row, COL_CHECK, chk)

            items = [str(d['id']), d['nama'], d['username'], d['jabatan']]
            for col_offset, val in enumerate(items):
                item = QTableWidgetItem(val)
                item.setBackground(bg)
                self.table.setItem(row, col_offset + 1, item)
        self.table.setSortingEnabled(True)
        # Sync ke manager dashboard jika ada callback
        if self.refresh_manager_callback:
            self.refresh_manager_callback()

    def _header_clicked(self, logical_index):
        if logical_index != COL_CHECK:
            return
        any_checked = any(
            self.table.cellWidget(r, COL_CHECK).isChecked()
            for r in range(self.table.rowCount())
            if self.table.cellWidget(r, COL_CHECK)
        )
        new_state = not any_checked
        for r in range(self.table.rowCount()):
            w = self.table.cellWidget(r, COL_CHECK)
            if w:
                w.setChecked(new_state)

    def _get_checked_ids(self):
        ids = []
        for r in range(self.table.rowCount()):
            w = self.table.cellWidget(r, COL_CHECK)
            if w and w.isChecked():
                ids.append(int(self.table.item(r, COL_ID).text()))
        return ids

    def _get_selected_id(self):
        selected = self.table.selectedItems()
        if not selected:
            QMessageBox.warning(self, "Peringatan", "Pilih data pegawai terlebih dahulu.")
            return None
        return int(self.table.item(self.table.currentRow(), COL_ID).text())

    def tambah_pegawai(self):
        dialog = PegawaiDialog(parent=self)
        if dialog.exec() == QDialog.Accepted:
            self.refresh()

    def edit_pegawai(self, row=None, col=None):
        if col == COL_CHECK:
            return
        if row is None:
            row = self.table.currentRow()
        if row < 0:
            QMessageBox.warning(self, "Peringatan", "Pilih data pegawai terlebih dahulu.")
            return
        pegawai_id = int(self.table.item(row, COL_ID).text())
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

        # Cek jika ada manajer di daftar hapus
        conn = database.get_db_connection()
        jumlah_manajer_total = conn.execute(
            "SELECT COUNT(*) FROM pegawai WHERE jabatan = 'Manajer'"
        ).fetchone()[0]
        manajer_terpilih = conn.execute(
            f"SELECT COUNT(*) FROM pegawai WHERE jabatan = 'Manajer' AND id IN ({','.join('?'*len(ids))})",
            ids
        ).fetchone()[0]
        conn.close()

        if manajer_terpilih >= jumlah_manajer_total:
            QMessageBox.warning(
                self, "Tidak Dapat Dihapus",
                "Tidak dapat menghapus semua Manajer. Minimal satu Manajer harus tetap ada."
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
            self, "Konfirmasi Hapus",
            f"Yakin ingin menghapus {len(ids)} pegawai berikut?\n" + "\n".join(f"• {n}" for n in nama_list),
            QMessageBox.Yes | QMessageBox.No
        )
        if reply == QMessageBox.Yes:
            ok, err = database.hapus_banyak_pegawai(ids)
            if ok:
                self.refresh()
                QMessageBox.information(self, "Sukses", f"{len(ids)} pegawai berhasil dihapus.")
            else:
                QMessageBox.critical(self, "Error", f"Gagal menghapus: {err}")
