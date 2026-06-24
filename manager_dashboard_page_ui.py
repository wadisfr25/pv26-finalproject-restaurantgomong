# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'manager_dashboard_page.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QSizePolicy,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_ManagerDashboardPageUi(object):
    def setupUi(self, ManagerDashboardPageUi):
        if not ManagerDashboardPageUi.objectName():
            ManagerDashboardPageUi.setObjectName(u"ManagerDashboardPageUi")
        self.main_layout = QVBoxLayout(ManagerDashboardPageUi)
        self.main_layout.setSpacing(18)
        self.main_layout.setObjectName(u"main_layout")
        self.main_layout.setContentsMargins(28, 24, 28, 24)
        self.header_label = QLabel(ManagerDashboardPageUi)
        self.header_label.setObjectName(u"header_label")

        self.main_layout.addWidget(self.header_label)

        self.date_label = QLabel(ManagerDashboardPageUi)
        self.date_label.setObjectName(u"date_label")

        self.main_layout.addWidget(self.date_label)

        self.reservasi_group = QGroupBox(ManagerDashboardPageUi)
        self.reservasi_group.setObjectName(u"reservasi_group")
        self.reservasi_layout = QHBoxLayout(self.reservasi_group)
        self.reservasi_layout.setSpacing(12)
        self.reservasi_layout.setObjectName(u"reservasi_layout")
        self.card_total = QFrame(self.reservasi_group)
        self.card_total.setObjectName(u"card_total")
        self.vboxLayout = QVBoxLayout(self.card_total)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.card_total_value = QLabel(self.card_total)
        self.card_total_value.setObjectName(u"card_total_value")
        self.card_total_value.setAlignment(Qt.AlignCenter)

        self.vboxLayout.addWidget(self.card_total_value)

        self.card_total_title = QLabel(self.card_total)
        self.card_total_title.setObjectName(u"card_total_title")
        self.card_total_title.setAlignment(Qt.AlignCenter)

        self.vboxLayout.addWidget(self.card_total_title)


        self.reservasi_layout.addWidget(self.card_total)

        self.card_hari_ini = QFrame(self.reservasi_group)
        self.card_hari_ini.setObjectName(u"card_hari_ini")
        self.vboxLayout1 = QVBoxLayout(self.card_hari_ini)
        self.vboxLayout1.setObjectName(u"vboxLayout1")
        self.card_hari_ini_value = QLabel(self.card_hari_ini)
        self.card_hari_ini_value.setObjectName(u"card_hari_ini_value")
        self.card_hari_ini_value.setAlignment(Qt.AlignCenter)

        self.vboxLayout1.addWidget(self.card_hari_ini_value)

        self.card_hari_ini_title = QLabel(self.card_hari_ini)
        self.card_hari_ini_title.setObjectName(u"card_hari_ini_title")
        self.card_hari_ini_title.setAlignment(Qt.AlignCenter)

        self.vboxLayout1.addWidget(self.card_hari_ini_title)


        self.reservasi_layout.addWidget(self.card_hari_ini)

        self.card_menunggu = QFrame(self.reservasi_group)
        self.card_menunggu.setObjectName(u"card_menunggu")
        self.vboxLayout2 = QVBoxLayout(self.card_menunggu)
        self.vboxLayout2.setObjectName(u"vboxLayout2")
        self.card_menunggu_value = QLabel(self.card_menunggu)
        self.card_menunggu_value.setObjectName(u"card_menunggu_value")
        self.card_menunggu_value.setAlignment(Qt.AlignCenter)

        self.vboxLayout2.addWidget(self.card_menunggu_value)

        self.card_menunggu_title = QLabel(self.card_menunggu)
        self.card_menunggu_title.setObjectName(u"card_menunggu_title")
        self.card_menunggu_title.setAlignment(Qt.AlignCenter)

        self.vboxLayout2.addWidget(self.card_menunggu_title)


        self.reservasi_layout.addWidget(self.card_menunggu)

        self.card_dibatalkan = QFrame(self.reservasi_group)
        self.card_dibatalkan.setObjectName(u"card_dibatalkan")
        self.vboxLayout3 = QVBoxLayout(self.card_dibatalkan)
        self.vboxLayout3.setObjectName(u"vboxLayout3")
        self.card_dibatalkan_value = QLabel(self.card_dibatalkan)
        self.card_dibatalkan_value.setObjectName(u"card_dibatalkan_value")
        self.card_dibatalkan_value.setAlignment(Qt.AlignCenter)

        self.vboxLayout3.addWidget(self.card_dibatalkan_value)

        self.card_dibatalkan_title = QLabel(self.card_dibatalkan)
        self.card_dibatalkan_title.setObjectName(u"card_dibatalkan_title")
        self.card_dibatalkan_title.setAlignment(Qt.AlignCenter)

        self.vboxLayout3.addWidget(self.card_dibatalkan_title)


        self.reservasi_layout.addWidget(self.card_dibatalkan)


        self.main_layout.addWidget(self.reservasi_group)

        self.info_layout = QHBoxLayout()
        self.info_layout.setSpacing(16)
        self.info_layout.setObjectName(u"info_layout")
        self.meja_group = QGroupBox(ManagerDashboardPageUi)
        self.meja_group.setObjectName(u"meja_group")
        self.meja_layout = QHBoxLayout(self.meja_group)
        self.meja_layout.setSpacing(12)
        self.meja_layout.setObjectName(u"meja_layout")
        self.card_meja_tersedia = QFrame(self.meja_group)
        self.card_meja_tersedia.setObjectName(u"card_meja_tersedia")
        self.vboxLayout4 = QVBoxLayout(self.card_meja_tersedia)
        self.vboxLayout4.setObjectName(u"vboxLayout4")
        self.card_meja_tersedia_value = QLabel(self.card_meja_tersedia)
        self.card_meja_tersedia_value.setObjectName(u"card_meja_tersedia_value")
        self.card_meja_tersedia_value.setAlignment(Qt.AlignCenter)

        self.vboxLayout4.addWidget(self.card_meja_tersedia_value)

        self.card_meja_tersedia_title = QLabel(self.card_meja_tersedia)
        self.card_meja_tersedia_title.setObjectName(u"card_meja_tersedia_title")
        self.card_meja_tersedia_title.setAlignment(Qt.AlignCenter)

        self.vboxLayout4.addWidget(self.card_meja_tersedia_title)


        self.meja_layout.addWidget(self.card_meja_tersedia)

        self.card_meja_terisi = QFrame(self.meja_group)
        self.card_meja_terisi.setObjectName(u"card_meja_terisi")
        self.vboxLayout5 = QVBoxLayout(self.card_meja_terisi)
        self.vboxLayout5.setObjectName(u"vboxLayout5")
        self.card_meja_terisi_value = QLabel(self.card_meja_terisi)
        self.card_meja_terisi_value.setObjectName(u"card_meja_terisi_value")
        self.card_meja_terisi_value.setAlignment(Qt.AlignCenter)

        self.vboxLayout5.addWidget(self.card_meja_terisi_value)

        self.card_meja_terisi_title = QLabel(self.card_meja_terisi)
        self.card_meja_terisi_title.setObjectName(u"card_meja_terisi_title")
        self.card_meja_terisi_title.setAlignment(Qt.AlignCenter)

        self.vboxLayout5.addWidget(self.card_meja_terisi_title)


        self.meja_layout.addWidget(self.card_meja_terisi)

        self.card_meja_maintenance = QFrame(self.meja_group)
        self.card_meja_maintenance.setObjectName(u"card_meja_maintenance")
        self.vboxLayout6 = QVBoxLayout(self.card_meja_maintenance)
        self.vboxLayout6.setObjectName(u"vboxLayout6")
        self.card_meja_maintenance_value = QLabel(self.card_meja_maintenance)
        self.card_meja_maintenance_value.setObjectName(u"card_meja_maintenance_value")
        self.card_meja_maintenance_value.setAlignment(Qt.AlignCenter)

        self.vboxLayout6.addWidget(self.card_meja_maintenance_value)

        self.card_meja_maintenance_title = QLabel(self.card_meja_maintenance)
        self.card_meja_maintenance_title.setObjectName(u"card_meja_maintenance_title")
        self.card_meja_maintenance_title.setAlignment(Qt.AlignCenter)

        self.vboxLayout6.addWidget(self.card_meja_maintenance_title)


        self.meja_layout.addWidget(self.card_meja_maintenance)


        self.info_layout.addWidget(self.meja_group)

        self.pegawai_group = QGroupBox(ManagerDashboardPageUi)
        self.pegawai_group.setObjectName(u"pegawai_group")
        self.pegawai_layout = QHBoxLayout(self.pegawai_group)
        self.pegawai_layout.setSpacing(12)
        self.pegawai_layout.setObjectName(u"pegawai_layout")
        self.card_total_pegawai = QFrame(self.pegawai_group)
        self.card_total_pegawai.setObjectName(u"card_total_pegawai")
        self.vboxLayout7 = QVBoxLayout(self.card_total_pegawai)
        self.vboxLayout7.setObjectName(u"vboxLayout7")
        self.card_total_pegawai_value = QLabel(self.card_total_pegawai)
        self.card_total_pegawai_value.setObjectName(u"card_total_pegawai_value")
        self.card_total_pegawai_value.setAlignment(Qt.AlignCenter)

        self.vboxLayout7.addWidget(self.card_total_pegawai_value)

        self.card_total_pegawai_title = QLabel(self.card_total_pegawai)
        self.card_total_pegawai_title.setObjectName(u"card_total_pegawai_title")
        self.card_total_pegawai_title.setAlignment(Qt.AlignCenter)

        self.vboxLayout7.addWidget(self.card_total_pegawai_title)


        self.pegawai_layout.addWidget(self.card_total_pegawai)

        self.card_manajer = QFrame(self.pegawai_group)
        self.card_manajer.setObjectName(u"card_manajer")
        self.vboxLayout8 = QVBoxLayout(self.card_manajer)
        self.vboxLayout8.setObjectName(u"vboxLayout8")
        self.card_manajer_value = QLabel(self.card_manajer)
        self.card_manajer_value.setObjectName(u"card_manajer_value")
        self.card_manajer_value.setAlignment(Qt.AlignCenter)

        self.vboxLayout8.addWidget(self.card_manajer_value)

        self.card_manajer_title = QLabel(self.card_manajer)
        self.card_manajer_title.setObjectName(u"card_manajer_title")
        self.card_manajer_title.setAlignment(Qt.AlignCenter)

        self.vboxLayout8.addWidget(self.card_manajer_title)


        self.pegawai_layout.addWidget(self.card_manajer)

        self.card_staf = QFrame(self.pegawai_group)
        self.card_staf.setObjectName(u"card_staf")
        self.vboxLayout9 = QVBoxLayout(self.card_staf)
        self.vboxLayout9.setObjectName(u"vboxLayout9")
        self.card_staf_value = QLabel(self.card_staf)
        self.card_staf_value.setObjectName(u"card_staf_value")
        self.card_staf_value.setAlignment(Qt.AlignCenter)

        self.vboxLayout9.addWidget(self.card_staf_value)

        self.card_staf_title = QLabel(self.card_staf)
        self.card_staf_title.setObjectName(u"card_staf_title")
        self.card_staf_title.setAlignment(Qt.AlignCenter)

        self.vboxLayout9.addWidget(self.card_staf_title)


        self.pegawai_layout.addWidget(self.card_staf)


        self.info_layout.addWidget(self.pegawai_group)


        self.main_layout.addLayout(self.info_layout)

        self.ai_group = QGroupBox(ManagerDashboardPageUi)
        self.ai_group.setObjectName(u"ai_group")
        self.ai_layout = QHBoxLayout(self.ai_group)
        self.ai_layout.setSpacing(12)
        self.ai_layout.setObjectName(u"ai_layout")
        self.card_ai_jam = QFrame(self.ai_group)
        self.card_ai_jam.setObjectName(u"card_ai_jam")
        self.vboxLayout10 = QVBoxLayout(self.card_ai_jam)
        self.vboxLayout10.setObjectName(u"vboxLayout10")
        self.card_ai_jam_value = QLabel(self.card_ai_jam)
        self.card_ai_jam_value.setObjectName(u"card_ai_jam_value")
        self.card_ai_jam_value.setAlignment(Qt.AlignCenter)

        self.vboxLayout10.addWidget(self.card_ai_jam_value)

        self.card_ai_jam_title = QLabel(self.card_ai_jam)
        self.card_ai_jam_title.setObjectName(u"card_ai_jam_title")
        self.card_ai_jam_title.setAlignment(Qt.AlignCenter)

        self.vboxLayout10.addWidget(self.card_ai_jam_title)


        self.ai_layout.addWidget(self.card_ai_jam)

        self.card_ai_tamu = QFrame(self.ai_group)
        self.card_ai_tamu.setObjectName(u"card_ai_tamu")
        self.vboxLayout11 = QVBoxLayout(self.card_ai_tamu)
        self.vboxLayout11.setObjectName(u"vboxLayout11")
        self.card_ai_tamu_value = QLabel(self.card_ai_tamu)
        self.card_ai_tamu_value.setObjectName(u"card_ai_tamu_value")
        self.card_ai_tamu_value.setAlignment(Qt.AlignCenter)

        self.vboxLayout11.addWidget(self.card_ai_tamu_value)

        self.card_ai_tamu_title = QLabel(self.card_ai_tamu)
        self.card_ai_tamu_title.setObjectName(u"card_ai_tamu_title")
        self.card_ai_tamu_title.setAlignment(Qt.AlignCenter)

        self.vboxLayout11.addWidget(self.card_ai_tamu_title)


        self.ai_layout.addWidget(self.card_ai_tamu)

        self.card_ai_staf = QFrame(self.ai_group)
        self.card_ai_staf.setObjectName(u"card_ai_staf")
        self.vboxLayout12 = QVBoxLayout(self.card_ai_staf)
        self.vboxLayout12.setObjectName(u"vboxLayout12")
        self.card_ai_staf_value = QLabel(self.card_ai_staf)
        self.card_ai_staf_value.setObjectName(u"card_ai_staf_value")
        self.card_ai_staf_value.setAlignment(Qt.AlignCenter)

        self.vboxLayout12.addWidget(self.card_ai_staf_value)

        self.card_ai_staf_title = QLabel(self.card_ai_staf)
        self.card_ai_staf_title.setObjectName(u"card_ai_staf_title")
        self.card_ai_staf_title.setAlignment(Qt.AlignCenter)

        self.vboxLayout12.addWidget(self.card_ai_staf_title)


        self.ai_layout.addWidget(self.card_ai_staf)


        self.main_layout.addWidget(self.ai_group)

        self.bottom_layout = QHBoxLayout()
        self.bottom_layout.setSpacing(16)
        self.bottom_layout.setObjectName(u"bottom_layout")
        self.today_group = QGroupBox(ManagerDashboardPageUi)
        self.today_group.setObjectName(u"today_group")
        self.today_layout = QVBoxLayout(self.today_group)
        self.today_layout.setObjectName(u"today_layout")
        self.today_table = QTableWidget(self.today_group)
        self.today_table.setObjectName(u"today_table")
        self.today_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.today_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.today_table.verticalHeader().setVisible(False)

        self.today_layout.addWidget(self.today_table)


        self.bottom_layout.addWidget(self.today_group)

        self.chart_container = QWidget(ManagerDashboardPageUi)
        self.chart_container.setObjectName(u"chart_container")
        self.chart_container.setMinimumWidth(280)
        self.chart_layout = QVBoxLayout(self.chart_container)
        self.chart_layout.setObjectName(u"chart_layout")
        self.chart_layout.setContentsMargins(0, 0, 0, 0)

        self.bottom_layout.addWidget(self.chart_container)


        self.main_layout.addLayout(self.bottom_layout)


        self.retranslateUi(ManagerDashboardPageUi)

        QMetaObject.connectSlotsByName(ManagerDashboardPageUi)
    # setupUi

    def retranslateUi(self, ManagerDashboardPageUi):
        self.header_label.setObjectName(QCoreApplication.translate("ManagerDashboardPageUi", u"pageHeader", None))
        self.date_label.setObjectName(QCoreApplication.translate("ManagerDashboardPageUi", u"dateLabel", None))
        self.reservasi_group.setTitle(QCoreApplication.translate("ManagerDashboardPageUi", u"Statistik Reservasi", None))
        self.card_total.setObjectName(QCoreApplication.translate("ManagerDashboardPageUi", u"dashCard", None))
        self.card_total_value.setText(QCoreApplication.translate("ManagerDashboardPageUi", u"0", None))
        self.card_total_value.setObjectName(QCoreApplication.translate("ManagerDashboardPageUi", u"cardValue", None))
        self.card_total_title.setText(QCoreApplication.translate("ManagerDashboardPageUi", u"Total Reservasi", None))
        self.card_total_title.setObjectName(QCoreApplication.translate("ManagerDashboardPageUi", u"cardTitle", None))
        self.card_hari_ini.setObjectName(QCoreApplication.translate("ManagerDashboardPageUi", u"dashCard", None))
        self.card_hari_ini_value.setText(QCoreApplication.translate("ManagerDashboardPageUi", u"0", None))
        self.card_hari_ini_value.setObjectName(QCoreApplication.translate("ManagerDashboardPageUi", u"cardValue", None))
        self.card_hari_ini_title.setText(QCoreApplication.translate("ManagerDashboardPageUi", u"Reservasi Hari Ini", None))
        self.card_hari_ini_title.setObjectName(QCoreApplication.translate("ManagerDashboardPageUi", u"cardTitle", None))
        self.card_menunggu.setObjectName(QCoreApplication.translate("ManagerDashboardPageUi", u"dashCard", None))
        self.card_menunggu_value.setText(QCoreApplication.translate("ManagerDashboardPageUi", u"0", None))
        self.card_menunggu_value.setObjectName(QCoreApplication.translate("ManagerDashboardPageUi", u"cardValue", None))
        self.card_menunggu_title.setText(QCoreApplication.translate("ManagerDashboardPageUi", u"Menunggu Konfirmasi", None))
        self.card_menunggu_title.setObjectName(QCoreApplication.translate("ManagerDashboardPageUi", u"cardTitle", None))
        self.card_dibatalkan.setObjectName(QCoreApplication.translate("ManagerDashboardPageUi", u"dashCard", None))
        self.card_dibatalkan_value.setText(QCoreApplication.translate("ManagerDashboardPageUi", u"0", None))
        self.card_dibatalkan_value.setObjectName(QCoreApplication.translate("ManagerDashboardPageUi", u"cardValue", None))
        self.card_dibatalkan_title.setText(QCoreApplication.translate("ManagerDashboardPageUi", u"Dibatalkan Bulan Ini", None))
        self.card_dibatalkan_title.setObjectName(QCoreApplication.translate("ManagerDashboardPageUi", u"cardTitle", None))
        self.meja_group.setTitle(QCoreApplication.translate("ManagerDashboardPageUi", u"Statistik Meja", None))
        self.card_meja_tersedia.setObjectName(QCoreApplication.translate("ManagerDashboardPageUi", u"dashCard", None))
        self.card_meja_tersedia_value.setText(QCoreApplication.translate("ManagerDashboardPageUi", u"0", None))
        self.card_meja_tersedia_value.setObjectName(QCoreApplication.translate("ManagerDashboardPageUi", u"cardValue", None))
        self.card_meja_tersedia_title.setText(QCoreApplication.translate("ManagerDashboardPageUi", u"Meja Tersedia", None))
        self.card_meja_tersedia_title.setObjectName(QCoreApplication.translate("ManagerDashboardPageUi", u"cardTitle", None))
        self.card_meja_terisi.setObjectName(QCoreApplication.translate("ManagerDashboardPageUi", u"dashCard", None))
        self.card_meja_terisi_value.setText(QCoreApplication.translate("ManagerDashboardPageUi", u"0", None))
        self.card_meja_terisi_value.setObjectName(QCoreApplication.translate("ManagerDashboardPageUi", u"cardValue", None))
        self.card_meja_terisi_title.setText(QCoreApplication.translate("ManagerDashboardPageUi", u"Meja Terisi", None))
        self.card_meja_terisi_title.setObjectName(QCoreApplication.translate("ManagerDashboardPageUi", u"cardTitle", None))
        self.card_meja_maintenance.setObjectName(QCoreApplication.translate("ManagerDashboardPageUi", u"dashCard", None))
        self.card_meja_maintenance_value.setText(QCoreApplication.translate("ManagerDashboardPageUi", u"0", None))
        self.card_meja_maintenance_value.setObjectName(QCoreApplication.translate("ManagerDashboardPageUi", u"cardValue", None))
        self.card_meja_maintenance_title.setText(QCoreApplication.translate("ManagerDashboardPageUi", u"Maintenance", None))
        self.card_meja_maintenance_title.setObjectName(QCoreApplication.translate("ManagerDashboardPageUi", u"cardTitle", None))
        self.pegawai_group.setTitle(QCoreApplication.translate("ManagerDashboardPageUi", u"Statistik Pegawai", None))
        self.card_total_pegawai.setObjectName(QCoreApplication.translate("ManagerDashboardPageUi", u"dashCard", None))
        self.card_total_pegawai_value.setText(QCoreApplication.translate("ManagerDashboardPageUi", u"0", None))
        self.card_total_pegawai_value.setObjectName(QCoreApplication.translate("ManagerDashboardPageUi", u"cardValue", None))
        self.card_total_pegawai_title.setText(QCoreApplication.translate("ManagerDashboardPageUi", u"Total Pegawai", None))
        self.card_total_pegawai_title.setObjectName(QCoreApplication.translate("ManagerDashboardPageUi", u"cardTitle", None))
        self.card_manajer.setObjectName(QCoreApplication.translate("ManagerDashboardPageUi", u"dashCard", None))
        self.card_manajer_value.setText(QCoreApplication.translate("ManagerDashboardPageUi", u"0", None))
        self.card_manajer_value.setObjectName(QCoreApplication.translate("ManagerDashboardPageUi", u"cardValue", None))
        self.card_manajer_title.setText(QCoreApplication.translate("ManagerDashboardPageUi", u"Manajer", None))
        self.card_manajer_title.setObjectName(QCoreApplication.translate("ManagerDashboardPageUi", u"cardTitle", None))
        self.card_staf.setObjectName(QCoreApplication.translate("ManagerDashboardPageUi", u"dashCard", None))
        self.card_staf_value.setText(QCoreApplication.translate("ManagerDashboardPageUi", u"0", None))
        self.card_staf_value.setObjectName(QCoreApplication.translate("ManagerDashboardPageUi", u"cardValue", None))
        self.card_staf_title.setText(QCoreApplication.translate("ManagerDashboardPageUi", u"Staf", None))
        self.card_staf_title.setObjectName(QCoreApplication.translate("ManagerDashboardPageUi", u"cardTitle", None))
        self.ai_group.setTitle(QCoreApplication.translate("ManagerDashboardPageUi", u"AI Prediksi Jam Ramai", None))
        self.card_ai_jam.setObjectName(QCoreApplication.translate("ManagerDashboardPageUi", u"dashCard", None))
        self.card_ai_jam_value.setText(QCoreApplication.translate("ManagerDashboardPageUi", u"-", None))
        self.card_ai_jam_value.setObjectName(QCoreApplication.translate("ManagerDashboardPageUi", u"cardValue", None))
        self.card_ai_jam_title.setText(QCoreApplication.translate("ManagerDashboardPageUi", u"Jam Ramai Hari Ini", None))
        self.card_ai_jam_title.setObjectName(QCoreApplication.translate("ManagerDashboardPageUi", u"cardTitle", None))
        self.card_ai_tamu.setObjectName(QCoreApplication.translate("ManagerDashboardPageUi", u"dashCard", None))
        self.card_ai_tamu_value.setText(QCoreApplication.translate("ManagerDashboardPageUi", u"0", None))
        self.card_ai_tamu_value.setObjectName(QCoreApplication.translate("ManagerDashboardPageUi", u"cardValue", None))
        self.card_ai_tamu_title.setText(QCoreApplication.translate("ManagerDashboardPageUi", u"Estimasi Tamu", None))
        self.card_ai_tamu_title.setObjectName(QCoreApplication.translate("ManagerDashboardPageUi", u"cardTitle", None))
        self.card_ai_staf.setObjectName(QCoreApplication.translate("ManagerDashboardPageUi", u"dashCard", None))
        self.card_ai_staf_value.setText(QCoreApplication.translate("ManagerDashboardPageUi", u"-", None))
        self.card_ai_staf_value.setObjectName(QCoreApplication.translate("ManagerDashboardPageUi", u"cardValue", None))
        self.card_ai_staf_title.setText(QCoreApplication.translate("ManagerDashboardPageUi", u"Saran Staf", None))
        self.card_ai_staf_title.setObjectName(QCoreApplication.translate("ManagerDashboardPageUi", u"cardTitle", None))
        self.today_group.setTitle(QCoreApplication.translate("ManagerDashboardPageUi", u"Reservasi Hari Ini", None))
        pass
    # retranslateUi

