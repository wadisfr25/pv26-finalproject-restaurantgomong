import sys
from PySide6.QtGui import QIcon, QAction
from PySide6.QtWidgets import (QApplication, QMainWindow, QStackedWidget,
                               QStatusBar, QLabel, QMessageBox)
from PySide6.QtCore import QSettings, Qt

from login import LoginForm
from dashboard import MainDashboard
import database.database as database


class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        database.init_database()

        self.setWindowTitle("Restaurant Gomong — Sistem Reservasi")
        self.settings = QSettings("RestaurantGomong", "ReservasiApp")

        self._create_menu_bar()
        self._create_status_bar()
        self._load_stylesheet()

        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        self.dashboard = None
        self.login_form = LoginForm(self.show_dashboard, self.switch_to_login)
        self.stacked_widget.addWidget(self.login_form)

        self.resizeAndCenter(0.4, 0.6)
        self.try_auto_login()

    def _create_menu_bar(self):
        menu_bar = self.menuBar()

        file_menu = menu_bar.addMenu("&File")

        self.logout_action = QAction("Logout", self)
        self.logout_action.triggered.connect(self.logout)
        self.logout_action.setEnabled(False)
        file_menu.addAction(self.logout_action)

        file_menu.addSeparator()

        exit_action = QAction("&Exit", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        help_menu = menu_bar.addMenu("&Help")
        about_action = QAction("About", self)
        about_action.triggered.connect(self.show_about)
        help_menu.addAction(about_action)

    def _create_status_bar(self):
        status_bar = QStatusBar()
        self.setStatusBar(status_bar)
        # Isi dengan nama & NIM anggota kelompok (tidak dapat diedit)
        label = QLabel(
            "🍽️ Restaurant Gomong |  Wadis Friendly (F1D02310094)  |  Lalu Farras Hanif Aslam (F1D02410118)  |  Muh. Rizky Destiawansyah (F1D02410146)"
        )
        label.setStyleSheet("color: #777; font-size: 11px;")
        status_bar.addPermanentWidget(label)
        status_bar.showMessage("Aplikasi Siap.")

    def _load_stylesheet(self):
        try:
            with open("assets/style.qss", "r", encoding="utf-8") as f:
                self.setStyleSheet(f.read())
        except FileNotFoundError:
            print("style.qss tidak ditemukan, tampilan default digunakan.")
        except UnicodeDecodeError:
            print("style.qss gagal dibaca sebagai UTF-8, tampilan default digunakan.")

    def resizeAndCenter(self, width_ratio=0.6, height_ratio=0.6):
        screen = self.screen().availableGeometry()
        w = int(screen.width() * width_ratio)
        h = int(screen.height() * height_ratio)
        self.resize(w, h)
        self.move((screen.width() - w) // 2, (screen.height() - h) // 2)

    def show_dashboard(self, nama_pegawai, jabatan):
        if self.dashboard is not None:
            self.stacked_widget.removeWidget(self.dashboard)
            self.dashboard.deleteLater()

        self.dashboard = MainDashboard(nama_pegawai, jabatan, self.switch_to_login)
        self.stacked_widget.addWidget(self.dashboard)
        self.stacked_widget.setCurrentWidget(self.dashboard)
        self.resizeAndCenter(0.88, 0.92)
        self.setWindowTitle(f"Restaurant Gomong — {nama_pegawai}")
        self.logout_action.setEnabled(True)

    def switch_to_login(self):
        self.logout_action.setEnabled(False)
        self.statusBar().showMessage("Silakan login untuk memulai.")
        self.stacked_widget.setCurrentWidget(self.login_form)
        self.setWindowTitle("Restaurant Gomong — Login")
        self.resizeAndCenter(0.4, 0.6)

    def logout(self):
        self.settings.remove("last_user")
        self.switch_to_login()

    def try_auto_login(self):
        last_user = self.settings.value("last_user", defaultValue=None)
        if last_user:
            conn = database.get_db_connection()
            user = conn.execute(
                "SELECT nama, jabatan FROM pegawai WHERE username = ?", (last_user,)
            ).fetchone()
            conn.close()
            if user:
                self.show_dashboard(user['nama'], user['jabatan'])

    def show_about(self):
        QMessageBox.about(
            self, "Tentang Aplikasi",
            "<h3>🍽️ Restaurant Gomong</h3>"
            "<p>Sistem Reservasi Meja Restaurant</p>"
            "<p>Lantai 1: Meja Kecil (≤ 4 orang)<br>"
            "Lantai 2: Meja Besar (5–8 orang)</p>"
            "<p>Dikembangkan dengan <b>PySide6</b> & <b>SQLite</b></p>"
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec())
