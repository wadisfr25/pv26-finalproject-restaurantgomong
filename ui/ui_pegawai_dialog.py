# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pegawai_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDialog,
    QFormLayout, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_PegawaiDialog(object):
    def setupUi(self, PegawaiDialog):
        if not PegawaiDialog.objectName():
            PegawaiDialog.setObjectName(u"PegawaiDialog")
        PegawaiDialog.setMinimumWidth(480)
        self.mainLayout = QVBoxLayout(PegawaiDialog)
        self.mainLayout.setSpacing(15)
        self.mainLayout.setObjectName(u"mainLayout")
        self.info_grp = QGroupBox(PegawaiDialog)
        self.info_grp.setObjectName(u"info_grp")
        self.info_lay = QFormLayout(self.info_grp)
        self.info_lay.setObjectName(u"info_lay")
        self.info_lay.setVerticalSpacing(12)
        self.nama_label = QLabel(self.info_grp)
        self.nama_label.setObjectName(u"nama_label")

        self.info_lay.setWidget(0, QFormLayout.ItemRole.LabelRole, self.nama_label)

        self.nama_input = QLineEdit(self.info_grp)
        self.nama_input.setObjectName(u"nama_input")
        self.nama_input.setMaxLength(100)

        self.info_lay.setWidget(0, QFormLayout.ItemRole.FieldRole, self.nama_input)

        self.username_label = QLabel(self.info_grp)
        self.username_label.setObjectName(u"username_label")

        self.info_lay.setWidget(1, QFormLayout.ItemRole.LabelRole, self.username_label)

        self.username_input = QLineEdit(self.info_grp)
        self.username_input.setObjectName(u"username_input")
        self.username_input.setMaxLength(50)

        self.info_lay.setWidget(1, QFormLayout.ItemRole.FieldRole, self.username_input)

        self.jabatan_label = QLabel(self.info_grp)
        self.jabatan_label.setObjectName(u"jabatan_label")

        self.info_lay.setWidget(2, QFormLayout.ItemRole.LabelRole, self.jabatan_label)

        self.jabatan_combo = QComboBox(self.info_grp)
        self.jabatan_combo.setObjectName(u"jabatan_combo")

        self.info_lay.setWidget(2, QFormLayout.ItemRole.FieldRole, self.jabatan_combo)


        self.mainLayout.addWidget(self.info_grp)

        self.pwd_grp = QGroupBox(PegawaiDialog)
        self.pwd_grp.setObjectName(u"pwd_grp")
        self.pwd_lay = QFormLayout(self.pwd_grp)
        self.pwd_lay.setObjectName(u"pwd_lay")
        self.pwd_lay.setVerticalSpacing(12)
        self.reset_pwd_check = QCheckBox(self.pwd_grp)
        self.reset_pwd_check.setObjectName(u"reset_pwd_check")

        self.pwd_lay.setWidget(0, QFormLayout.ItemRole.FieldRole, self.reset_pwd_check)

        self.password_label = QLabel(self.pwd_grp)
        self.password_label.setObjectName(u"password_label")

        self.pwd_lay.setWidget(1, QFormLayout.ItemRole.LabelRole, self.password_label)

        self.password_input = QLineEdit(self.pwd_grp)
        self.password_input.setObjectName(u"password_input")
        self.password_input.setMaxLength(100)
        self.password_input.setEchoMode(QLineEdit.Password)

        self.pwd_lay.setWidget(1, QFormLayout.ItemRole.FieldRole, self.password_input)

        self.konfirmasi_label = QLabel(self.pwd_grp)
        self.konfirmasi_label.setObjectName(u"konfirmasi_label")

        self.pwd_lay.setWidget(2, QFormLayout.ItemRole.LabelRole, self.konfirmasi_label)

        self.konfirmasi_input = QLineEdit(self.pwd_grp)
        self.konfirmasi_input.setObjectName(u"konfirmasi_input")
        self.konfirmasi_input.setMaxLength(100)
        self.konfirmasi_input.setEchoMode(QLineEdit.Password)

        self.pwd_lay.setWidget(2, QFormLayout.ItemRole.FieldRole, self.konfirmasi_input)


        self.mainLayout.addWidget(self.pwd_grp)

        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.setObjectName(u"buttonLayout")
        self.buttonSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.buttonLayout.addItem(self.buttonSpacer)

        self.cancel_btn = QPushButton(PegawaiDialog)
        self.cancel_btn.setObjectName(u"cancel_btn")

        self.buttonLayout.addWidget(self.cancel_btn)

        self.save_btn = QPushButton(PegawaiDialog)
        self.save_btn.setObjectName(u"save_btn")

        self.buttonLayout.addWidget(self.save_btn)


        self.mainLayout.addLayout(self.buttonLayout)


        self.retranslateUi(PegawaiDialog)

        QMetaObject.connectSlotsByName(PegawaiDialog)
    # setupUi

    def retranslateUi(self, PegawaiDialog):
        PegawaiDialog.setWindowTitle(QCoreApplication.translate("PegawaiDialog", u"Pegawai", None))
        self.info_grp.setTitle(QCoreApplication.translate("PegawaiDialog", u"Informasi Pegawai", None))
        self.nama_label.setText(QCoreApplication.translate("PegawaiDialog", u"Nama *", None))
        self.nama_input.setPlaceholderText(QCoreApplication.translate("PegawaiDialog", u"Nama lengkap pegawai", None))
        self.username_label.setText(QCoreApplication.translate("PegawaiDialog", u"Username *", None))
        self.username_input.setPlaceholderText(QCoreApplication.translate("PegawaiDialog", u"Username untuk login", None))
        self.jabatan_label.setText(QCoreApplication.translate("PegawaiDialog", u"Jabatan *", None))
        self.pwd_grp.setTitle(QCoreApplication.translate("PegawaiDialog", u"Password", None))
        self.reset_pwd_check.setText(QCoreApplication.translate("PegawaiDialog", u"Reset / Ubah Password", None))
        self.password_label.setText(QCoreApplication.translate("PegawaiDialog", u"Password *", None))
        self.password_input.setPlaceholderText(QCoreApplication.translate("PegawaiDialog", u"Password baru", None))
        self.konfirmasi_label.setText(QCoreApplication.translate("PegawaiDialog", u"Konfirmasi *", None))
        self.konfirmasi_input.setPlaceholderText(QCoreApplication.translate("PegawaiDialog", u"Ulangi password", None))
        self.cancel_btn.setText(QCoreApplication.translate("PegawaiDialog", u"Batal", None))
        self.save_btn.setText(QCoreApplication.translate("PegawaiDialog", u"Simpan", None))
    # retranslateUi

