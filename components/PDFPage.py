from PySide6.QtWidgets import (
    QApplication, QLabel, QFrame
)
from PySide6.QtCore import Signal
from PySide6.QtGui import QPalette

class PDFPage(QLabel):
    selection_changed = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFrameStyle(QFrame.StyledPanel | QFrame.Plain)
        self.setFixedSize(120, 160)
        self.selected = False
        self.page_num = None  
        self.pdf_document = None

        # Store the base stylesheet to easily modify later
        self.base_stylesheet = (
            "QLabel {"
            "    border: 2px solid rgb(18, 18, 18);"
            "    border-radius: 5px;"
            "    padding: 2px;"
            "}"
            "QLabel:hover {"
            "    background-color: rgb(214, 214, 214);"
            "}"
        )
        self.setStyleSheet(self.base_stylesheet)
        self.unselect()

        self.setToolTip("Click to select or unselect this PDF page.")

    def mousePressEvent(self, event):
        if self.selected:
            self.unselect()
        else:
            self.select()
    
        self.selection_changed.emit()

    def select(self):
        self.selected = True
        border_color = self.get_system_theme_color(selected=True)
        self.update_border_color(border_color)

    def unselect(self):
        self.selected = False
        border_color = self.get_system_theme_color(selected=False)
        self.update_border_color(border_color)

    def update_border_color(self, color):
        self.setStyleSheet(f"{self.base_stylesheet} QLabel {{ border-color: {color}; }}")

    def get_system_theme_color(self, selected):
        palette = QApplication.palette()

        if palette.color(QPalette.Window).lightness() > 128:  # Light mode
            return "blue" if selected else "gray"  # Use light-mode colors
        else:  # Dark mode
            return "cyan" if selected else "darkgray"  # Use dark-mode colors
