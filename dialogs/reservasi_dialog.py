from PySide6.QtCore import QDate
from PySide6.QtWidgets import QDialog, QMessageBox

import database.database as database
from ui.ui_reservasi_dialog import Ui_ReservasiDialog

JAM_OPERASIONAL = [
    "11:00", "11:30", "12:00", "12:30", "13:00", "13:30",
    "17:00", "17:30", "18:00", "18:30", "19:00", "19:30", "20:00", "20:30",
]

class ReservasiDialog(QDialog, Ui_ReservasiDialog):
    def __init__(self, reservasi_id=None, parent=None):
        super().__init__(parent)
        self.reservasi_id = reservasi_id
        self.is_edit = reservasi_id is not None
        self.init_ui()
        if self.is_edit:
            self.load_data()
        else:
            self._update_meja()

    def init_ui(self):
        self.setupUi(self)
        self.setWindowTitle("Edit Reservasi" if self.is_edit else "Tambah Reservasi Baru")
        self.setMinimumWidth(520)

        self.tanggal_input.setDate(QDate.currentDate())
        self.tanggal_input.setMinimumDate(QDate.currentDate())
        self.waktu_combo.addItems(JAM_OPERASIONAL)
        self.status_combo.addItems(["Menunggu", "Dikonfirmasi", "Selesai", "Dibatalkan"])
        self.save_btn.setObjectName("primaryButton")

        self.cancel_btn.clicked.connect(self.reject)
        self.save_btn.clicked.connect(self.save)
        self.jumlah_input.valueChanged.connect(self._update_meja)
        self.tanggal_input.dateChanged.connect(self._update_meja)
        self.waktu_combo.currentTextChanged.connect(self._update_meja)

    def _update_meja(self):
        jumlah = self.jumlah_input.value()
        tanggal = self.tanggal_input.date().toString("yyyy-MM-dd")
        waktu = self.waktu_combo.currentText()
        tables = database.get_recommended_tables(jumlah, tanggal, waktu, self.reservasi_id)

        self.meja_combo.clear()
        self.meja_combo.addItem("-- Pilih meja (opsional) --", None)
        for t in tables:
            self.meja_combo.addItem(f"{t['nomor_meja']}  (kapasitas {t['kapasitas']} orang)", t["id"])

        if not tables:
            self.meja_combo.addItem("Tidak ada meja tersedia di jam ini", None)
            self.info_meja_lbl.setText("")
            return

        best_table = tables[0]
        self.meja_combo.setCurrentIndex(1)
        self.info_meja_lbl.setText(
            "Rekomendasi AI: "
            f"{best_table['nomor_meja']} karena sisa kursinya {best_table['sisa_kursi']} "
            f"dan riwayat pemakaiannya {best_table['jumlah_pemakaian']} kali."
        )

    def load_data(self):
        conn = database.get_db_connection()
        d = conn.execute("SELECT * FROM reservasi WHERE id = ?", (self.reservasi_id,)).fetchone()
        conn.close()
        if not d:
            return

        self.nama_input.setText(d["nama_tamu"])
        self.telepon_input.setText(d["no_telepon"])
        self.jumlah_input.setValue(d["jumlah_tamu"])
        self.tanggal_input.setDate(QDate.fromString(d["tanggal"], "yyyy-MM-dd"))
        self.waktu_combo.setCurrentText(d["waktu"])
        self.status_combo.setCurrentText(d["status"])
        self.catatan_input.setPlainText(d["catatan"] or "")
        self._update_meja()

        if d["meja_id"]:
            for i in range(self.meja_combo.count()):
                if self.meja_combo.itemData(i) == d["meja_id"]:
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
            QMessageBox.warning(
                self, "Validasi", "Nomor telepon tidak valid (min. 10 digit angka)."
            )
            self.telepon_input.setFocus()
            return
        if meja_id is None:
            QMessageBox.warning(self, "Validasi", "Meja wajib dipilih untuk reservasi.")
            self.meja_combo.setFocus()
            return

        ok, err = database.simpan_reservasi(
            nama, telepon, jumlah, tanggal, waktu,
            meja_id, status, catatan,
            reservasi_id=self.reservasi_id,
        )
        if ok:
            QMessageBox.information(self, "Sukses", "Reservasi berhasil disimpan!")
            self.accept()
        else:
            QMessageBox.critical(self, "Error", f"Gagal menyimpan: {err}")
