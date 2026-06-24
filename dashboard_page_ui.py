# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dashboard_page.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QSizePolicy, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_DashboardPageUi(object):
    def setupUi(self, DashboardPageUi):
        if not DashboardPageUi.objectName():
            DashboardPageUi.setObjectName(u"DashboardPageUi")
        self.main_layout = QVBoxLayout(DashboardPageUi)
        self.main_layout.setSpacing(18)
        self.main_layout.setObjectName(u"main_layout")
        self.main_layout.setContentsMargins(28, 24, 28, 24)
        self.header_label = QLabel(DashboardPageUi)
        self.header_label.setObjectName(u"header_label")

        self.main_layout.addWidget(self.header_label)

        self.date_label = QLabel(DashboardPageUi)
        self.date_label.setObjectName(u"date_label")

        self.main_layout.addWidget(self.date_label)

        self.cards_layout = QHBoxLayout()
        self.cards_layout.setSpacing(16)
        self.cards_layout.setObjectName(u"cards_layout")
        self.card_hari_ini = QFrame(DashboardPageUi)
        self.card_hari_ini.setObjectName(u"card_hari_ini")
        self.card_hari_ini_layout = QVBoxLayout(self.card_hari_ini)
        self.card_hari_ini_layout.setObjectName(u"card_hari_ini_layout")
        self.card_hari_ini_layout.setContentsMargins(18, 12, 18, 12)
        self.card_hari_ini_value = QLabel(self.card_hari_ini)
        self.card_hari_ini_value.setObjectName(u"card_hari_ini_value")
        self.card_hari_ini_value.setAlignment(Qt.AlignCenter)

        self.card_hari_ini_layout.addWidget(self.card_hari_ini_value)

        self.card_hari_ini_title = QLabel(self.card_hari_ini)
        self.card_hari_ini_title.setObjectName(u"card_hari_ini_title")
        self.card_hari_ini_title.setAlignment(Qt.AlignCenter)
        self.card_hari_ini_title.setWordWrap(True)

        self.card_hari_ini_layout.addWidget(self.card_hari_ini_title)


        self.cards_layout.addWidget(self.card_hari_ini)

        self.card_menunggu = QFrame(DashboardPageUi)
        self.card_menunggu.setObjectName(u"card_menunggu")
        self.card_menunggu_layout = QVBoxLayout(self.card_menunggu)
        self.card_menunggu_layout.setObjectName(u"card_menunggu_layout")
        self.card_menunggu_layout.setContentsMargins(18, 12, 18, 12)
        self.card_menunggu_value = QLabel(self.card_menunggu)
        self.card_menunggu_value.setObjectName(u"card_menunggu_value")
        self.card_menunggu_value.setAlignment(Qt.AlignCenter)

        self.card_menunggu_layout.addWidget(self.card_menunggu_value)

        self.card_menunggu_title = QLabel(self.card_menunggu)
        self.card_menunggu_title.setObjectName(u"card_menunggu_title")
        self.card_menunggu_title.setAlignment(Qt.AlignCenter)
        self.card_menunggu_title.setWordWrap(True)

        self.card_menunggu_layout.addWidget(self.card_menunggu_title)


        self.cards_layout.addWidget(self.card_menunggu)

        self.card_selesai = QFrame(DashboardPageUi)
        self.card_selesai.setObjectName(u"card_selesai")
        self.card_selesai_layout = QVBoxLayout(self.card_selesai)
        self.card_selesai_layout.setObjectName(u"card_selesai_layout")
        self.card_selesai_layout.setContentsMargins(18, 12, 18, 12)
        self.card_selesai_value = QLabel(self.card_selesai)
        self.card_selesai_value.setObjectName(u"card_selesai_value")
        self.card_selesai_value.setAlignment(Qt.AlignCenter)

        self.card_selesai_layout.addWidget(self.card_selesai_value)

        self.card_selesai_title = QLabel(self.card_selesai)
        self.card_selesai_title.setObjectName(u"card_selesai_title")
        self.card_selesai_title.setAlignment(Qt.AlignCenter)
        self.card_selesai_title.setWordWrap(True)

        self.card_selesai_layout.addWidget(self.card_selesai_title)


        self.cards_layout.addWidget(self.card_selesai)

        self.card_total = QFrame(DashboardPageUi)
        self.card_total.setObjectName(u"card_total")
        self.card_total_layout = QVBoxLayout(self.card_total)
        self.card_total_layout.setObjectName(u"card_total_layout")
        self.card_total_layout.setContentsMargins(18, 12, 18, 12)
        self.card_total_value = QLabel(self.card_total)
        self.card_total_value.setObjectName(u"card_total_value")
        self.card_total_value.setAlignment(Qt.AlignCenter)

        self.card_total_layout.addWidget(self.card_total_value)

        self.card_total_title = QLabel(self.card_total)
        self.card_total_title.setObjectName(u"card_total_title")
        self.card_total_title.setAlignment(Qt.AlignCenter)
        self.card_total_title.setWordWrap(True)

        self.card_total_layout.addWidget(self.card_total_title)


        self.cards_layout.addWidget(self.card_total)


        self.main_layout.addLayout(self.cards_layout)

        self.bottom_layout = QHBoxLayout()
        self.bottom_layout.setSpacing(16)
        self.bottom_layout.setObjectName(u"bottom_layout")
        self.table_wrap = QWidget(DashboardPageUi)
        self.table_wrap.setObjectName(u"table_wrap")
        self.table_layout = QVBoxLayout(self.table_wrap)
        self.table_layout.setSpacing(8)
        self.table_layout.setObjectName(u"table_layout")
        self.table_layout.setContentsMargins(0, 0, 0, 0)
        self.section_label = QLabel(self.table_wrap)
        self.section_label.setObjectName(u"section_label")

        self.table_layout.addWidget(self.section_label)

        self.today_table = QTableWidget(self.table_wrap)
        self.today_table.setObjectName(u"today_table")
        self.today_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.today_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.today_table.verticalHeader().setVisible(False)

        self.table_layout.addWidget(self.today_table)


        self.bottom_layout.addWidget(self.table_wrap)

        self.chart_container = QWidget(DashboardPageUi)
        self.chart_container.setObjectName(u"chart_container")
        self.chart_container.setMinimumWidth(280)
        self.chart_layout = QVBoxLayout(self.chart_container)
        self.chart_layout.setObjectName(u"chart_layout")
        self.chart_layout.setContentsMargins(0, 0, 0, 0)

        self.bottom_layout.addWidget(self.chart_container)


        self.main_layout.addLayout(self.bottom_layout)


        self.retranslateUi(DashboardPageUi)

        QMetaObject.connectSlotsByName(DashboardPageUi)
    # setupUi

    def retranslateUi(self, DashboardPageUi):
        self.header_label.setObjectName(QCoreApplication.translate("DashboardPageUi", u"pageHeader", None))
        self.date_label.setObjectName(QCoreApplication.translate("DashboardPageUi", u"dateLabel", None))
        self.card_hari_ini.setObjectName(QCoreApplication.translate("DashboardPageUi", u"dashCard", None))
        self.card_hari_ini_value.setText(QCoreApplication.translate("DashboardPageUi", u"0", None))
        self.card_hari_ini_value.setObjectName(QCoreApplication.translate("DashboardPageUi", u"cardValue", None))
        self.card_hari_ini_title.setText(QCoreApplication.translate("DashboardPageUi", u"Reservasi Hari Ini", None))
        self.card_hari_ini_title.setObjectName(QCoreApplication.translate("DashboardPageUi", u"cardTitle", None))
        self.card_menunggu.setObjectName(QCoreApplication.translate("DashboardPageUi", u"dashCard", None))
        self.card_menunggu_value.setText(QCoreApplication.translate("DashboardPageUi", u"0", None))
        self.card_menunggu_value.setObjectName(QCoreApplication.translate("DashboardPageUi", u"cardValue", None))
        self.card_menunggu_title.setText(QCoreApplication.translate("DashboardPageUi", u"Menunggu Konfirmasi", None))
        self.card_menunggu_title.setObjectName(QCoreApplication.translate("DashboardPageUi", u"cardTitle", None))
        self.card_selesai.setObjectName(QCoreApplication.translate("DashboardPageUi", u"dashCard", None))
        self.card_selesai_value.setText(QCoreApplication.translate("DashboardPageUi", u"0", None))
        self.card_selesai_value.setObjectName(QCoreApplication.translate("DashboardPageUi", u"cardValue", None))
        self.card_selesai_title.setText(QCoreApplication.translate("DashboardPageUi", u"Selesai Hari Ini", None))
        self.card_selesai_title.setObjectName(QCoreApplication.translate("DashboardPageUi", u"cardTitle", None))
        self.card_total.setObjectName(QCoreApplication.translate("DashboardPageUi", u"dashCard", None))
        self.card_total_value.setText(QCoreApplication.translate("DashboardPageUi", u"0", None))
        self.card_total_value.setObjectName(QCoreApplication.translate("DashboardPageUi", u"cardValue", None))
        self.card_total_title.setText(QCoreApplication.translate("DashboardPageUi", u"Total Reservasi Aktif", None))
        self.card_total_title.setObjectName(QCoreApplication.translate("DashboardPageUi", u"cardTitle", None))
        self.section_label.setText(QCoreApplication.translate("DashboardPageUi", u"Reservasi Hari Ini", None))
        self.section_label.setObjectName(QCoreApplication.translate("DashboardPageUi", u"sectionTitle", None))
        pass
    # retranslateUi

