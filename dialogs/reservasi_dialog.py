from PySide6.QtWidgets import (QDialog, QVBoxLayout, QHBoxLayout, QFormLayout,
                               QLabel, QLineEdit, QSpinBox, QComboBox, QDateEdit,
                               QTextEdit, QPushButton, QMessageBox, QGroupBox)
from PySide6.QtCore import Qt, QDate
import database.database as database

JAM_OPERASIONAL = [
    "11:00", "11:30", "12:00", "12:30", "13:00", "13:30",
    "17:00", "17:30", "18:00", "18:30", "19:00", "19:30", "20:00", "20:30",
]


class ReservasiDialog(QDialog):
    def __init__(self, reservasi_id=None, parent=None):
        super().__init__(parent)
        self.reservasi_id = reservasi_id
        self.is_edit = reservasi_id is not None
        self.setWindowTitle("Edit Reservasi" if self.is_edit else "Tambah Reservasi Baru")
        self.setMinimumWidth(520)
        self.init_ui()
        if self.is_edit:
            self.load_data()
        else:
            self._update_meja()

    def init_ui(self):
        layout = QVBoxLayout(self)
        layout.setSpacing(15)

        # ── Informasi Tamu ──────────────────────────────────────────
        tamu_grp = QGroupBox("👤  Informasi Tamu")
        tamu_lay = QFormLayout(tamu_grp)
        tamu_lay.setVerticalSpacing(12)

        self.nama_input = QLineEdit()
        self.nama_input.setPlaceholderText("Masukkan nama lengkap tamu")
        self.nama_input.setMaxLength(100)

        self.telepon_input = QLineEdit()
        self.telepon_input.setPlaceholderText("08xxxxxxxxxx")
        self.telepon_input.setMaxLength(15)

        self.jumlah_input = QSpinBox()
        self.jumlah_input.setRange(1, 8)
        self.jumlah_input.setValue(2)
        self.jumlah_input.setSuffix("  orang")
        self.jumlah_input.valueChanged.connect(self._update_meja)

        tamu_lay.addRow("Nama Tamu *", self.nama_input)
        tamu_lay.addRow("No. Telepon *", self.telepon_input)
        tamu_lay.addRow("Jumlah Tamu *", self.jumlah_input)

        # ── Detail Reservasi ─────────────────────────────────────────
        res_grp = QGroupBox("🗓️  Detail Reservasi")
        res_lay = QFormLayout(res_grp)
        res_lay.setVerticalSpacing(12)

        self.tanggal_input = QDateEdit(QDate.currentDate())
        self.tanggal_input.setMinimumDate(QDate.currentDate())
        self.tanggal_input.setCalendarPopup(True)
        self.tanggal_input.dateChanged.connect(self._update_meja)

        self.waktu_combo = QComboBox()
        self.waktu_combo.addItems(JAM_OPERASIONAL)
        self.waktu_combo.currentTextChanged.connect(self._update_meja)

        self.meja_combo = QComboBox()

        self.status_combo = QComboBox()
        self.status_combo.addItems(
            ["Menunggu", "Dikonfirmasi", "Duduk", "Selesai", "Dibatalkan"]
        )

        self.catatan_input = QTextEdit()
        self.catatan_input.setPlaceholderText(
            "Catatan khusus: alergi makanan, dekorasi, permintaan meja window seat, dll."
        )
        self.catatan_input.setMaximumHeight(75)

        # Info otomatis
        self.info_meja_lbl = QLabel()
        self.info_meja_lbl.setStyleSheet(
            "color: #1A5276; font-size: 10px; font-style: italic;"
        )

        res_lay.addRow("Tanggal *", self.tanggal_input)
        res_lay.addRow("Jam *", self.waktu_combo)
        res_lay.addRow("Pilih Meja", self.meja_combo)
        res_lay.addRow("", self.info_meja_lbl)
        res_lay.addRow("Status", self.status_combo)
        res_lay.addRow("Catatan", self.catatan_input)

        # ── Tombol ───────────────────────────────────────────────────
        btn_row = QHBoxLayout()
        cancel_btn = QPushButton("Batal")
        cancel_btn.clicked.connect(self.reject)

        save_btn = QPushButton("💾  Simpan Reservasi")
        save_btn.setObjectName("primaryButton")
        save_btn.clicked.connect(self.save)

        btn_row.addStretch()
        btn_row.addWidget(cancel_btn)
        btn_row.addWidget(save_btn)

        layout.addWidget(tamu_grp)
        layout.addWidget(res_grp)
        layout.addLayout(btn_row)

    def _update_meja(self):
        jumlah = self.jumlah_input.value()
        tanggal = self.tanggal_input.date().toString("yyyy-MM-dd")
        waktu = self.waktu_combo.currentText()
        tables = database.get_available_tables(jumlah, tanggal, waktu, self.reservasi_id)

        self.meja_combo.clear()
        self.meja_combo.addItem("— Pilih meja (opsional) —", None)
        for t in tables:
            self.meja_combo.addItem(f"{t['nomor_meja']}  (kapasitas {t['kapasitas']} orang)", t['id'])
        if not tables:
            self.meja_combo.addItem("⚠️  Tidak ada meja tersedia di jam ini", None)
            self.info_meja_lbl.setText("")
        else:
            self.info_meja_lbl.setText(
                "ℹ️  Meja yang dipilih akan otomatis ditandai Terisi setelah disimpan."
            )

    def load_data(self):
        conn = database.get_db_connection()
        d = conn.execute("SELECT * FROM reservasi WHERE id = ?", (self.reservasi_id,)).fetchone()
        conn.close()
        if not d:
            return
        self.nama_input.setText(d['nama_tamu'])
        self.telepon_input.setText(d['no_telepon'])
        self.jumlah_input.setValue(d['jumlah_tamu'])
        self.tanggal_input.setDate(QDate.fromString(d['tanggal'], "yyyy-MM-dd"))
        self.waktu_combo.setCurrentText(d['waktu'])
        self.status_combo.setCurrentText(d['status'])
        self.catatan_input.setPlainText(d['catatan'] or "")
        self._update_meja()
        if d['meja_id']:
            for i in range(self.meja_combo.count()):
                if self.meja_combo.itemData(i) == d['meja_id']:
                    self.meja_combo.setCurrentIndex(i)
                    break

    def save(self):
        nama = self.nama_input.text().strip()
        telepon = self.telepon_input.text().strip()
        jumlah = self.jumlah_input.value()
        tanggal = self.tanggal_input.date().toString("yyyy-MM-dd")
        waktu = self.waktu_combo.currentText()
        meja_id = self.meja_combo.currentData()
        status = self.status_combo.currentText()
        catatan = self.catatan_input.toPlainText().strip()

        if not nama:
            QMessageBox.warning(self, "Validasi", "Nama tamu tidak boleh kosong.")
            self.nama_input.setFocus()
            return
        if len(nama) < 2:
            QMessageBox.warning(self, "Validasi", "Nama tamu minimal 2 karakter.")
            return
        if not telepon:
            QMessageBox.warning(self, "Validasi", "Nomor telepon tidak boleh kosong.")
            self.telepon_input.setFocus()
            return
        if not telepon.isdigit() or len(telepon) < 10:
            QMessageBox.warning(self, "Validasi",
                                "Nomor telepon tidak valid (min. 10 digit angka).")
            self.telepon_input.setFocus()
            return
        if meja_id is None:
            QMessageBox.warning(self, "Validasi", "Meja wajib dipilih untuk reservasi.")
            self.meja_combo.setFocus()
            return

        ok, err = database.simpan_reservasi(
            nama, telepon, jumlah, tanggal, waktu,
            meja_id, status, catatan,
            reservasi_id=self.reservasi_id
        )
        if ok:
            QMessageBox.information(self, "Sukses", "✅  Reservasi berhasil disimpan!")
            self.accept()
        else:
            QMessageBox.critical(self, "Error", f"Gagal menyimpan: {err}")
