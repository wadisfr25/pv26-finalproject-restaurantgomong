# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'reservasi_page.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_ReservasiPageUi(object):
    def setupUi(self, ReservasiPageUi):
        if not ReservasiPageUi.objectName():
            ReservasiPageUi.setObjectName(u"ReservasiPageUi")
        self.main_layout = QVBoxLayout(ReservasiPageUi)
        self.main_layout.setSpacing(12)
        self.main_layout.setObjectName(u"main_layout")
        self.main_layout.setContentsMargins(25, 20, 25, 20)
        self.header_layout = QHBoxLayout()
        self.header_layout.setObjectName(u"header_layout")
        self.title_label = QLabel(ReservasiPageUi)
        self.title_label.setObjectName(u"title_label")

        self.header_layout.addWidget(self.title_label)

        self.header_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.header_layout.addItem(self.header_spacer)

        self.add_btn = QPushButton(ReservasiPageUi)
        self.add_btn.setObjectName(u"add_btn")
        self.add_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.header_layout.addWidget(self.add_btn)


        self.main_layout.addLayout(self.header_layout)

        self.filter_layout = QHBoxLayout()
        self.filter_layout.setObjectName(u"filter_layout")
        self.search_input = QLineEdit(ReservasiPageUi)
        self.search_input.setObjectName(u"search_input")

        self.filter_layout.addWidget(self.search_input)

        self.filter_status = QComboBox(ReservasiPageUi)
        self.filter_status.setObjectName(u"filter_status")

        self.filter_layout.addWidget(self.filter_status)


        self.main_layout.addLayout(self.filter_layout)

        self.table = QTableWidget(ReservasiPageUi)
        self.table.setObjectName(u"table")
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.setSortingEnabled(True)
        self.table.verticalHeader().setVisible(False)

        self.main_layout.addWidget(self.table)

        self.action_layout = QHBoxLayout()
        self.action_layout.setObjectName(u"action_layout")
        self.edit_btn = QPushButton(ReservasiPageUi)
        self.edit_btn.setObjectName(u"edit_btn")

        self.action_layout.addWidget(self.edit_btn)

        self.konfirmasi_btn = QPushButton(ReservasiPageUi)
        self.konfirmasi_btn.setObjectName(u"konfirmasi_btn")

        self.action_layout.addWidget(self.konfirmasi_btn)

        self.selesai_btn = QPushButton(ReservasiPageUi)
        self.selesai_btn.setObjectName(u"selesai_btn")

        self.action_layout.addWidget(self.selesai_btn)

        self.action_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.action_layout.addItem(self.action_spacer)

        self.hapus_btn = QPushButton(ReservasiPageUi)
        self.hapus_btn.setObjectName(u"hapus_btn")

        self.action_layout.addWidget(self.hapus_btn)


        self.main_layout.addLayout(self.action_layout)


        self.retranslateUi(ReservasiPageUi)

        QMetaObject.connectSlotsByName(ReservasiPageUi)
    # setupUi

    def retranslateUi(self, ReservasiPageUi):
        self.title_label.setText(QCoreApplication.translate("ReservasiPageUi", u"Manajemen Reservasi", None))
        self.title_label.setObjectName(QCoreApplication.translate("ReservasiPageUi", u"pageHeader", None))
        self.add_btn.setText(QCoreApplication.translate("ReservasiPageUi", u"+  Tambah Reservasi", None))
        self.add_btn.setObjectName(QCoreApplication.translate("ReservasiPageUi", u"primaryButton", None))
        self.search_input.setPlaceholderText(QCoreApplication.translate("ReservasiPageUi", u"Cari nama tamu atau nomor telepon...", None))
        self.edit_btn.setText(QCoreApplication.translate("ReservasiPageUi", u"Edit", None))
        self.konfirmasi_btn.setText(QCoreApplication.translate("ReservasiPageUi", u"Konfirmasi", None))
        self.konfirmasi_btn.setObjectName(QCoreApplication.translate("ReservasiPageUi", u"successButton", None))
        self.selesai_btn.setText(QCoreApplication.translate("ReservasiPageUi", u"Tandai Selesai", None))
        self.hapus_btn.setText(QCoreApplication.translate("ReservasiPageUi", u"Hapus Terpilih", None))
        self.hapus_btn.setObjectName(QCoreApplication.translate("ReservasiPageUi", u"dangerButton", None))
        pass
    # retranslateUi

