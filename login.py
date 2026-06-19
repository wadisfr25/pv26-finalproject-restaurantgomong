import hashlib
from PySide6.QtWidgets import (QWidget, QLabel, QLineEdit, QPushButton,
                               QVBoxLayout, QMessageBox, QCheckBox,
                               QGraphicsDropShadowEffect)
from PySide6.QtCore import Qt, QSettings
from PySide6.QtGui import QColor
import database.database as database


class LoginForm(QWidget):
    def __init__(self, switch_to_dashboard, switch_to_login_func):
        super().__init__()
        self.switch_to_dashboard = switch_to_dashboard
        self.settings = QSettings("RestaurantGomong", "ReservasiApp")
        self.setup_ui()
        self.load_settings()

    def setup_ui(self):
        self.setObjectName("loginPage")

        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignCenter)
        main_layout.setContentsMargins(24, 24, 24, 24)

        container = QWidget()
        container.setObjectName("loginContainer")
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(34)
        shadow.setOffset(0, 14)
        shadow.setColor(QColor(30, 45, 61, 34))
        container.setGraphicsEffect(shadow)

        container_layout = QVBoxLayout()
        container_layout.setContentsMargins(50, 44, 50, 44)
        container_layout.setSpacing(13)
        container_layout.setAlignment(Qt.AlignCenter)
        container.setLayout(container_layout)
        container.setFixedWidth(500)

        badge = QLabel("ADMIN ACCESS")
        badge.setAlignment(Qt.AlignCenter)
        badge.setObjectName("loginBadge")

        heading = QLabel("🍽️ Restaurant Gomong")
        heading.setText("Restaurant Gomong")
        heading.setAlignment(Qt.AlignCenter)
        heading.setObjectName("loginHeading")

        subheading = QLabel("Sistem Reservasi Meja — Silakan Login")
        subheading.setText("Dashboard Reservasi & Manajemen Restoran")
        subheading.setAlignment(Qt.AlignCenter)
        subheading.setObjectName("loginSubHeading")

        username_label = QLabel("Username")
        username_label.setObjectName("formTitle")
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Masukkan username")

        password_label = QLabel("Password")
        password_label.setObjectName("formTitle")
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Masukkan password")
        self.password_input.setEchoMode(QLineEdit.Password)

        self.remember_me = QCheckBox("Ingat Saya")
        self.remember_me.setObjectName("checkBox")

        login_btn = QPushButton("Masuk Admin")
        login_btn.setObjectName("primaryButton")
        login_btn.setFixedHeight(42)
        login_btn.clicked.connect(self.check_login)
        self.password_input.returnPressed.connect(self.check_login)

        hint = QLabel("Demo: admin / admin123")
        hint.setAlignment(Qt.AlignCenter)
        hint.setObjectName("loginHint")

        form_layout = QVBoxLayout()
        form_layout.setSpacing(11)
        form_layout.addWidget(username_label)
        form_layout.addWidget(self.username_input)
        form_layout.addWidget(password_label)
        form_layout.addWidget(self.password_input)
        form_layout.addWidget(self.remember_me)
        form_layout.addSpacing(15)
        form_layout.addWidget(login_btn)
        form_layout.addWidget(hint)

        container_layout.addWidget(badge)
        container_layout.addWidget(heading)
        container_layout.addWidget(subheading)
        container_layout.addSpacing(18)
        container_layout.addLayout(form_layout)

        main_layout.addWidget(container)
        self.setLayout(main_layout)

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

        if user and user['password'] == hashlib.sha256(password.encode()).hexdigest():
            if self.remember_me.isChecked():
                self.settings.setValue("last_user", username)
            else:
                self.settings.remove("last_user")
            self.switch_to_dashboard(user['nama'], user['jabatan'])
            self.password_input.clear()
        else:
            QMessageBox.critical(self, "Login Gagal", "Username atau password salah.")

    def load_settings(self):
        last_user = self.settings.value("last_user", defaultValue=None)
        if last_user:
            self.username_input.setText(last_user)
            self.remember_me.setChecked(True)
            self.password_input.setFocus()
