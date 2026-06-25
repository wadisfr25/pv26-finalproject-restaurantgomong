from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog, QMessageBox

import database.database as database
from ui.ui_pegawai_dialog import Ui_PegawaiDialog


class PegawaiDialog(QDialog, Ui_PegawaiDialog):
    def __init__(self, pegawai_id=None, parent=None):
        super().__init__(parent)
        self.pegawai_id = pegawai_id
        self.is_edit = pegawai_id is not None
        self.saved_pegawai_id = pegawai_id
        self.init_ui()
        if self.is_edit:
            self.load_data()

    def init_ui(self):
        self.setupUi(self)
        self.setWindowTitle("Edit Pegawai" if self.is_edit else "Tambah Pegawai Baru")
        self.setMinimumWidth(480)
        self.jabatan_combo.addItems(["Staf", "Manajer"])
        self.save_btn.setObjectName("primaryButton")

        self.cancel_btn.clicked.connect(self.reject)
        self.save_btn.clicked.connect(self.save)
        self.reset_pwd_check.stateChanged.connect(self._toggle_password_fields)

        if self.is_edit:
            self.password_input.setEnabled(False)
            self.konfirmasi_input.setEnabled(False)
        else:
            self.reset_pwd_check.hide()

    def _toggle_password_fields(self, state):
        enabled = state == Qt.Checked
        self.password_input.setEnabled(enabled)
        self.konfirmasi_input.setEnabled(enabled)
        if not enabled:
            self.password_input.clear()
            self.konfirmasi_input.clear()

    def load_data(self):
        data = database.get_pegawai_by_id(self.pegawai_id)
        if not data:
            return
        self.nama_input.setText(data["nama"])
        self.username_input.setText(data["username"])
        self.jabatan_combo.setCurrentText(data["jabatan"])

    def save(self):
        nama = self.nama_input.text().strip()
        username = self.username_input.text().strip()
        jabatan = self.jabatan_combo.currentText()

        if not nama or len(nama) < 2:
            QMessageBox.warning(self, "Validasi", "Nama pegawai minimal 2 karakter.")
            self.nama_input.setFocus()
            return

        if not username or len(username) < 3:
            QMessageBox.warning(self, "Validasi", "Username minimal 3 karakter.")
            self.username_input.setFocus()
            return

        password_plain = None

        if self.is_edit:
            if self.reset_pwd_check.isChecked():
                password_plain = self.password_input.text()
                konfirmasi = self.konfirmasi_input.text()
                if not password_plain or len(password_plain) < 6:
                    QMessageBox.warning(self, "Validasi", "Password minimal 6 karakter.")
                    self.password_input.setFocus()
                    return
                if password_plain != konfirmasi:
                    QMessageBox.warning(self, "Validasi", "Konfirmasi password tidak cocok.")
                    self.konfirmasi_input.setFocus()
                    return
            ok, err = database.edit_pegawai(self.pegawai_id, nama, username, jabatan, password_plain)
        else:
            password_plain = self.password_input.text()
            konfirmasi = self.konfirmasi_input.text()
            if not password_plain or len(password_plain) < 6:
                QMessageBox.warning(self, "Validasi", "Password minimal 6 karakter.")
                self.password_input.setFocus()
                return
            if password_plain != konfirmasi:
                QMessageBox.warning(self, "Validasi", "Konfirmasi password tidak cocok.")
                self.konfirmasi_input.setFocus()
                return
            ok, err = database.tambah_pegawai(nama, username, password_plain, jabatan)
            if ok:
                self.saved_pegawai_id = err

        if ok:
            QMessageBox.information(self, "Sukses", "Data pegawai berhasil disimpan!")
            self.accept()
        else:
            if "UNIQUE" in str(err):
                QMessageBox.critical(self, "Error", "Username sudah digunakan. Pilih username lain.")
            else:
                QMessageBox.critical(self, "Error", f"Gagal menyimpan: {err}")
