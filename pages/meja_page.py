from PySide6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel,
                               QPushButton, QFrame, QGridLayout, QScrollArea,
                               QGroupBox, QMessageBox, QLineEdit, QComboBox,
                               QDialog)
from PySide6.QtCore import Qt

import database.database as database
from dialogs.meja_dialog import MejaDialog


class MejaCard(QFrame):
    def __init__(self, meja, callback):
        super().__init__()
        self.meja_id = meja['id']
        self.callback = callback
        self.setFrameShape(QFrame.NoFrame)
        self.setCursor(Qt.PointingHandCursor)
        self.setMinimumSize(132, 104)
        self.setMaximumHeight(112)

        status_color = {
            'Tersedia': ('#1E8449', '#EAF7EF'),
            'Terisi': ('#C0392B', '#FDEDEC'),
            'Dibereskan': ('#2874A6', '#EBF5FB'),
            'Maintenance': ('#B9770E', '#FEF5E7'),
        }
        border, bg = status_color.get(meja['status'], ('#7F8C8D', '#F2F3F4'))

        self.setStyleSheet(f"""
            MejaCard {{
                background: {bg};
                border: 1.5px solid {border};
                border-radius: 10px;
            }}
            MejaCard QLabel {{
                background: transparent;
            }}
            MejaCard:hover {{
                background: white;
                border: 2px solid {border};
            }}
        """)

        lay = QVBoxLayout(self)
        lay.setAlignment(Qt.AlignCenter)
        lay.setContentsMargins(8, 8, 8, 8)
        lay.setSpacing(3)

        no = QLabel(meja['nomor_meja'])
        no.setAlignment(Qt.AlignCenter)
        no.setStyleSheet("font-weight: bold; font-size: 15px; color: #1E2D3D;")

        meta = QLabel(f"{meja['kapasitas']} orang | Lantai {meja['lantai']}")
        meta.setAlignment(Qt.AlignCenter)
        meta.setStyleSheet("font-size: 10px; color: #566573;")

        jenis = QLabel(meja['jenis'])
        jenis.setAlignment(Qt.AlignCenter)
        jenis.setStyleSheet("font-size: 10px; color: #566573;")

        status = QLabel(meja['status'])
        status.setAlignment(Qt.AlignCenter)
        status.setStyleSheet(f"color: {border}; font-size: 10px; font-weight: bold;")

        lay.addWidget(no)
        lay.addWidget(meta)
        lay.addWidget(jenis)
        lay.addWidget(status)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.callback(self.meja_id)


class MejaPage(QWidget):
    def __init__(self):
        super().__init__()
        self.all_data = []
        self.init_ui()
        self.refresh()

    def init_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(25, 20, 25, 20)
        layout.setSpacing(14)

        hdr = QHBoxLayout()
        hdr.setSpacing(14)

        title_col = QVBoxLayout()
        title_col.setSpacing(3)
        title = QLabel("Manajemen Meja")
        title.setObjectName("pageHeader")

        subtitle = QLabel("Atur ketersediaan, kapasitas, dan status meja restoran.")
        subtitle.setObjectName("pageSubtitle")
        title_col.addWidget(title)
        title_col.addWidget(subtitle)

        add_btn = QPushButton("+  Tambah Meja")
        add_btn.setObjectName("primaryButton")
        add_btn.setFixedHeight(38)
        add_btn.clicked.connect(self.tambah_meja)

        refresh_btn = QPushButton("Refresh")
        refresh_btn.setObjectName("secondaryButton")
        refresh_btn.setFixedHeight(38)
        refresh_btn.clicked.connect(self.refresh)

        hdr.addLayout(title_col)
        hdr.addStretch()
        hdr.addWidget(add_btn)
        hdr.addWidget(refresh_btn)
        layout.addLayout(hdr)

        info_lbl = QLabel(
            "Status meja otomatis mengikuti reservasi aktif. Klik kartu meja untuk edit, hapus, atau ubah status maintenance."
        )
        info_lbl.setObjectName("infoBanner")
        info_lbl.setWordWrap(True)
        layout.addWidget(info_lbl)

        toolbar = QFrame()
        toolbar.setObjectName("mejaToolbar")
        toolbar.setFrameShape(QFrame.NoFrame)
        toolbar_layout = QVBoxLayout(toolbar)
        toolbar_layout.setContentsMargins(14, 12, 14, 12)
        toolbar_layout.setSpacing(10)

        filter_row = QHBoxLayout()
        filter_row.setSpacing(10)
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Cari nomor meja atau jenis...")
        self.search_input.textChanged.connect(self.apply_filter)

        self.filter_status = QComboBox()
        self.filter_status.addItems(["Semua Status", "Tersedia", "Terisi", "Dibereskan", "Maintenance"])
        self.filter_status.currentTextChanged.connect(self.apply_filter)

        self.filter_kapasitas = QComboBox()
        self.filter_kapasitas.addItems(["Semua Kapasitas", "1-2 orang", "3-4 orang", "5-8 orang", "> 8 orang"])
        self.filter_kapasitas.currentTextChanged.connect(self.apply_filter)

        self.sort_combo = QComboBox()
        self.sort_combo.addItems(["Urut: Kapasitas", "Urut: Nomor Meja", "Urut: Status", "Urut: Lantai"])
        self.sort_combo.currentTextChanged.connect(self.apply_filter)

        filter_row.addWidget(self.search_input, 3)
        filter_row.addWidget(self.filter_status, 1)
        filter_row.addWidget(self.filter_kapasitas, 1)
        filter_row.addWidget(self.sort_combo, 1)
        toolbar_layout.addLayout(filter_row)

        legend = QHBoxLayout()
        legend.setSpacing(8)
        for label, color in [
            ("Tersedia", "#1E8449"),
            ("Terisi", "#C0392B"),
            ("Dibereskan", "#2874A6"),
            ("Maintenance", "#B9770E"),
        ]:
            lbl = QLabel(f"● {label}")
            lbl.setStyleSheet(f"color: {color}; font-weight: bold; font-size: 12px;")
            legend.addWidget(lbl)
            legend.addSpacing(16)

        self.summary_lbl = QLabel()
        self.summary_lbl.setObjectName("mejaSummary")
        legend.addStretch()
        legend.addWidget(self.summary_lbl)
        toolbar_layout.addLayout(legend)
        layout.addWidget(toolbar)

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(QFrame.NoFrame)
        self.floor_container = QWidget()
        self.floor_layout = QVBoxLayout(self.floor_container)
        self.floor_layout.setSpacing(16)
        scroll.setWidget(self.floor_container)
        layout.addWidget(scroll)

    def refresh(self):
        self.all_data = database.get_all_meja()
        self.apply_filter()

    def apply_filter(self):
        while self.floor_layout.count():
            child = self.floor_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

        tables = self._filtered_sorted_data()
        self._update_summary(tables)

        if not tables:
            empty = QLabel("Tidak ada meja yang sesuai dengan pencarian/filter.")
            empty.setAlignment(Qt.AlignCenter)
            empty.setObjectName("emptyState")
            self.floor_layout.addWidget(empty)
            self.floor_layout.addStretch()
            return

        groups = {}
        for t in tables:
            cap = t['kapasitas']
            groups.setdefault(cap, []).append(t)

        for cap in sorted(groups.keys()):
            meja_list = groups[cap]
            tersedia_grp = sum(1 for m in meja_list if m['status'] == 'Tersedia')
            terisi_grp = sum(1 for m in meja_list if m['status'] == 'Terisi')
            dibereskan_grp = sum(1 for m in meja_list if m['status'] == 'Dibereskan')

            group = QGroupBox(
                f"Meja {cap} Orang - {len(meja_list)} meja "
                f"({tersedia_grp} tersedia / {terisi_grp} terisi / {dibereskan_grp} dibereskan)"
            )
            group.setObjectName("floorGroup")
            grid = QGridLayout(group)
            grid.setSpacing(12)
            for i, meja in enumerate(meja_list):
                card = MejaCard(meja, self.on_meja_clicked)
                grid.addWidget(card, i // 8, i % 8)
            self.floor_layout.addWidget(group)

        self.floor_layout.addStretch()

    def _filtered_sorted_data(self):
        search = self.search_input.text().strip().lower()
        status_filter = self.filter_status.currentText()
        kapasitas_filter = self.filter_kapasitas.currentText()

        data = []
        for meja in self.all_data:
            if search and search not in meja['nomor_meja'].lower() and search not in meja['jenis'].lower():
                continue
            if status_filter != "Semua Status" and meja['status'] != status_filter:
                continue
            if not self._match_kapasitas(meja['kapasitas'], kapasitas_filter):
                continue
            data.append(meja)

        sort_mode = self.sort_combo.currentText()
        if sort_mode == "Urut: Nomor Meja":
            data.sort(key=lambda m: m['nomor_meja'])
        elif sort_mode == "Urut: Status":
            data.sort(key=lambda m: (m['status'], m['nomor_meja']))
        elif sort_mode == "Urut: Lantai":
            data.sort(key=lambda m: (m['lantai'], m['nomor_meja']))
        else:
            data.sort(key=lambda m: (m['kapasitas'], m['nomor_meja']))
        return data

    def _match_kapasitas(self, kapasitas, filter_text):
        if filter_text == "1-2 orang":
            return kapasitas <= 2
        if filter_text == "3-4 orang":
            return 3 <= kapasitas <= 4
        if filter_text == "5-8 orang":
            return 5 <= kapasitas <= 8
        if filter_text == "> 8 orang":
            return kapasitas > 8
        return True

    def _update_summary(self, tables):
        total = len(tables)
        tersedia = sum(1 for t in tables if t['status'] == 'Tersedia')
        terisi = sum(1 for t in tables if t['status'] == 'Terisi')
        dibereskan = sum(1 for t in tables if t['status'] == 'Dibereskan')
        maintenance = sum(1 for t in tables if t['status'] == 'Maintenance')
        self.summary_lbl.setText(
            f"Total: {total} meja | Tersedia: {tersedia} | Terisi: {terisi} | Dibereskan: {dibereskan} | Maintenance: {maintenance}"
        )

    def tambah_meja(self):
        dialog = MejaDialog(parent=self)
        if dialog.exec() == QDialog.Accepted:
            self.refresh()

    def edit_meja(self, meja_id):
        dialog = MejaDialog(meja_id=meja_id, parent=self)
        if dialog.exec() == QDialog.Accepted:
            self.refresh()

    def hapus_meja(self, meja_id):
        meja = database.get_meja_by_id(meja_id)
        if not meja:
            return
        reply = QMessageBox.question(
            self, "Konfirmasi Hapus",
            f"Yakin ingin menghapus meja {meja['nomor_meja']}?",
            QMessageBox.Yes | QMessageBox.No
        )
        if reply == QMessageBox.Yes:
            ok, err = database.hapus_meja(meja_id)
            if ok:
                self.refresh()
                QMessageBox.information(self, "Sukses", "Meja berhasil dihapus.")
            else:
                QMessageBox.critical(self, "Error", f"Gagal menghapus meja: {err}")

    def on_meja_clicked(self, meja_id):
        meja = database.get_meja_by_id(meja_id)
        if not meja:
            return

        conn = database.get_db_connection()
        aktif = conn.execute("""
            SELECT r.nama_tamu, r.waktu, r.tanggal, r.status
            FROM reservasi r
            WHERE r.meja_id = ? AND r.status IN ('Menunggu','Dikonfirmasi')
            ORDER BY r.tanggal, r.waktu
        """, (meja_id,)).fetchall()
        conn.close()

        msg = QMessageBox(self)
        msg.setWindowTitle(f"Meja {meja['nomor_meja']}")
        msg.setText(
            f"<b>Nomor Meja:</b> {meja['nomor_meja']}<br>"
            f"<b>Kapasitas:</b> {meja['kapasitas']} orang<br>"
            f"<b>Lantai:</b> {meja['lantai']}<br>"
            f"<b>Jenis:</b> {meja['jenis']}<br>"
            f"<b>Status Saat Ini:</b> {meja['status']}"
            + (f"<br><br>Ada <b>{len(aktif)}</b> reservasi aktif pada meja ini." if aktif else "")
            + "<br><br>Pilih aksi:"
        )

        btns = {}
        btn_edit = msg.addButton("Edit Data", QMessageBox.ActionRole)
        btns[btn_edit] = 'Edit'
        btn_delete = msg.addButton("Hapus", QMessageBox.ActionRole)
        btns[btn_delete] = 'Hapus'
        if meja['status'] == 'Dibereskan':
            btn_t = msg.addButton("Set Tersedia", QMessageBox.ActionRole)
            btns[btn_t] = 'Tersedia'
        elif meja['status'] != 'Maintenance':
            btn_m = msg.addButton("Set Maintenance", QMessageBox.ActionRole)
            btns[btn_m] = 'Maintenance'
        else:
            btn_t = msg.addButton("Set Tersedia", QMessageBox.ActionRole)
            btns[btn_t] = 'Tersedia'

        msg.addButton("Tutup", QMessageBox.RejectRole)
        msg.exec()

        clicked = msg.clickedButton()
        if clicked not in btns:
            return

        action = btns[clicked]
        if action == 'Edit':
            self.edit_meja(meja_id)
            return
        if action == 'Hapus':
            self.hapus_meja(meja_id)
            return

        if action == 'Maintenance' and aktif:
            konfirm = QMessageBox.question(
                self, "Konfirmasi",
                f"Meja ini masih punya {len(aktif)} reservasi aktif.\nYakin ingin set Maintenance?",
                QMessageBox.Yes | QMessageBox.No
            )
            if konfirm == QMessageBox.No:
                return

        conn = database.get_db_connection()
        conn.execute("UPDATE meja SET status = ? WHERE id = ?", (action, meja_id))
        if action != 'Maintenance':
            database.sync_status_meja(conn, meja_id)
        conn.commit()
        conn.close()
        self.refresh()
