from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QHBoxLayout, QScrollArea, QFrame
)
from ui_python_files.ui_PDFArea import Ui_PDFArea
import fitz
from components.PDFPage import PDFPage
from PySide6.QtGui import QPixmap, QImage
from helpers.helpers import get_system_theme_color

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

        self.filenameLabel.setText(file_name) 

        self.addButton.clicked.connect(self.add_selected_to_output)
        self.closeButton.clicked.connect(self.remove_pdf_area)
        self.selectButton.clicked.connect(self.toggle_select)

        self.update_add_button_state()
        self.apply_stylesheet()
    
    def load(self):
        for page_num in range(len(self.pdf_document)):
            page = self.pdf_document.load_page(page_num)
            pix = page.get_pixmap(matrix=fitz.Matrix(3.0, 3.0))

            if pix.alpha:  
                qimage = QImage(pix.samples, pix.width, pix.height, pix.stride, QImage.Format_RGBA8888)
            else:  
                qimage = QImage(pix.samples, pix.width, pix.height, pix.stride, QImage.Format_RGB888)

            if not qimage.isNull():
                page_label = PDFPage()
                page_label.setPixmap(QPixmap.fromImage(qimage).scaled(150, 200, Qt.KeepAspectRatio, Qt.SmoothTransformation))
                page_label.page_num = page_num
                page_label.pdf_document = self.pdf_document
                self.page_labels.append(page_label)
                self.horizontalScrollContent.addWidget(page_label)
                page_label.selection_changed.connect(self.update_add_button_state)
            else:
                print(f"Failed to convert pixmap to QImage for page {page_num}")
    
    def copy_label(self, label):
        new_label = PDFPage()
        new_label.setText(label.text())  
        new_label.setPixmap(label.pixmap()) 
        new_label.page_num = label.page_num
        new_label.pdf_document = label.pdf_document
        
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

    def remove_pdf_area(self):
        parent_layout = self.parentWidget().layout()

        if parent_layout:
            parent_layout.removeWidget(self)

        self.setParent(None)
        self.deleteLater()

    def toggle_select(self):
        all_selected = all(label.selected for label in self.page_labels)

        if all_selected:
            for label in self.page_labels:
                label.unselect()
            self.selectButton.setText("Select All")
        else:
            for label in self.page_labels:
                label.select()
            self.selectButton.setText("Unselect All")
        
        self.update_add_button_state()

    def update_add_button_state(self):
        if len(self.get_selected_labels()) == 0:
            self.addButton.setDisabled(True)
        else:
            self.addButton.setDisabled(False)
    
    def apply_stylesheet(self):
        theme = get_system_theme_color()
        if theme == "light":
            border_color = "rgb(18, 18, 18)"
            hover_color = "rgb(214, 214, 214)"
        else:  # dark theme
            border_color = "rgb(200, 200, 200);"
            hover_color = "rgb(70, 70, 70);"

        button_stylesheet = f"""
            QPushButton {{
                border: 2px solid {border_color};
                border-radius: 10px;
                padding: 5px;
            }}
            QPushButton:hover {{
                background-color: {hover_color};
            }}
        """
        self.selectButton.setStyleSheet(button_stylesheet)
        self.addButton.setStyleSheet(button_stylesheet)