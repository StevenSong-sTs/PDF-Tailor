from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QHBoxLayout, QScrollArea, QFrame
)
from PySide6.QtCore import Signal
from PySide6.QtGui import QPalette

class PDFPage(QLabel):
    selection_changed = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFrameStyle(QFrame.StyledPanel | QFrame.Plain)
        self.setLineWidth(2)
        self.setFixedSize(120,160)
        self.selected = False
        self.unselect()
        
        self.page_num = None  
        self.pdf_document = None  
    
    def mousePressEvent(self, event):
        if self.selected:
            self.unselect()
        else:
            self.select()
    
        self.selection_changed.emit()

    def select(self):
        self.selected = True
        border_color = self.get_system_theme_color(selected=True)
        self.setStyleSheet(f"border: 2px solid {border_color}; padding: 2px;")

    def unselect(self):
        self.selected = False
        border_color = self.get_system_theme_color(selected=False)
        self.setStyleSheet(f"border: 2px solid {border_color}; padding: 2px;")

    def get_system_theme_color(self, selected):
        palette = QApplication.palette()

        if palette.color(QPalette.Window).lightness() > 128:  # Light mode
            return "blue" if selected else "gray"  # Use light-mode colors
        else:  # Dark mode
            return "cyan" if selected else "darkgray"  # Use dark-mode colors