from PySide6.QtWidgets import (QDialog, QVBoxLayout, QHBoxLayout, QFormLayout,
                               QLineEdit, QSpinBox, QComboBox, QPushButton,
                               QMessageBox, QGroupBox)

import database.database as database


class MejaDialog(QDialog):
    def __init__(self, meja_id=None, parent=None):
        super().__init__(parent)
        self.meja_id = meja_id
        self.is_edit = meja_id is not None
        self.setWindowTitle("Edit Meja" if self.is_edit else "Tambah Meja")
        self.setMinimumWidth(430)
        self.init_ui()
        if self.is_edit:
            self.load_data()

    def init_ui(self):
        layout = QVBoxLayout(self)
        layout.setSpacing(14)

        form_group = QGroupBox("Data Meja")
        form = QFormLayout(form_group)
        form.setVerticalSpacing(12)

        self.nomor_input = QLineEdit()
        self.nomor_input.setPlaceholderText("Contoh: M25")
        self.nomor_input.setMaxLength(10)

        self.kapasitas_input = QSpinBox()
        self.kapasitas_input.setRange(1, 50)
        self.kapasitas_input.setValue(2)
        self.kapasitas_input.valueChanged.connect(self._update_jenis_default)

        self.lantai_input = QSpinBox()
        self.lantai_input.setRange(1, 20)
        self.lantai_input.setValue(1)

        self.jenis_combo = QComboBox()
        self.jenis_combo.addItems(["Kecil", "Besar", "VIP", "Outdoor"])

        self.status_combo = QComboBox()
        self.status_combo.addItems(["Tersedia", "Terisi", "Maintenance"])

        form.addRow("Nomor Meja *", self.nomor_input)
        form.addRow("Kapasitas *", self.kapasitas_input)
        form.addRow("Lantai *", self.lantai_input)
        form.addRow("Jenis *", self.jenis_combo)
        form.addRow("Status *", self.status_combo)

        btn_row = QHBoxLayout()
        cancel_btn = QPushButton("Batal")
        cancel_btn.clicked.connect(self.reject)

        save_btn = QPushButton("Simpan Meja")
        save_btn.setObjectName("primaryButton")
        save_btn.clicked.connect(self.save)

        btn_row.addStretch()
        btn_row.addWidget(cancel_btn)
        btn_row.addWidget(save_btn)

        layout.addWidget(form_group)
        layout.addLayout(btn_row)

    def _update_jenis_default(self):
        if not self.is_edit:
            self.jenis_combo.setCurrentText("Besar" if self.kapasitas_input.value() > 4 else "Kecil")

    def load_data(self):
        data = database.get_meja_by_id(self.meja_id)
        if not data:
            return
        self.nomor_input.setText(data['nomor_meja'])
        self.kapasitas_input.setValue(data['kapasitas'])
        self.lantai_input.setValue(data['lantai'])
        self.jenis_combo.setCurrentText(data['jenis'])
        self.status_combo.setCurrentText(data['status'])

    def save(self):
        nomor = self.nomor_input.text().strip().upper()
        kapasitas = self.kapasitas_input.value()
        lantai = self.lantai_input.value()
        jenis = self.jenis_combo.currentText()
        status = self.status_combo.currentText()

        if not nomor:
            QMessageBox.warning(self, "Validasi", "Nomor meja tidak boleh kosong.")
            self.nomor_input.setFocus()
            return
        if len(nomor) < 2:
            QMessageBox.warning(self, "Validasi", "Nomor meja minimal 2 karakter.")
            self.nomor_input.setFocus()
            return
        if kapasitas < 1:
            QMessageBox.warning(self, "Validasi", "Kapasitas meja harus lebih dari 0.")
            return

        if self.is_edit:
            ok, err = database.edit_meja(self.meja_id, nomor, kapasitas, lantai, jenis, status)
        else:
            ok, err = database.tambah_meja(nomor, kapasitas, lantai, jenis, status)

        if ok:
            QMessageBox.information(self, "Sukses", "Data meja berhasil disimpan.")
            self.accept()
        else:
            if "UNIQUE" in str(err):
                QMessageBox.critical(self, "Error", "Nomor meja sudah digunakan.")
            else:
                QMessageBox.critical(self, "Error", f"Gagal menyimpan: {err}")
