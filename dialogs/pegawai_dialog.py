from PySide6.QtWidgets import (QDialog, QVBoxLayout, QHBoxLayout, QFormLayout,
                               QLabel, QLineEdit, QComboBox, QPushButton,
                               QMessageBox, QGroupBox, QCheckBox)
from PySide6.QtCore import Qt
import database


class PegawaiDialog(QDialog):
    def __init__(self, pegawai_id=None, parent=None):
        super().__init__(parent)
        self.pegawai_id = pegawai_id
        self.is_edit = pegawai_id is not None
        self.setWindowTitle("Edit Pegawai" if self.is_edit else "Tambah Pegawai Baru")
        self.setMinimumWidth(480)
        self.init_ui()
        if self.is_edit:
            self.load_data()

    def init_ui(self):
        layout = QVBoxLayout(self)
        layout.setSpacing(15)

        # ── Informasi Pegawai ────────────────────────────────────────
        info_grp = QGroupBox("👤  Informasi Pegawai")
        info_lay = QFormLayout(info_grp)
        info_lay.setVerticalSpacing(12)

        self.nama_input = QLineEdit()
        self.nama_input.setPlaceholderText("Nama lengkap pegawai")
        self.nama_input.setMaxLength(100)

        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Username untuk login")
        self.username_input.setMaxLength(50)

        self.jabatan_combo = QComboBox()
        self.jabatan_combo.addItems(["Staf", "Manajer"])

        info_lay.addRow("Nama *", self.nama_input)
        info_lay.addRow("Username *", self.username_input)
        info_lay.addRow("Jabatan *", self.jabatan_combo)

        # ── Password ─────────────────────────────────────────────────
        pwd_grp = QGroupBox("🔒  Password")
        pwd_lay = QFormLayout(pwd_grp)
        pwd_lay.setVerticalSpacing(12)

        if self.is_edit:
            self.reset_pwd_check = QCheckBox("Reset / Ubah Password")
            self.reset_pwd_check.stateChanged.connect(self._toggle_password_fields)
            pwd_lay.addRow("", self.reset_pwd_check)

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Password baru")
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setMaxLength(100)

        self.konfirmasi_input = QLineEdit()
        self.konfirmasi_input.setPlaceholderText("Ulangi password")
        self.konfirmasi_input.setEchoMode(QLineEdit.Password)
        self.konfirmasi_input.setMaxLength(100)

        pwd_lay.addRow("Password *", self.password_input)
        pwd_lay.addRow("Konfirmasi *", self.konfirmasi_input)

        if self.is_edit:
            # Saat edit, field password awalnya nonaktif
            self.password_input.setEnabled(False)
            self.konfirmasi_input.setEnabled(False)

        # ── Tombol ───────────────────────────────────────────────────
        btn_row = QHBoxLayout()
        cancel_btn = QPushButton("Batal")
        cancel_btn.clicked.connect(self.reject)

        save_btn = QPushButton("💾  Simpan")
        save_btn.setObjectName("primaryButton")
        save_btn.clicked.connect(self.save)

        btn_row.addStretch()
        btn_row.addWidget(cancel_btn)
        btn_row.addWidget(save_btn)

        layout.addWidget(info_grp)
        layout.addWidget(pwd_grp)
        layout.addLayout(btn_row)

    def _toggle_password_fields(self, state):
        enabled = (state == Qt.Checked)
        self.password_input.setEnabled(enabled)
        self.konfirmasi_input.setEnabled(enabled)
        if not enabled:
            self.password_input.clear()
            self.konfirmasi_input.clear()

    def load_data(self):
        data = database.get_pegawai_by_id(self.pegawai_id)
        if not data:
            return
        self.nama_input.setText(data['nama'])
        self.username_input.setText(data['username'])
        self.jabatan_combo.setCurrentText(data['jabatan'])

    def save(self):
        nama = self.nama_input.text().strip()
        username = self.username_input.text().strip()
        jabatan = self.jabatan_combo.currentText()

        # Validasi nama
        if not nama or len(nama) < 2:
            QMessageBox.warning(self, "Validasi", "Nama pegawai minimal 2 karakter.")
            self.nama_input.setFocus()
            return

        # Validasi username
        if not username or len(username) < 3:
            QMessageBox.warning(self, "Validasi", "Username minimal 3 karakter.")
            self.username_input.setFocus()
            return

        password_plain = None

        if self.is_edit:
            # Cek apakah mau reset password
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
            # Tambah baru — password wajib
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
            QMessageBox.information(self, "Sukses", "✅  Data pegawai berhasil disimpan!")
            self.accept()
        else:
            if "UNIQUE" in str(err):
                QMessageBox.critical(self, "Error", "Username sudah digunakan. Pilih username lain.")
            else:
                QMessageBox.critical(self, "Error", f"Gagal menyimpan: {err}")
