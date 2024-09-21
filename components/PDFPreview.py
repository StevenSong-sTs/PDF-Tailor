from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QHBoxLayout, QScrollArea, QFrame
)

class PDFPreview(QLabel):
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
        """ Mark label as selected with a border """
        self.selected = True
        self.setStyleSheet("border: 2px solid blue")

    def unselect(self):
        """ Mark label as unselected """
        self.selected = False
        self.setStyleSheet("border: 2px solid gray")