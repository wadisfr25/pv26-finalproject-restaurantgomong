from PySide6.QtWidgets import QDialog, QMessageBox

import database.database as database
from ui.ui_meja_dialog import Ui_MejaDialog


class MejaDialog(QDialog, Ui_MejaDialog):
    def __init__(self, meja_id=None, parent=None):
        super().__init__(parent)
        self.meja_id = meja_id
        self.is_edit = meja_id is not None
        self.init_ui()
        if self.is_edit:
            self.load_data()

    def init_ui(self):
        self.setupUi(self)
        self.setWindowTitle("Edit Meja" if self.is_edit else "Tambah Meja")
        self.setMinimumWidth(430)
        self.jenis_combo.addItems(["Kecil", "Besar", "VIP", "Outdoor", "Window Seat", "Family", "Private Room"])
        self.status_combo.addItems(["Tersedia", "Terisi", "Dibereskan", "Maintenance"])
        self.save_btn.setObjectName("primaryButton")

        self.cancel_btn.clicked.connect(self.reject)
        self.save_btn.clicked.connect(self.save)
        self.kapasitas_input.valueChanged.connect(self._update_jenis_default)

    def _update_jenis_default(self):
        if not self.is_edit:
            self.jenis_combo.setCurrentText("Besar" if self.kapasitas_input.value() > 4 else "Kecil")

    def load_data(self):
        data = database.get_meja_by_id(self.meja_id)
        if not data:
            return
        self.nomor_input.setText(data["nomor_meja"])
        self.kapasitas_input.setValue(data["kapasitas"])
        self.lantai_input.setValue(data["lantai"])
        self.jenis_combo.setCurrentText(data["jenis"])
        self.status_combo.setCurrentText(data["status"])

    def save(self):
        nomor = self.nomor_input.text().strip().upper()
        kapasitas = self.kapasitas_input.value()
        lantai = self.lantai_input.value()
        jenis = self.jenis_combo.currentText()
        status = self.status_combo.currentText()

        if not nomor:
            QMessageBox.warning(self, "Validasi", "Nomor meja tidak boleh kosong.")
            self.nomor_input.setFocus()
            return
        if len(nomor) < 2:
            QMessageBox.warning(self, "Validasi", "Nomor meja minimal 2 karakter.")
            self.nomor_input.setFocus()
            return
        if kapasitas < 1:
            QMessageBox.warning(self, "Validasi", "Kapasitas meja harus lebih dari 0.")
            return

        if self.is_edit:
            ok, err = database.edit_meja(self.meja_id, nomor, kapasitas, lantai, jenis, status)
        else:
            ok, err = database.tambah_meja(nomor, kapasitas, lantai, jenis, status)

        if ok:
            QMessageBox.information(self, "Sukses", "Data meja berhasil disimpan.")
            self.accept()
        else:
            if "UNIQUE" in str(err):
                QMessageBox.critical(self, "Error", "Nomor meja sudah digunakan.")
            else:
                QMessageBox.critical(self, "Error", f"Gagal menyimpan: {err}")
