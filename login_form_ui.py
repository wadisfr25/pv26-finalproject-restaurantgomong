# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_form.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_LoginFormUi(object):
    def setupUi(self, LoginFormUi):
        if not LoginFormUi.objectName():
            LoginFormUi.setObjectName(u"LoginFormUi")
        self.main_layout = QVBoxLayout(LoginFormUi)
        self.main_layout.setObjectName(u"main_layout")
        self.main_layout.setContentsMargins(24, 24, 24, 24)
        self.loginContainer = QWidget(LoginFormUi)
        self.loginContainer.setObjectName(u"loginContainer")
        self.loginContainer.setMinimumWidth(500)
        self.loginContainer.setMaximumWidth(500)
        self.container_layout = QVBoxLayout(self.loginContainer)
        self.container_layout.setSpacing(13)
        self.container_layout.setObjectName(u"container_layout")
        self.container_layout.setContentsMargins(50, 44, 50, 44)
        self.badge_label = QLabel(self.loginContainer)
        self.badge_label.setObjectName(u"badge_label")
        self.badge_label.setAlignment(Qt.AlignCenter)

        self.container_layout.addWidget(self.badge_label)

        self.heading_label = QLabel(self.loginContainer)
        self.heading_label.setObjectName(u"heading_label")
        self.heading_label.setAlignment(Qt.AlignCenter)

        self.container_layout.addWidget(self.heading_label)

        self.subheading_label = QLabel(self.loginContainer)
        self.subheading_label.setObjectName(u"subheading_label")
        self.subheading_label.setAlignment(Qt.AlignCenter)

        self.container_layout.addWidget(self.subheading_label)

        self.top_spacer = QSpacerItem(20, 18, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.container_layout.addItem(self.top_spacer)

        self.username_label = QLabel(self.loginContainer)
        self.username_label.setObjectName(u"username_label")

        self.container_layout.addWidget(self.username_label)

        self.username_input = QLineEdit(self.loginContainer)
        self.username_input.setObjectName(u"username_input")

        self.container_layout.addWidget(self.username_input)

        self.password_label = QLabel(self.loginContainer)
        self.password_label.setObjectName(u"password_label")

        self.container_layout.addWidget(self.password_label)

        self.password_input = QLineEdit(self.loginContainer)
        self.password_input.setObjectName(u"password_input")
        self.password_input.setEchoMode(QLineEdit.Password)

        self.container_layout.addWidget(self.password_input)

        self.remember_me = QCheckBox(self.loginContainer)
        self.remember_me.setObjectName(u"remember_me")

        self.container_layout.addWidget(self.remember_me)

        self.button_spacer = QSpacerItem(20, 15, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.container_layout.addItem(self.button_spacer)

        self.login_btn = QPushButton(self.loginContainer)
        self.login_btn.setObjectName(u"login_btn")
        self.login_btn.setMinimumHeight(42)
        self.login_btn.setMaximumHeight(42)

        self.container_layout.addWidget(self.login_btn)

        self.hint_label = QLabel(self.loginContainer)
        self.hint_label.setObjectName(u"hint_label")
        self.hint_label.setAlignment(Qt.AlignCenter)

        self.container_layout.addWidget(self.hint_label)


        self.main_layout.addWidget(self.loginContainer, 0, Qt.AlignCenter)


        self.retranslateUi(LoginFormUi)

        QMetaObject.connectSlotsByName(LoginFormUi)
    # setupUi

    def retranslateUi(self, LoginFormUi):
        LoginFormUi.setObjectName(QCoreApplication.translate("LoginFormUi", u"loginPage", None))
        self.badge_label.setText(QCoreApplication.translate("LoginFormUi", u"ADMIN ACCESS", None))
        self.badge_label.setObjectName(QCoreApplication.translate("LoginFormUi", u"loginBadge", None))
        self.heading_label.setText(QCoreApplication.translate("LoginFormUi", u"Restaurant Gomong", None))
        self.heading_label.setObjectName(QCoreApplication.translate("LoginFormUi", u"loginHeading", None))
        self.subheading_label.setText(QCoreApplication.translate("LoginFormUi", u"Dashboard Reservasi & Manajemen Restoran", None))
        self.subheading_label.setObjectName(QCoreApplication.translate("LoginFormUi", u"loginSubHeading", None))
        self.username_label.setText(QCoreApplication.translate("LoginFormUi", u"Username", None))
        self.username_label.setObjectName(QCoreApplication.translate("LoginFormUi", u"formTitle", None))
        self.username_input.setPlaceholderText(QCoreApplication.translate("LoginFormUi", u"Masukkan username", None))
        self.password_label.setText(QCoreApplication.translate("LoginFormUi", u"Password", None))
        self.password_label.setObjectName(QCoreApplication.translate("LoginFormUi", u"formTitle", None))
        self.password_input.setPlaceholderText(QCoreApplication.translate("LoginFormUi", u"Masukkan password", None))
        self.remember_me.setText(QCoreApplication.translate("LoginFormUi", u"Ingat Saya", None))
        self.remember_me.setObjectName(QCoreApplication.translate("LoginFormUi", u"checkBox", None))
        self.login_btn.setText(QCoreApplication.translate("LoginFormUi", u"Masuk Admin", None))
        self.login_btn.setObjectName(QCoreApplication.translate("LoginFormUi", u"primaryButton", None))
        self.hint_label.setText(QCoreApplication.translate("LoginFormUi", u"Demo: admin / admin123", None))
        self.hint_label.setObjectName(QCoreApplication.translate("LoginFormUi", u"loginHint", None))
    # retranslateUi

