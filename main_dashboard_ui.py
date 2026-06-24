# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_dashboard.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QVBoxLayout, QWidget)

class Ui_MainDashboardUi(object):
    def setupUi(self, MainDashboardUi):
        if not MainDashboardUi.objectName():
            MainDashboardUi.setObjectName(u"MainDashboardUi")
        self.root_layout = QHBoxLayout(MainDashboardUi)
        self.root_layout.setSpacing(0)
        self.root_layout.setObjectName(u"root_layout")
        self.root_layout.setContentsMargins(0, 0, 0, 0)
        self.sidebar = QFrame(MainDashboardUi)
        self.sidebar.setObjectName(u"sidebar")
        self.sidebar.setMinimumWidth(230)
        self.sidebar.setMaximumWidth(230)
        self.sidebar.setFrameShape(QFrame.NoFrame)
        self.sidebar_layout = QVBoxLayout(self.sidebar)
        self.sidebar_layout.setSpacing(0)
        self.sidebar_layout.setObjectName(u"sidebar_layout")
        self.sidebar_layout.setContentsMargins(0, 0, 0, 0)
        self.sidebarHeader = QWidget(self.sidebar)
        self.sidebarHeader.setObjectName(u"sidebarHeader")
        self.header_layout = QVBoxLayout(self.sidebarHeader)
        self.header_layout.setObjectName(u"header_layout")
        self.header_layout.setContentsMargins(15, 25, 15, 20)
        self.sidebar_title = QLabel(self.sidebarHeader)
        self.sidebar_title.setObjectName(u"sidebar_title")
        self.sidebar_title.setAlignment(Qt.AlignCenter)

        self.header_layout.addWidget(self.sidebar_title)

        self.sidebar_subtitle = QLabel(self.sidebarHeader)
        self.sidebar_subtitle.setObjectName(u"sidebar_subtitle")
        self.sidebar_subtitle.setAlignment(Qt.AlignCenter)

        self.header_layout.addWidget(self.sidebar_subtitle)


        self.sidebar_layout.addWidget(self.sidebarHeader)

        self.nav_container = QWidget(self.sidebar)
        self.nav_container.setObjectName(u"nav_container")
        self.nav_layout = QVBoxLayout(self.nav_container)
        self.nav_layout.setSpacing(0)
        self.nav_layout.setObjectName(u"nav_layout")
        self.nav_layout.setContentsMargins(0, 0, 0, 0)

        self.sidebar_layout.addWidget(self.nav_container)

        self.sidebar_spacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.sidebar_layout.addItem(self.sidebar_spacer)

        self.role_badge = QLabel(self.sidebar)
        self.role_badge.setObjectName(u"role_badge")
        self.role_badge.setAlignment(Qt.AlignCenter)

        self.sidebar_layout.addWidget(self.role_badge)

        self.sidebarFooter = QWidget(self.sidebar)
        self.sidebarFooter.setObjectName(u"sidebarFooter")
        self.footer_layout = QVBoxLayout(self.sidebarFooter)
        self.footer_layout.setSpacing(8)
        self.footer_layout.setObjectName(u"footer_layout")
        self.footer_layout.setContentsMargins(15, 15, 15, 15)
        self.user_label = QLabel(self.sidebarFooter)
        self.user_label.setObjectName(u"user_label")
        self.user_label.setAlignment(Qt.AlignCenter)
        self.user_label.setWordWrap(True)

        self.footer_layout.addWidget(self.user_label)

        self.logout_btn = QPushButton(self.sidebarFooter)
        self.logout_btn.setObjectName(u"logout_btn")

        self.footer_layout.addWidget(self.logout_btn)


        self.sidebar_layout.addWidget(self.sidebarFooter)


        self.root_layout.addWidget(self.sidebar)

        self.content_stack = QStackedWidget(MainDashboardUi)
        self.content_stack.setObjectName(u"content_stack")

        self.root_layout.addWidget(self.content_stack)


        self.retranslateUi(MainDashboardUi)

        QMetaObject.connectSlotsByName(MainDashboardUi)
    # setupUi

    def retranslateUi(self, MainDashboardUi):
        self.sidebar_title.setText(QCoreApplication.translate("MainDashboardUi", u"Gomong", None))
        self.sidebar_title.setObjectName(QCoreApplication.translate("MainDashboardUi", u"sidebarTitle", None))
        self.sidebar_subtitle.setText(QCoreApplication.translate("MainDashboardUi", u"Restaurant & Reservasi", None))
        self.sidebar_subtitle.setObjectName(QCoreApplication.translate("MainDashboardUi", u"sidebarSubtitle", None))
        self.role_badge.setObjectName(QCoreApplication.translate("MainDashboardUi", u"sidebarRole", None))
        self.user_label.setObjectName(QCoreApplication.translate("MainDashboardUi", u"sidebarUser", None))
        self.logout_btn.setText(QCoreApplication.translate("MainDashboardUi", u"Logout", None))
        self.logout_btn.setObjectName(QCoreApplication.translate("MainDashboardUi", u"logoutButton", None))
        pass
    # retranslateUi

