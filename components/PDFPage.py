from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QHBoxLayout, QScrollArea, QFrame
)
from PySide6.QtGui import QPalette

class PDFPage(QLabel):
    """ Custom QLabel to make it clickable """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFrameStyle(QFrame.StyledPanel | QFrame.Plain)
        self.setLineWidth(2)
        self.setFixedSize(150,200)
        self.selected = False
        self.unselect()
        
        self.page_num = None  
        self.pdf_document = None  
    
    def mousePressEvent(self, event):
        """ Toggle selection on mouse click """
        if self.selected:
            self.unselect()
        else:
            self.select()

    def select(self):
        """ Mark label as selected with a border based on system theme """
        self.selected = True
        border_color = self.get_system_theme_color(selected=True)
        self.setStyleSheet(f"border: 2px solid {border_color}; padding: 2px;")

    def unselect(self):
        """ Mark label as unselected with a border based on system theme """
        self.selected = False
        border_color = self.get_system_theme_color(selected=False)
        self.setStyleSheet(f"border: 2px solid {border_color}; padding: 2px;")

    def get_system_theme_color(self, selected):
        """ Get the color based on the current system theme and selection state """
        palette = QApplication.palette()

        if palette.color(QPalette.Window).lightness() > 128:  # Light mode
            return "blue" if selected else "gray"  # Use light-mode colors
        else:  # Dark mode
            return "cyan" if selected else "darkgray"  # Use dark-mode colors