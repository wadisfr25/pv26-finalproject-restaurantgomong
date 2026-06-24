# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'meja_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFormLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
    QVBoxLayout, QWidget)

class Ui_MejaDialog(object):
    def setupUi(self, MejaDialog):
        if not MejaDialog.objectName():
            MejaDialog.setObjectName(u"MejaDialog")
        MejaDialog.setMinimumWidth(430)
        self.mainLayout = QVBoxLayout(MejaDialog)
        self.mainLayout.setSpacing(14)
        self.mainLayout.setObjectName(u"mainLayout")
        self.form_group = QGroupBox(MejaDialog)
        self.form_group.setObjectName(u"form_group")
        self.formLayout = QFormLayout(self.form_group)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setVerticalSpacing(12)
        self.nomor_label = QLabel(self.form_group)
        self.nomor_label.setObjectName(u"nomor_label")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.nomor_label)

        self.nomor_input = QLineEdit(self.form_group)
        self.nomor_input.setObjectName(u"nomor_input")
        self.nomor_input.setMaxLength(10)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.nomor_input)

        self.kapasitas_label = QLabel(self.form_group)
        self.kapasitas_label.setObjectName(u"kapasitas_label")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.kapasitas_label)

        self.kapasitas_input = QSpinBox(self.form_group)
        self.kapasitas_input.setObjectName(u"kapasitas_input")
        self.kapasitas_input.setMinimum(1)
        self.kapasitas_input.setMaximum(50)
        self.kapasitas_input.setValue(2)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.kapasitas_input)

        self.lantai_label = QLabel(self.form_group)
        self.lantai_label.setObjectName(u"lantai_label")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.lantai_label)

        self.lantai_input = QSpinBox(self.form_group)
        self.lantai_input.setObjectName(u"lantai_input")
        self.lantai_input.setMinimum(1)
        self.lantai_input.setMaximum(20)
        self.lantai_input.setValue(1)

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.lantai_input)

        self.jenis_label = QLabel(self.form_group)
        self.jenis_label.setObjectName(u"jenis_label")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.jenis_label)

        self.jenis_combo = QComboBox(self.form_group)
        self.jenis_combo.setObjectName(u"jenis_combo")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.jenis_combo)

        self.status_label = QLabel(self.form_group)
        self.status_label.setObjectName(u"status_label")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.status_label)

        self.status_combo = QComboBox(self.form_group)
        self.status_combo.setObjectName(u"status_combo")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.status_combo)


        self.mainLayout.addWidget(self.form_group)

        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.setObjectName(u"buttonLayout")
        self.buttonSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.buttonLayout.addItem(self.buttonSpacer)

        self.cancel_btn = QPushButton(MejaDialog)
        self.cancel_btn.setObjectName(u"cancel_btn")

        self.buttonLayout.addWidget(self.cancel_btn)

        self.save_btn = QPushButton(MejaDialog)
        self.save_btn.setObjectName(u"save_btn")

        self.buttonLayout.addWidget(self.save_btn)


        self.mainLayout.addLayout(self.buttonLayout)


        self.retranslateUi(MejaDialog)

        QMetaObject.connectSlotsByName(MejaDialog)
    # setupUi

    def retranslateUi(self, MejaDialog):
        MejaDialog.setWindowTitle(QCoreApplication.translate("MejaDialog", u"Meja", None))
        self.form_group.setTitle(QCoreApplication.translate("MejaDialog", u"Data Meja", None))
        self.nomor_label.setText(QCoreApplication.translate("MejaDialog", u"Nomor Meja *", None))
        self.nomor_input.setPlaceholderText(QCoreApplication.translate("MejaDialog", u"Contoh: M25", None))
        self.kapasitas_label.setText(QCoreApplication.translate("MejaDialog", u"Kapasitas *", None))
        self.lantai_label.setText(QCoreApplication.translate("MejaDialog", u"Lantai *", None))
        self.jenis_label.setText(QCoreApplication.translate("MejaDialog", u"Jenis *", None))
        self.status_label.setText(QCoreApplication.translate("MejaDialog", u"Status *", None))
        self.cancel_btn.setText(QCoreApplication.translate("MejaDialog", u"Batal", None))
        self.save_btn.setText(QCoreApplication.translate("MejaDialog", u"Simpan Meja", None))
    # retranslateUi

