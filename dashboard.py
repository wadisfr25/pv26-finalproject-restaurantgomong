from PySide6.QtCore import Qt
from PySide6.QtWidgets import QPushButton, QVBoxLayout, QWidget

from pages.dashboard_page import DashboardPage
from pages.laporan_page import LaporanPage
from pages.manager_dashboard_page import ManagerDashboardPage
from pages.meja_page import MejaPage
from pages.pegawai_page import PegawaiPage
from pages.reservasi_page import ReservasiPage
from ui.ui_loader import load_ui


class SidebarButton(QPushButton):
    def __init__(self, icon, text, parent=None):
        label = f"{icon}  {text}".strip()
        super().__init__(label, parent)
        self.setObjectName("sidebarButton")
        self.setCheckable(True)
        self.setFixedHeight(52)
        self.setCursor(Qt.PointingHandCursor)


class MainDashboard(QWidget):
    def __init__(self, nama_pegawai, jabatan, logout_callback):
        super().__init__()
        self.nama_pegawai = nama_pegawai
        self.jabatan = jabatan
        self.logout_callback = logout_callback
        self.is_manager = jabatan == "Manajer"
        self.init_ui()

    def init_ui(self):
        self.ui_root = load_ui(self, "main_dashboard.ui")
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.ui_root)

        self.role_badge = self.sidebarRole
        self.user_label = self.sidebarUser
        self.logout_btn = self.logoutButton
        self.sidebarTitle.setText("🍽️ Gomong")
        self.role_badge.setText(f"🔑  {self.jabatan}")
        self.user_label.setText(f"👤  {self.nama_pegawai}")
        self.logout_btn.setText("🚪  Logout")
        self.logout_btn.setCursor(Qt.PointingHandCursor)
        self.logout_btn.clicked.connect(self.logout_callback)
        self._apply_sidebar_theme()

        self._build_sidebar()
        if self.is_manager:
            self._init_manager_pages()
        else:
            self._init_pegawai_pages()
        self.nav_btns[0].setChecked(True)

    def _init_pegawai_pages(self):
        self.page_dash = DashboardPage(self.nama_pegawai)
        self.page_reservasi = ReservasiPage(self.nama_pegawai, self._refresh_all)
        self.page_meja = MejaPage()
        for page in [self.page_dash, self.page_reservasi, self.page_meja]:
            self.content_stack.addWidget(page)

    def _init_manager_pages(self):
        self.page_dash = ManagerDashboardPage(self.nama_pegawai)
        self.page_reservasi = ReservasiPage(self.nama_pegawai, self._refresh_all)
        self.page_meja = MejaPage()
        self.page_laporan = LaporanPage()
        self.page_pegawai = PegawaiPage(refresh_manager_callback=self.page_dash.refresh)
        for page in [
            self.page_dash,
            self.page_reservasi,
            self.page_meja,
            self.page_laporan,
            self.page_pegawai,
        ]:
            self.content_stack.addWidget(page)

    def _build_sidebar(self):
        if self.is_manager:
            nav_items = [
                ("🏠", "Dashboard"),
                ("📋", "Reservasi"),
                ("🪑", "Manajemen Meja"),
                ("📊", "Laporan & Statistik"),
                ("👥", "Manajemen Pegawai"),
            ]
        else:
            nav_items = [
                ("🏠", "Dashboard"),
                ("📋", "Reservasi"),
                ("🪑", "Manajemen Meja"),
            ]

        self.nav_btns = []
        for i, (icon, label) in enumerate(nav_items):
            btn = SidebarButton(icon, label)
            btn.clicked.connect(lambda _, idx=i: self._switch_page(idx))
            self.nav_btns.append(btn)
            self.nav_layout.addWidget(btn)

    def _apply_sidebar_theme(self):
        self.sidebar.setStyleSheet("""
            QFrame#sidebar {
                background: #1F2937;
                border-right: 1px solid #111827;
            }
            QWidget#sidebarHeader {
                background: #172033;
                border-bottom: 1px solid #374151;
            }
            QWidget#nav_container {
                background: #1F2937;
            }
            QLabel#sidebarTitle {
                background: transparent;
                font-size: 24px;
                font-weight: 800;
                color: #FF6B6B;
                letter-spacing: 0px;
                padding-top: 2px;
            }
            QLabel#sidebarSubtitle {
                background: transparent;
                font-size: 11px;
                color: #CBD5E1;
                letter-spacing: 0.3px;
                padding-top: 2px;
            }
            QWidget#sidebarFooter {
                background: #1F2937;
                border-top: 1px solid #374151;
            }
            QLabel#sidebarUser {
                background: transparent;
                color: #A0AEC0;
                font-size: 12px;
            }
            QLabel#sidebarRole {
                background: transparent;
                color: #FBBF24;
                font-size: 11px;
                font-weight: 700;
                padding: 4px;
            }
            QPushButton#sidebarButton {
                text-align: left;
                color: #8896B0;
                background: transparent;
                border: none;
                border-left: 3px solid transparent;
                padding: 0 20px;
                font-size: 13px;
                font-weight: 500;
            }
            QPushButton#sidebarButton:hover {
                background: #2F3B4C;
                color: #E2E8F0;
                border-left: 3px solid #FF6B6B;
            }
            QPushButton#sidebarButton:checked {
                background: #374151;
                color: #FF6B6B;
                font-weight: 700;
                border-left: 3px solid #FF6B6B;
            }
            QPushButton#logoutButton {
                background: transparent;
                color: #FF6B6B;
                border: 1px solid #FF6B6B;
                border-radius: 8px;
                padding: 8px;
                font-weight: 600;
                font-size: 12px;
            }
            QPushButton#logoutButton:hover {
                background: #E74C3C;
                color: white;
                border-color: #E74C3C;
            }
        """)

    def _switch_page(self, index):
        for i, btn in enumerate(self.nav_btns):
            btn.setChecked(i == index)
        self.content_stack.setCurrentIndex(index)
        if index == 0:
            self.page_dash.refresh()
        elif index == 2:
            self.page_meja.refresh()
        elif self.is_manager and index == 3:
            self.page_laporan.refresh()
        elif self.is_manager and index == 4:
            self.page_pegawai.refresh()

    def _refresh_all(self):
        self.page_dash.refresh()
        self.page_meja.refresh()
