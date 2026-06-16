from PySide6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel,
                               QPushButton, QStackedWidget, QFrame)
from PySide6.QtCore import Qt

from pages.dashboard_page import DashboardPage
from pages.manager_dashboard_page import ManagerDashboardPage
from pages.reservasi_page import ReservasiPage
from pages.meja_page import MejaPage
from pages.laporan_page import LaporanPage
from pages.pegawai_page import PegawaiPage


class SidebarButton(QPushButton):
    def __init__(self, icon, text, parent=None):
        super().__init__(f"  {icon}  {text}", parent)
        self.setObjectName("sidebarButton")
        self.setCheckable(True)
        self.setFixedHeight(52)
        self.setCursor(Qt.PointingHandCursor)


class MainDashboard(QWidget):
    def __init__(self, nama_pegawai, jabatan, logout_callback):
        super().__init__()
        self.nama_pegawai    = nama_pegawai
        self.jabatan         = jabatan
        self.logout_callback = logout_callback
        self.is_manager      = (jabatan == 'Manajer')
        self.init_ui()

    def init_ui(self):
        root = QHBoxLayout(self)
        root.setContentsMargins(0, 0, 0, 0)
        root.setSpacing(0)

        root.addWidget(self._build_sidebar())

        self.content_stack = QStackedWidget()

        if self.is_manager:
            self._init_manager_pages()
        else:
            self._init_pegawai_pages()

        root.addWidget(self.content_stack)
        self.nav_btns[0].setChecked(True)

    def _init_pegawai_pages(self):
        self.page_dash      = DashboardPage(self.nama_pegawai)
        self.page_reservasi = ReservasiPage(self.nama_pegawai, self._refresh_all)
        self.page_meja      = MejaPage()
        for page in [self.page_dash, self.page_reservasi, self.page_meja]:
            self.content_stack.addWidget(page)

    def _init_manager_pages(self):
        self.page_dash      = ManagerDashboardPage(self.nama_pegawai)
        self.page_reservasi = ReservasiPage(self.nama_pegawai, self._refresh_all)
        self.page_meja      = MejaPage()
        self.page_laporan   = LaporanPage()
        self.page_pegawai   = PegawaiPage(refresh_manager_callback=self.page_dash.refresh)
        for page in [self.page_dash, self.page_reservasi, self.page_meja,
                     self.page_laporan, self.page_pegawai]:
            self.content_stack.addWidget(page)

    def _build_sidebar(self):
        sidebar = QFrame()
        sidebar.setObjectName("sidebar")
        sidebar.setFixedWidth(230)

        layout = QVBoxLayout(sidebar)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        header = QWidget()
        header.setObjectName("sidebarHeader")
        h_layout = QVBoxLayout(header)
        h_layout.setContentsMargins(15, 25, 15, 20)

        title = QLabel("🍽️ Gomong")
        title.setObjectName("sidebarTitle")
        title.setAlignment(Qt.AlignCenter)

        subtitle = QLabel("Restaurant & Reservasi")
        subtitle.setObjectName("sidebarSubtitle")
        subtitle.setAlignment(Qt.AlignCenter)

        h_layout.addWidget(title)
        h_layout.addWidget(subtitle)
        layout.addWidget(header)

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
            layout.addWidget(btn)

        layout.addStretch()

        role_badge = QLabel(f"🔑  {self.jabatan}")
        role_badge.setAlignment(Qt.AlignCenter)
        role_badge.setStyleSheet(
            "color: #F39C12; font-size: 11px; font-weight: bold; padding: 4px;"
        )
        layout.addWidget(role_badge)

        footer = QWidget()
        footer.setObjectName("sidebarFooter")
        f_layout = QVBoxLayout(footer)
        f_layout.setContentsMargins(15, 15, 15, 15)
        f_layout.setSpacing(8)

        user_label = QLabel(f"👤  {self.nama_pegawai}")
        user_label.setObjectName("sidebarUser")
        user_label.setAlignment(Qt.AlignCenter)
        user_label.setWordWrap(True)

        logout_btn = QPushButton("🚪  Logout")
        logout_btn.setObjectName("logoutButton")
        logout_btn.setCursor(Qt.PointingHandCursor)
        logout_btn.clicked.connect(self.logout_callback)

        f_layout.addWidget(user_label)
        f_layout.addWidget(logout_btn)
        layout.addWidget(footer)

        return sidebar

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
