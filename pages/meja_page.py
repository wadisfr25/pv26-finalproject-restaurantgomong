from PySide6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel,
                               QPushButton, QFrame, QGridLayout, QScrollArea,
                               QGroupBox, QMessageBox)
from PySide6.QtCore import Qt
import database


class MejaCard(QFrame):
    def __init__(self, meja, callback):
        super().__init__()
        self.meja_id = meja['id']
        self.callback = callback
        self.setCursor(Qt.PointingHandCursor)
        self.setFixedSize(120, 95)

        STATUS_COLOR = {
            'Tersedia':    ('#27AE60', '#EAFAF1'),
            'Terisi':      ('#E74C3C', '#FDEDEC'),
            'Maintenance': ('#F39C12', '#FEF9E7'),
        }
        border, bg = STATUS_COLOR.get(meja['status'], ('#95A5A6', '#F2F3F4'))

        self.setStyleSheet(f"""
            MejaCard {{
                background: {bg};
                border: 2px solid {border};
                border-radius: 10px;
            }}
            MejaCard:hover {{ background: {border}33; }}
        """)

        lay = QVBoxLayout(self)
        lay.setAlignment(Qt.AlignCenter)
        lay.setSpacing(3)

        no = QLabel(meja['nomor_meja'])
        no.setAlignment(Qt.AlignCenter)
        no.setStyleSheet("font-weight: bold; font-size: 11px;")

        cap = QLabel(f"👥 {meja['kapasitas']} orang")
        cap.setAlignment(Qt.AlignCenter)
        cap.setStyleSheet("font-size: 10px; color: #555;")

        status = QLabel(meja['status'])
        status.setAlignment(Qt.AlignCenter)
        status.setStyleSheet(f"color: {border}; font-size: 10px; font-weight: bold;")

        lay.addWidget(no)
        lay.addWidget(cap)
        lay.addWidget(status)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.callback(self.meja_id)


class MejaPage(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.refresh()

    def init_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(25, 20, 25, 20)
        layout.setSpacing(15)

        hdr = QHBoxLayout()
        title = QLabel("🪑 Peta Meja Restaurant Wadis")
        title.setObjectName("pageHeader")
        refresh_btn = QPushButton("🔄 Refresh")
        refresh_btn.clicked.connect(self.refresh)
        hdr.addWidget(title)
        hdr.addStretch()
        hdr.addWidget(refresh_btn)
        layout.addLayout(hdr)

        # Info otomatis
        info_lbl = QLabel(
            "ℹ️  Status meja diperbarui otomatis saat reservasi ditambah, diedit, atau dihapus. "
            "Klik kartu meja untuk ubah status Maintenance secara manual."
        )
        info_lbl.setStyleSheet(
            "color: #555; font-size: 11px; font-style: italic; "
            "background: #F0F4FF; border-radius: 6px; padding: 6px 10px;"
        )
        info_lbl.setWordWrap(True)
        layout.addWidget(info_lbl)

        # Legend
        legend = QHBoxLayout()
        for label, color in [
            ("● Tersedia", "#27AE60"),
            ("● Terisi", "#E74C3C"),
            ("● Maintenance", "#F39C12")
        ]:
            lbl = QLabel(label)
            lbl.setStyleSheet(f"color: {color}; font-weight: bold; font-size: 12px;")
            legend.addWidget(lbl)
            legend.addSpacing(20)

        # Ringkasan jumlah per status
        self.summary_lbl = QLabel()
        self.summary_lbl.setStyleSheet("color: #555; font-size: 11px;")
        legend.addStretch()
        legend.addWidget(self.summary_lbl)
        layout.addLayout(legend)

        # Scroll
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(QFrame.NoFrame)
        self.floor_container = QWidget()
        self.floor_layout = QVBoxLayout(self.floor_container)
        self.floor_layout.setSpacing(20)
        scroll.setWidget(self.floor_container)
        layout.addWidget(scroll)

    def refresh(self):
        while self.floor_layout.count():
            child = self.floor_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

        conn = database.get_db_connection()
        tables = conn.execute("SELECT * FROM meja ORDER BY kapasitas, nomor_meja").fetchall()
        conn.close()

        # Ringkasan
        total = len(tables)
        tersedia = sum(1 for t in tables if t['status'] == 'Tersedia')
        terisi = sum(1 for t in tables if t['status'] == 'Terisi')
        maintenance = sum(1 for t in tables if t['status'] == 'Maintenance')
        self.summary_lbl.setText(
            f"Total: {total} meja  |  Tersedia: {tersedia}  |  Terisi: {terisi}  |  Maintenance: {maintenance}"
        )

        # Kelompokkan berdasarkan kapasitas
        groups = {}
        for t in tables:
            cap = t['kapasitas']
            groups.setdefault(cap, []).append(t)

        group_labels = {
            2: "Meja 2 Orang",
            4: "Meja 4 Orang",
            6: "Meja 6 Orang",
            8: "Meja 8 Orang",
        }

        for cap in sorted(groups.keys()):
            meja_list = groups[cap]
            label = group_labels.get(cap, f"Meja {cap} Orang")
            tersedia_grp = sum(1 for m in meja_list if m['status'] == 'Tersedia')
            terisi_grp = sum(1 for m in meja_list if m['status'] == 'Terisi')

            group = QGroupBox(
                f"🪑  {label}  ·  {len(meja_list)} meja  "
                f"(✅ {tersedia_grp} tersedia  /  🔴 {terisi_grp} terisi)"
            )
            group.setObjectName("floorGroup")
            grid = QGridLayout(group)
            grid.setSpacing(12)
            for i, meja in enumerate(meja_list):
                card = MejaCard(meja, self.on_meja_clicked)
                grid.addWidget(card, i // 8, i % 8)
            self.floor_layout.addWidget(group)

        self.floor_layout.addStretch()

    def on_meja_clicked(self, meja_id):
        conn = database.get_db_connection()
        meja = conn.execute("SELECT * FROM meja WHERE id = ?", (meja_id,)).fetchone()
        conn.close()

        # Cek apakah ada reservasi aktif
        conn = database.get_db_connection()
        aktif = conn.execute("""
            SELECT r.nama_tamu, r.waktu, r.tanggal, r.status
            FROM reservasi r
            WHERE r.meja_id = ? AND r.status IN ('Menunggu','Dikonfirmasi','Duduk')
            ORDER BY r.tanggal, r.waktu
        """, (meja_id,)).fetchall()
        conn.close()

        info_reservasi = ""
        if aktif:
            baris = "\n".join(
                f"  • {r['nama_tamu']} — {r['tanggal']} {r['waktu']} [{r['status']}]"
                for r in aktif
            )
            info_reservasi = f"\n\n📋 Reservasi aktif:\n{baris}"

        msg = QMessageBox(self)
        msg.setWindowTitle(f"Meja {meja['nomor_meja']}")
        msg.setText(
            f"<b>Nomor Meja:</b> {meja['nomor_meja']}<br>"
            f"<b>Kapasitas:</b> {meja['kapasitas']} orang<br>"
            f"<b>Jenis:</b> {meja['jenis']}<br>"
            f"<b>Status Saat Ini:</b> {meja['status']}"
            + (f"<br><br>📋 Ada <b>{len(aktif)}</b> reservasi aktif pada meja ini." if aktif else "")
            + "<br><br>Ubah status:"
        )

        btns = {}
        if meja['status'] != 'Maintenance':
            btn_m = msg.addButton("🔧 Set Maintenance", QMessageBox.ActionRole)
            btns[btn_m] = 'Maintenance'
        if meja['status'] == 'Maintenance':
            btn_t = msg.addButton("✅ Set Tersedia", QMessageBox.ActionRole)
            btns[btn_t] = 'Tersedia'

        msg.addButton("Tutup", QMessageBox.RejectRole)
        msg.exec()

        clicked = msg.clickedButton()
        if clicked in btns:
            new_status = btns[clicked]
            if new_status == 'Maintenance' and aktif:
                konfirm = QMessageBox.question(
                    self, "Konfirmasi",
                    f"Meja ini masih punya {len(aktif)} reservasi aktif.\n"
                    "Yakin ingin set Maintenance?",
                    QMessageBox.Yes | QMessageBox.No
                )
                if konfirm == QMessageBox.No:
                    return
            conn = database.get_db_connection()
            conn.execute("UPDATE meja SET status = ? WHERE id = ?", (new_status, meja_id))
            conn.commit()
            conn.close()
            self.refresh()
