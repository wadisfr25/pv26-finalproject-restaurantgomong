# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pegawai_page.ui'
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

class Ui_PegawaiPageUi(object):
    def setupUi(self, PegawaiPageUi):
        if not PegawaiPageUi.objectName():
            PegawaiPageUi.setObjectName(u"PegawaiPageUi")
        self.main_layout = QVBoxLayout(PegawaiPageUi)
        self.main_layout.setSpacing(12)
        self.main_layout.setObjectName(u"main_layout")
        self.main_layout.setContentsMargins(25, 20, 25, 20)
        self.header_layout = QHBoxLayout()
        self.header_layout.setObjectName(u"header_layout")
        self.title_label = QLabel(PegawaiPageUi)
        self.title_label.setObjectName(u"title_label")

        self.header_layout.addWidget(self.title_label)

        self.header_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.header_layout.addItem(self.header_spacer)

        self.add_btn = QPushButton(PegawaiPageUi)
        self.add_btn.setObjectName(u"add_btn")
        self.add_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.header_layout.addWidget(self.add_btn)


        self.main_layout.addLayout(self.header_layout)

        self.filter_layout = QHBoxLayout()
        self.filter_layout.setObjectName(u"filter_layout")
        self.search_input = QLineEdit(PegawaiPageUi)
        self.search_input.setObjectName(u"search_input")

        self.filter_layout.addWidget(self.search_input)

        self.filter_jabatan = QComboBox(PegawaiPageUi)
        self.filter_jabatan.setObjectName(u"filter_jabatan")

        self.filter_layout.addWidget(self.filter_jabatan)


        self.main_layout.addLayout(self.filter_layout)

        self.table = QTableWidget(PegawaiPageUi)
        self.table.setObjectName(u"table")
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.setSortingEnabled(True)
        self.table.verticalHeader().setVisible(False)

        self.main_layout.addWidget(self.table)

        self.action_layout = QHBoxLayout()
        self.action_layout.setObjectName(u"action_layout")
        self.edit_btn = QPushButton(PegawaiPageUi)
        self.edit_btn.setObjectName(u"edit_btn")

        self.action_layout.addWidget(self.edit_btn)

        self.action_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.action_layout.addItem(self.action_spacer)

        self.hapus_btn = QPushButton(PegawaiPageUi)
        self.hapus_btn.setObjectName(u"hapus_btn")

        self.action_layout.addWidget(self.hapus_btn)


        self.main_layout.addLayout(self.action_layout)


        self.retranslateUi(PegawaiPageUi)

        QMetaObject.connectSlotsByName(PegawaiPageUi)
    # setupUi

    def retranslateUi(self, PegawaiPageUi):
        self.title_label.setText(QCoreApplication.translate("PegawaiPageUi", u"Manajemen Pegawai", None))
        self.title_label.setObjectName(QCoreApplication.translate("PegawaiPageUi", u"pageHeader", None))
        self.add_btn.setText(QCoreApplication.translate("PegawaiPageUi", u"+  Tambah Pegawai", None))
        self.add_btn.setObjectName(QCoreApplication.translate("PegawaiPageUi", u"primaryButton", None))
        self.search_input.setPlaceholderText(QCoreApplication.translate("PegawaiPageUi", u"Cari nama atau username pegawai...", None))
        self.edit_btn.setText(QCoreApplication.translate("PegawaiPageUi", u"Edit", None))
        self.hapus_btn.setText(QCoreApplication.translate("PegawaiPageUi", u"Hapus Terpilih", None))
        self.hapus_btn.setObjectName(QCoreApplication.translate("PegawaiPageUi", u"dangerButton", None))
        pass
    # retranslateUi

