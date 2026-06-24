# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'meja_page.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_MejaPageUi(object):
    def setupUi(self, MejaPageUi):
        if not MejaPageUi.objectName():
            MejaPageUi.setObjectName(u"MejaPageUi")
        self.main_layout = QVBoxLayout(MejaPageUi)
        self.main_layout.setSpacing(14)
        self.main_layout.setObjectName(u"main_layout")
        self.main_layout.setContentsMargins(25, 20, 25, 20)
        self.header_layout = QHBoxLayout()
        self.header_layout.setObjectName(u"header_layout")
        self.title_layout = QVBoxLayout()
        self.title_layout.setSpacing(3)
        self.title_layout.setObjectName(u"title_layout")
        self.title_label = QLabel(MejaPageUi)
        self.title_label.setObjectName(u"title_label")

        self.title_layout.addWidget(self.title_label)

        self.subtitle_label = QLabel(MejaPageUi)
        self.subtitle_label.setObjectName(u"subtitle_label")

        self.title_layout.addWidget(self.subtitle_label)


        self.header_layout.addLayout(self.title_layout)

        self.header_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.header_layout.addItem(self.header_spacer)

        self.add_btn = QPushButton(MejaPageUi)
        self.add_btn.setObjectName(u"add_btn")
        self.add_btn.setMinimumHeight(38)
        self.add_btn.setMaximumHeight(38)

        self.header_layout.addWidget(self.add_btn)

        self.refresh_btn = QPushButton(MejaPageUi)
        self.refresh_btn.setObjectName(u"refresh_btn")
        self.refresh_btn.setMinimumHeight(38)
        self.refresh_btn.setMaximumHeight(38)

        self.header_layout.addWidget(self.refresh_btn)


        self.main_layout.addLayout(self.header_layout)

        self.info_label = QLabel(MejaPageUi)
        self.info_label.setObjectName(u"info_label")
        self.info_label.setWordWrap(True)

        self.main_layout.addWidget(self.info_label)

        self.mejaToolbar = QFrame(MejaPageUi)
        self.mejaToolbar.setObjectName(u"mejaToolbar")
        self.mejaToolbar.setFrameShape(QFrame.NoFrame)
        self.toolbar_layout = QVBoxLayout(self.mejaToolbar)
        self.toolbar_layout.setSpacing(10)
        self.toolbar_layout.setObjectName(u"toolbar_layout")
        self.toolbar_layout.setContentsMargins(14, 12, 14, 12)
        self.filter_layout = QHBoxLayout()
        self.filter_layout.setSpacing(10)
        self.filter_layout.setObjectName(u"filter_layout")
        self.search_input = QLineEdit(self.mejaToolbar)
        self.search_input.setObjectName(u"search_input")

        self.filter_layout.addWidget(self.search_input)

        self.filter_status = QComboBox(self.mejaToolbar)
        self.filter_status.setObjectName(u"filter_status")

        self.filter_layout.addWidget(self.filter_status)

        self.filter_kapasitas = QComboBox(self.mejaToolbar)
        self.filter_kapasitas.setObjectName(u"filter_kapasitas")

        self.filter_layout.addWidget(self.filter_kapasitas)

        self.sort_combo = QComboBox(self.mejaToolbar)
        self.sort_combo.setObjectName(u"sort_combo")

        self.filter_layout.addWidget(self.sort_combo)


        self.toolbar_layout.addLayout(self.filter_layout)

        self.legend_layout = QHBoxLayout()
        self.legend_layout.setSpacing(8)
        self.legend_layout.setObjectName(u"legend_layout")
        self.legend_tersedia = QLabel(self.mejaToolbar)
        self.legend_tersedia.setObjectName(u"legend_tersedia")

        self.legend_layout.addWidget(self.legend_tersedia)

        self.legend_terisi = QLabel(self.mejaToolbar)
        self.legend_terisi.setObjectName(u"legend_terisi")

        self.legend_layout.addWidget(self.legend_terisi)

        self.legend_dibereskan = QLabel(self.mejaToolbar)
        self.legend_dibereskan.setObjectName(u"legend_dibereskan")

        self.legend_layout.addWidget(self.legend_dibereskan)

        self.legend_maintenance = QLabel(self.mejaToolbar)
        self.legend_maintenance.setObjectName(u"legend_maintenance")

        self.legend_layout.addWidget(self.legend_maintenance)

        self.legend_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.legend_layout.addItem(self.legend_spacer)

        self.summary_lbl = QLabel(self.mejaToolbar)
        self.summary_lbl.setObjectName(u"summary_lbl")

        self.legend_layout.addWidget(self.summary_lbl)


        self.toolbar_layout.addLayout(self.legend_layout)


        self.main_layout.addWidget(self.mejaToolbar)

        self.scroll_area = QScrollArea(MejaPageUi)
        self.scroll_area.setObjectName(u"scroll_area")
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setFrameShape(QFrame.NoFrame)
        self.floor_container = QWidget()
        self.floor_container.setObjectName(u"floor_container")
        self.floor_layout = QVBoxLayout(self.floor_container)
        self.floor_layout.setSpacing(16)
        self.floor_layout.setObjectName(u"floor_layout")
        self.scroll_area.setWidget(self.floor_container)

        self.main_layout.addWidget(self.scroll_area)


        self.retranslateUi(MejaPageUi)

        QMetaObject.connectSlotsByName(MejaPageUi)
    # setupUi

    def retranslateUi(self, MejaPageUi):
        self.title_label.setText(QCoreApplication.translate("MejaPageUi", u"Manajemen Meja", None))
        self.title_label.setObjectName(QCoreApplication.translate("MejaPageUi", u"pageHeader", None))
        self.subtitle_label.setText(QCoreApplication.translate("MejaPageUi", u"Atur ketersediaan, kapasitas, dan status meja restoran.", None))
        self.subtitle_label.setObjectName(QCoreApplication.translate("MejaPageUi", u"pageSubtitle", None))
        self.add_btn.setText(QCoreApplication.translate("MejaPageUi", u"+  Tambah Meja", None))
        self.add_btn.setObjectName(QCoreApplication.translate("MejaPageUi", u"primaryButton", None))
        self.refresh_btn.setText(QCoreApplication.translate("MejaPageUi", u"Refresh", None))
        self.refresh_btn.setObjectName(QCoreApplication.translate("MejaPageUi", u"secondaryButton", None))
        self.info_label.setText(QCoreApplication.translate("MejaPageUi", u"Status meja otomatis mengikuti reservasi aktif. Klik kartu meja untuk edit, hapus, atau ubah status maintenance.", None))
        self.info_label.setObjectName(QCoreApplication.translate("MejaPageUi", u"infoBanner", None))
        self.search_input.setPlaceholderText(QCoreApplication.translate("MejaPageUi", u"Cari nomor meja atau jenis...", None))
        self.legend_tersedia.setText(QCoreApplication.translate("MejaPageUi", u"Tersedia", None))
        self.legend_tersedia.setStyleSheet(QCoreApplication.translate("MejaPageUi", u"color: #1E8449; font-weight: bold; font-size: 12px;", None))
        self.legend_terisi.setText(QCoreApplication.translate("MejaPageUi", u"Terisi", None))
        self.legend_terisi.setStyleSheet(QCoreApplication.translate("MejaPageUi", u"color: #C0392B; font-weight: bold; font-size: 12px;", None))
        self.legend_dibereskan.setText(QCoreApplication.translate("MejaPageUi", u"Dibereskan", None))
        self.legend_dibereskan.setStyleSheet(QCoreApplication.translate("MejaPageUi", u"color: #2874A6; font-weight: bold; font-size: 12px;", None))
        self.legend_maintenance.setText(QCoreApplication.translate("MejaPageUi", u"Maintenance", None))
        self.legend_maintenance.setStyleSheet(QCoreApplication.translate("MejaPageUi", u"color: #B9770E; font-weight: bold; font-size: 12px;", None))
        self.summary_lbl.setObjectName(QCoreApplication.translate("MejaPageUi", u"mejaSummary", None))
        pass
    # retranslateUi

