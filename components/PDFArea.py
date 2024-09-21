from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QHBoxLayout, QScrollArea, QFrame
)
from ui_python_files.ui_PDFArea import Ui_PDFArea
import fitz
from components.PDFPreview import PDFPreview
from PySide6.QtGui import QPixmap, QImage

class PDFArea(QWidget, Ui_PDFArea):
    def __init__(self, document, file_name, outputContent):
        super().__init__()
        self.setupUi(self)
        self.pdf_document = document
        self.file_name = file_name
        self.outputContent = outputContent
        self.page_labels = []

        self.horizontalScrollWidget = QWidget()
        self.horizontalScrollContent = QHBoxLayout(self.horizontalScrollWidget)
        self.horizontalScrollContent.setAlignment(Qt.AlignLeft)
        self.scrollArea.setWidget(self.horizontalScrollWidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setFixedHeight(240)

        self.filenameLabel.setText(file_name) 

        self.addButton.clicked.connect(self.add_selected_to_output)

    def load(self):
        for page_num in range(len(self.pdf_document)):
            page = self.pdf_document.load_page(page_num)
            pix = page.get_pixmap(matrix=fitz.Matrix(3.0, 3.0))

            if pix.alpha:  
                qimage = QImage(pix.samples, pix.width, pix.height, pix.stride, QImage.Format_RGBA8888)
            else:  
                qimage = QImage(pix.samples, pix.width, pix.height, pix.stride, QImage.Format_RGB888)

            if not qimage.isNull():
                page_label = PDFPreview()
                page_label.setPixmap(QPixmap.fromImage(qimage).scaled(150, 200, Qt.KeepAspectRatio, Qt.SmoothTransformation))
                page_label.page_num = page_num
                page_label.pdf_document = self.pdf_document
                self.page_labels.append(page_label)
                self.horizontalScrollContent.addWidget(page_label)
            else:
                print(f"Failed to convert pixmap to QImage for page {page_num}")
    
    def copy_label(self, label):
        new_label = PDFPreview()
        new_label.setText(label.text())  
        new_label.setPixmap(label.pixmap()) 
        new_label.selected = label.selected
        new_label.page_num = label.page_num
        new_label.pdf_document = label.pdf_document

        if new_label.selected:
            new_label.select()
        else:
            new_label.unselect() 
        
        return new_label
    
    def get_selected_labels(self):
        selected_labels = []
        for label in self.page_labels:
            if label.selected:
                new_label = self.copy_label(label)
                selected_labels.append(new_label)

        return selected_labels
    
    def add_selected_to_output(self):
        selected_labels = self.get_selected_labels()
        if len(selected_labels) > 0:
            for label in selected_labels:
                self.outputContent.addWidget(label)
