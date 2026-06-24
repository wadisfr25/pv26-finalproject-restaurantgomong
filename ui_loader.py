from pathlib import Path

from PySide6.QtCore import QFile, QObject
from PySide6.QtUiTools import QUiLoader


def load_ui(parent, filename):
    ui_path = Path(__file__).resolve().parent / filename
    ui_file = QFile(str(ui_path))
    if not ui_file.open(QFile.ReadOnly):
        raise FileNotFoundError(f"Tidak dapat membuka file UI: {ui_path}")

    try:
        widget = QUiLoader().load(ui_file, parent)
    finally:
        ui_file.close()

    if widget is None:
        raise RuntimeError(f"Gagal memuat file UI: {ui_path}")

    _bind_named_children(parent, widget)
    return widget


def _bind_named_children(parent, root):
    for child in root.findChildren(QObject):
        name = child.objectName()
        if name:
            setattr(parent, name, child)
