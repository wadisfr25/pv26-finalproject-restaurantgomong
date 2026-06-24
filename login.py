import hashlib

from PySide6.QtCore import QSettings, Qt
from PySide6.QtGui import QColor
from PySide6.QtWidgets import QGraphicsDropShadowEffect, QMessageBox, QVBoxLayout, QWidget

import database.database as database
from ui.ui_loader import load_ui


class LoginForm(QWidget):
    def __init__(self, switch_to_dashboard, switch_to_login_func):
        super().__init__()
        self.switch_to_dashboard = switch_to_dashboard
        self.settings = QSettings("RestaurantGomong", "ReservasiApp")
        self.setup_ui()
        self.load_settings()

    def setup_ui(self):
        self.ui_root = load_ui(self, "login_form.ui")
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.ui_root)

        self.ui_root.layout().setAlignment(Qt.AlignCenter)
        self.loginContainer.setFixedWidth(500)

        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(34)
        shadow.setOffset(0, 14)
        shadow.setColor(QColor(30, 45, 61, 34))
        self.loginContainer.setGraphicsEffect(shadow)

        self.login_btn = self.primaryButton
        self.remember_me = self.checkBox
        self.login_btn.clicked.connect(self.check_login)
        self.password_input.returnPressed.connect(self.check_login)

    def check_login(self):
        username = self.username_input.text().strip()
        password = self.password_input.text().strip()

        if not username or not password:
            QMessageBox.warning(self, "Login Gagal", "Username dan password tidak boleh kosong.")
            return

        conn = database.get_db_connection()
        user = conn.execute(
            "SELECT nama, password, jabatan FROM pegawai WHERE username = ?", (username,)
        ).fetchone()
        conn.close()

        if user and user["password"] == hashlib.sha256(password.encode()).hexdigest():
            if self.remember_me.isChecked():
                self.settings.setValue("last_user", username)
            else:
                self.settings.remove("last_user")
            self.switch_to_dashboard(user["nama"], user["jabatan"])
            self.password_input.clear()
        else:
            QMessageBox.critical(self, "Login Gagal", "Username atau password salah.")

    def load_settings(self):
        last_user = self.settings.value("last_user", defaultValue=None)
        if last_user:
            self.username_input.setText(last_user)
            self.remember_me.setChecked(True)
            self.password_input.setFocus()
