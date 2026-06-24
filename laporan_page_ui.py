# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'laporan_page.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractSpinBox, QApplication, QComboBox,
    QDateEdit, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_LaporanPageUi(object):
    def setupUi(self, LaporanPageUi):
        if not LaporanPageUi.objectName():
            LaporanPageUi.setObjectName(u"LaporanPageUi")
        self.main_layout = QVBoxLayout(LaporanPageUi)
        self.main_layout.setSpacing(18)
        self.main_layout.setObjectName(u"main_layout")
        self.main_layout.setContentsMargins(28, 24, 28, 24)
        self.title_label = QLabel(LaporanPageUi)
        self.title_label.setObjectName(u"title_label")

        self.main_layout.addWidget(self.title_label)

        self.filter_group = QGroupBox(LaporanPageUi)
        self.filter_group.setObjectName(u"filter_group")
        self.filter_group_layout = QVBoxLayout(self.filter_group)
        self.filter_group_layout.setSpacing(14)
        self.filter_group_layout.setObjectName(u"filter_group_layout")
        self.filter_group_layout.setContentsMargins(18, 22, 18, 16)
        self.filter_layout = QHBoxLayout()
        self.filter_layout.setSpacing(14)
        self.filter_layout.setObjectName(u"filter_layout")
        self.from_field = QWidget(self.filter_group)
        self.from_field.setObjectName(u"from_field")
        self.from_layout = QVBoxLayout(self.from_field)
        self.from_layout.setSpacing(6)
        self.from_layout.setObjectName(u"from_layout")
        self.from_layout.setContentsMargins(0, 0, 0, 0)
        self.date_from_label = QLabel(self.from_field)
        self.date_from_label.setObjectName(u"date_from_label")

        self.from_layout.addWidget(self.date_from_label)

        self.date_from = QDateEdit(self.from_field)
        self.date_from.setObjectName(u"date_from")
        self.date_from.setCalendarPopup(True)
        self.date_from.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.date_from.setKeyboardTracking(False)
        self.date_from.setMinimumWidth(156)
        self.date_from.setMinimumHeight(40)

        self.from_layout.addWidget(self.date_from)


        self.filter_layout.addWidget(self.from_field)

        self.to_field = QWidget(self.filter_group)
        self.to_field.setObjectName(u"to_field")
        self.to_layout = QVBoxLayout(self.to_field)
        self.to_layout.setSpacing(6)
        self.to_layout.setObjectName(u"to_layout")
        self.to_layout.setContentsMargins(0, 0, 0, 0)
        self.date_to_label = QLabel(self.to_field)
        self.date_to_label.setObjectName(u"date_to_label")

        self.to_layout.addWidget(self.date_to_label)

        self.date_to = QDateEdit(self.to_field)
        self.date_to.setObjectName(u"date_to")
        self.date_to.setCalendarPopup(True)
        self.date_to.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.date_to.setKeyboardTracking(False)
        self.date_to.setMinimumWidth(156)
        self.date_to.setMinimumHeight(40)

        self.to_layout.addWidget(self.date_to)


        self.filter_layout.addWidget(self.to_field)

        self.status_field = QWidget(self.filter_group)
        self.status_field.setObjectName(u"status_field")
        self.status_layout = QVBoxLayout(self.status_field)
        self.status_layout.setSpacing(6)
        self.status_layout.setObjectName(u"status_layout")
        self.status_layout.setContentsMargins(0, 0, 0, 0)
        self.status_label = QLabel(self.status_field)
        self.status_label.setObjectName(u"status_label")

        self.status_layout.addWidget(self.status_label)

        self.filter_status = QComboBox(self.status_field)
        self.filter_status.setObjectName(u"filter_status")
        self.filter_status.setMinimumWidth(176)
        self.filter_status.setMinimumHeight(40)

        self.status_layout.addWidget(self.filter_status)


        self.filter_layout.addWidget(self.status_field)

        self.apply_field = QWidget(self.filter_group)
        self.apply_field.setObjectName(u"apply_field")
        self.apply_layout = QVBoxLayout(self.apply_field)
        self.apply_layout.setSpacing(6)
        self.apply_layout.setObjectName(u"apply_layout")
        self.apply_layout.setContentsMargins(0, 0, 0, 0)
        self.apply_spacer_label = QLabel(self.apply_field)
        self.apply_spacer_label.setObjectName(u"apply_spacer_label")

        self.apply_layout.addWidget(self.apply_spacer_label)

        self.apply_btn = QPushButton(self.apply_field)
        self.apply_btn.setObjectName(u"apply_btn")
        self.apply_btn.setMinimumHeight(40)
        self.apply_btn.setMinimumWidth(116)
        self.apply_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.apply_layout.addWidget(self.apply_btn)


        self.filter_layout.addWidget(self.apply_field)

        self.filter_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.filter_layout.addItem(self.filter_spacer)


        self.filter_group_layout.addLayout(self.filter_layout)

        self.filter_footer_layout = QHBoxLayout()
        self.filter_footer_layout.setSpacing(12)
        self.filter_footer_layout.setObjectName(u"filter_footer_layout")
        self.filter_footer_layout.setContentsMargins(-1, 2, -1, -1)
        self.filter_summary = QLabel(self.filter_group)
        self.filter_summary.setObjectName(u"filter_summary")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filter_summary.sizePolicy().hasHeightForWidth())
        self.filter_summary.setSizePolicy(sizePolicy)

        self.filter_footer_layout.addWidget(self.filter_summary)

        self.export_field = QWidget(self.filter_group)
        self.export_field.setObjectName(u"export_field")
        self.export_layout = QHBoxLayout(self.export_field)
        self.export_layout.setSpacing(8)
        self.export_layout.setObjectName(u"export_layout")
        self.export_layout.setContentsMargins(10, 8, 10, 8)
        self.export_label = QLabel(self.export_field)
        self.export_label.setObjectName(u"export_label")

        self.export_layout.addWidget(self.export_label)

        self.export_btn = QPushButton(self.export_field)
        self.export_btn.setObjectName(u"export_btn")
        self.export_btn.setMinimumHeight(34)
        self.export_btn.setMinimumWidth(104)
        self.export_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.export_layout.addWidget(self.export_btn)

        self.export_pdf_btn = QPushButton(self.export_field)
        self.export_pdf_btn.setObjectName(u"export_pdf_btn")
        self.export_pdf_btn.setMinimumHeight(34)
        self.export_pdf_btn.setMinimumWidth(104)
        self.export_pdf_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.export_layout.addWidget(self.export_pdf_btn)


        self.filter_footer_layout.addWidget(self.export_field)


        self.filter_group_layout.addLayout(self.filter_footer_layout)


        self.main_layout.addWidget(self.filter_group)

        self.ai_group = QGroupBox(LaporanPageUi)
        self.ai_group.setObjectName(u"ai_group")
        self.ai_layout = QVBoxLayout(self.ai_group)
        self.ai_layout.setObjectName(u"ai_layout")
        self.ai_layout.setContentsMargins(18, 14, 18, 14)
        self.ai_summary = QLabel(self.ai_group)
        self.ai_summary.setObjectName(u"ai_summary")
        self.ai_summary.setWordWrap(True)

        self.ai_layout.addWidget(self.ai_summary)


        self.main_layout.addWidget(self.ai_group)

        self.content_layout = QHBoxLayout()
        self.content_layout.setSpacing(16)
        self.content_layout.setObjectName(u"content_layout")
        self.table = QTableWidget(LaporanPageUi)
        self.table.setObjectName(u"table")
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.setSortingEnabled(True)
        self.table.verticalHeader().setVisible(False)

        self.content_layout.addWidget(self.table)

        self.chart_container = QWidget(LaporanPageUi)
        self.chart_container.setObjectName(u"chart_container")
        self.chart_container.setMinimumWidth(320)
        self.chart_layout = QVBoxLayout(self.chart_container)
        self.chart_layout.setObjectName(u"chart_layout")
        self.chart_layout.setContentsMargins(0, 0, 0, 0)

        self.content_layout.addWidget(self.chart_container)


        self.main_layout.addLayout(self.content_layout)


        self.retranslateUi(LaporanPageUi)

        QMetaObject.connectSlotsByName(LaporanPageUi)
    # setupUi

    def retranslateUi(self, LaporanPageUi):
        self.title_label.setText(QCoreApplication.translate("LaporanPageUi", u"Laporan & Statistik", None))
        self.title_label.setObjectName(QCoreApplication.translate("LaporanPageUi", u"pageHeader", None))
        self.filter_group.setTitle(QCoreApplication.translate("LaporanPageUi", u"Filter Data", None))
        self.filter_group.setObjectName(QCoreApplication.translate("LaporanPageUi", u"reportFilterGroup", None))
        self.from_field.setObjectName(QCoreApplication.translate("LaporanPageUi", u"reportFilterField", None))
        self.date_from_label.setText(QCoreApplication.translate("LaporanPageUi", u"Dari Tanggal", None))
        self.date_from_label.setObjectName(QCoreApplication.translate("LaporanPageUi", u"reportFilterLabel", None))
        self.date_from.setDisplayFormat(QCoreApplication.translate("LaporanPageUi", u"dd MMM yyyy", None))
        self.date_from.setObjectName(QCoreApplication.translate("LaporanPageUi", u"reportDateInput", None))
        self.to_field.setObjectName(QCoreApplication.translate("LaporanPageUi", u"reportFilterField", None))
        self.date_to_label.setText(QCoreApplication.translate("LaporanPageUi", u"Sampai Tanggal", None))
        self.date_to_label.setObjectName(QCoreApplication.translate("LaporanPageUi", u"reportFilterLabel", None))
        self.date_to.setDisplayFormat(QCoreApplication.translate("LaporanPageUi", u"dd MMM yyyy", None))
        self.date_to.setObjectName(QCoreApplication.translate("LaporanPageUi", u"reportDateInput", None))
        self.status_field.setObjectName(QCoreApplication.translate("LaporanPageUi", u"reportFilterField", None))
        self.status_label.setText(QCoreApplication.translate("LaporanPageUi", u"Status Reservasi", None))
        self.status_label.setObjectName(QCoreApplication.translate("LaporanPageUi", u"reportFilterLabel", None))
        self.filter_status.setObjectName(QCoreApplication.translate("LaporanPageUi", u"reportStatusFilter", None))
        self.apply_field.setObjectName(QCoreApplication.translate("LaporanPageUi", u"reportFilterField", None))
        self.apply_spacer_label.setText("")
        self.apply_spacer_label.setObjectName(QCoreApplication.translate("LaporanPageUi", u"reportFilterLabel", None))
        self.apply_btn.setText(QCoreApplication.translate("LaporanPageUi", u"Terapkan", None))
        self.apply_btn.setObjectName(QCoreApplication.translate("LaporanPageUi", u"reportApplyButton", None))
        self.filter_summary.setObjectName(QCoreApplication.translate("LaporanPageUi", u"reportFilterSummary", None))
        self.export_field.setObjectName(QCoreApplication.translate("LaporanPageUi", u"reportExportBar", None))
        self.export_label.setText(QCoreApplication.translate("LaporanPageUi", u"Export data:", None))
        self.export_label.setObjectName(QCoreApplication.translate("LaporanPageUi", u"reportExportLabel", None))
        self.export_btn.setText(QCoreApplication.translate("LaporanPageUi", u"Export CSV", None))
        self.export_btn.setObjectName(QCoreApplication.translate("LaporanPageUi", u"primaryButton", None))
        self.export_pdf_btn.setText(QCoreApplication.translate("LaporanPageUi", u"Export PDF", None))
        self.export_pdf_btn.setObjectName(QCoreApplication.translate("LaporanPageUi", u"successButton", None))
        self.ai_group.setTitle(QCoreApplication.translate("LaporanPageUi", u"Analisis AI", None))
        self.ai_summary.setObjectName(QCoreApplication.translate("LaporanPageUi", u"reportFilterSummary", None))
        pass
    # retranslateUi

