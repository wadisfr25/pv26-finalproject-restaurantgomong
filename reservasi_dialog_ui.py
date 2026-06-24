# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'reservasi_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QDialog,
    QFormLayout, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QTextEdit, QVBoxLayout, QWidget)

class Ui_ReservasiDialog(object):
    def setupUi(self, ReservasiDialog):
        if not ReservasiDialog.objectName():
            ReservasiDialog.setObjectName(u"ReservasiDialog")
        ReservasiDialog.setMinimumWidth(520)
        self.mainLayout = QVBoxLayout(ReservasiDialog)
        self.mainLayout.setSpacing(15)
        self.mainLayout.setObjectName(u"mainLayout")
        self.tamu_grp = QGroupBox(ReservasiDialog)
        self.tamu_grp.setObjectName(u"tamu_grp")
        self.tamu_lay = QFormLayout(self.tamu_grp)
        self.tamu_lay.setObjectName(u"tamu_lay")
        self.tamu_lay.setVerticalSpacing(12)
        self.nama_label = QLabel(self.tamu_grp)
        self.nama_label.setObjectName(u"nama_label")

        self.tamu_lay.setWidget(0, QFormLayout.ItemRole.LabelRole, self.nama_label)

        self.nama_input = QLineEdit(self.tamu_grp)
        self.nama_input.setObjectName(u"nama_input")
        self.nama_input.setMaxLength(100)

        self.tamu_lay.setWidget(0, QFormLayout.ItemRole.FieldRole, self.nama_input)

        self.telepon_label = QLabel(self.tamu_grp)
        self.telepon_label.setObjectName(u"telepon_label")

        self.tamu_lay.setWidget(1, QFormLayout.ItemRole.LabelRole, self.telepon_label)

        self.telepon_input = QLineEdit(self.tamu_grp)
        self.telepon_input.setObjectName(u"telepon_input")
        self.telepon_input.setMaxLength(15)

        self.tamu_lay.setWidget(1, QFormLayout.ItemRole.FieldRole, self.telepon_input)

        self.jumlah_label = QLabel(self.tamu_grp)
        self.jumlah_label.setObjectName(u"jumlah_label")

        self.tamu_lay.setWidget(2, QFormLayout.ItemRole.LabelRole, self.jumlah_label)

        self.jumlah_input = QSpinBox(self.tamu_grp)
        self.jumlah_input.setObjectName(u"jumlah_input")
        self.jumlah_input.setMinimum(1)
        self.jumlah_input.setMaximum(8)
        self.jumlah_input.setValue(2)

        self.tamu_lay.setWidget(2, QFormLayout.ItemRole.FieldRole, self.jumlah_input)


        self.mainLayout.addWidget(self.tamu_grp)

        self.res_grp = QGroupBox(ReservasiDialog)
        self.res_grp.setObjectName(u"res_grp")
        self.res_lay = QFormLayout(self.res_grp)
        self.res_lay.setObjectName(u"res_lay")
        self.res_lay.setVerticalSpacing(12)
        self.tanggal_label = QLabel(self.res_grp)
        self.tanggal_label.setObjectName(u"tanggal_label")

        self.res_lay.setWidget(0, QFormLayout.ItemRole.LabelRole, self.tanggal_label)

        self.tanggal_input = QDateEdit(self.res_grp)
        self.tanggal_input.setObjectName(u"tanggal_input")
        self.tanggal_input.setCalendarPopup(True)

        self.res_lay.setWidget(0, QFormLayout.ItemRole.FieldRole, self.tanggal_input)

        self.waktu_label = QLabel(self.res_grp)
        self.waktu_label.setObjectName(u"waktu_label")

        self.res_lay.setWidget(1, QFormLayout.ItemRole.LabelRole, self.waktu_label)

        self.waktu_combo = QComboBox(self.res_grp)
        self.waktu_combo.setObjectName(u"waktu_combo")

        self.res_lay.setWidget(1, QFormLayout.ItemRole.FieldRole, self.waktu_combo)

        self.meja_label = QLabel(self.res_grp)
        self.meja_label.setObjectName(u"meja_label")

        self.res_lay.setWidget(2, QFormLayout.ItemRole.LabelRole, self.meja_label)

        self.meja_combo = QComboBox(self.res_grp)
        self.meja_combo.setObjectName(u"meja_combo")

        self.res_lay.setWidget(2, QFormLayout.ItemRole.FieldRole, self.meja_combo)

        self.info_meja_lbl = QLabel(self.res_grp)
        self.info_meja_lbl.setObjectName(u"info_meja_lbl")
        self.info_meja_lbl.setStyleSheet(u"color: #1A5276; font-size: 10px; font-style: italic;")

        self.res_lay.setWidget(3, QFormLayout.ItemRole.FieldRole, self.info_meja_lbl)

        self.status_label = QLabel(self.res_grp)
        self.status_label.setObjectName(u"status_label")

        self.res_lay.setWidget(4, QFormLayout.ItemRole.LabelRole, self.status_label)

        self.status_combo = QComboBox(self.res_grp)
        self.status_combo.setObjectName(u"status_combo")

        self.res_lay.setWidget(4, QFormLayout.ItemRole.FieldRole, self.status_combo)

        self.catatan_label = QLabel(self.res_grp)
        self.catatan_label.setObjectName(u"catatan_label")

        self.res_lay.setWidget(5, QFormLayout.ItemRole.LabelRole, self.catatan_label)

        self.catatan_input = QTextEdit(self.res_grp)
        self.catatan_input.setObjectName(u"catatan_input")
        self.catatan_input.setMaximumHeight(75)

        self.res_lay.setWidget(5, QFormLayout.ItemRole.FieldRole, self.catatan_input)


        self.mainLayout.addWidget(self.res_grp)

        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.setObjectName(u"buttonLayout")
        self.buttonSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.buttonLayout.addItem(self.buttonSpacer)

        self.cancel_btn = QPushButton(ReservasiDialog)
        self.cancel_btn.setObjectName(u"cancel_btn")

        self.buttonLayout.addWidget(self.cancel_btn)

        self.save_btn = QPushButton(ReservasiDialog)
        self.save_btn.setObjectName(u"save_btn")

        self.buttonLayout.addWidget(self.save_btn)


        self.mainLayout.addLayout(self.buttonLayout)


        self.retranslateUi(ReservasiDialog)

        QMetaObject.connectSlotsByName(ReservasiDialog)
    # setupUi

    def retranslateUi(self, ReservasiDialog):
        ReservasiDialog.setWindowTitle(QCoreApplication.translate("ReservasiDialog", u"Reservasi", None))
        self.tamu_grp.setTitle(QCoreApplication.translate("ReservasiDialog", u"Informasi Tamu", None))
        self.nama_label.setText(QCoreApplication.translate("ReservasiDialog", u"Nama Tamu *", None))
        self.nama_input.setPlaceholderText(QCoreApplication.translate("ReservasiDialog", u"Masukkan nama lengkap tamu", None))
        self.telepon_label.setText(QCoreApplication.translate("ReservasiDialog", u"No. Telepon *", None))
        self.telepon_input.setPlaceholderText(QCoreApplication.translate("ReservasiDialog", u"08xxxxxxxxxx", None))
        self.jumlah_label.setText(QCoreApplication.translate("ReservasiDialog", u"Jumlah Tamu *", None))
        self.jumlah_input.setSuffix(QCoreApplication.translate("ReservasiDialog", u"  orang", None))
        self.res_grp.setTitle(QCoreApplication.translate("ReservasiDialog", u"Detail Reservasi", None))
        self.tanggal_label.setText(QCoreApplication.translate("ReservasiDialog", u"Tanggal *", None))
        self.waktu_label.setText(QCoreApplication.translate("ReservasiDialog", u"Jam *", None))
        self.meja_label.setText(QCoreApplication.translate("ReservasiDialog", u"Pilih Meja", None))
        self.info_meja_lbl.setText("")
        self.status_label.setText(QCoreApplication.translate("ReservasiDialog", u"Status", None))
        self.catatan_label.setText(QCoreApplication.translate("ReservasiDialog", u"Catatan", None))
        self.catatan_input.setPlaceholderText(QCoreApplication.translate("ReservasiDialog", u"Catatan khusus: alergi makanan, dekorasi, permintaan meja window seat, dll.", None))
        self.cancel_btn.setText(QCoreApplication.translate("ReservasiDialog", u"Batal", None))
        self.save_btn.setText(QCoreApplication.translate("ReservasiDialog", u"Simpan Reservasi", None))
    # retranslateUi

