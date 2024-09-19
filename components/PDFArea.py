from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QHBoxLayout, QScrollArea, QFrame
)
from ui_python_files.ui_PDFArea import Ui_PDFArea
import fitz
from components.ClickableLabel import ClickableLabel
from PySide6.QtGui import QPixmap, QImage

class PDFArea(QWidget, Ui_PDFArea):
    def __init__(self, document, file_name):
        super().__init__()
        self.setupUi(self)
        self.pdf_document = document
        self.file_name = file_name
        self.page_labels = []

        # setup horizontal scrolling
        self.horizontalScrollWidget = QWidget()
        self.horizontalScrollContent = QHBoxLayout(self.horizontalScrollWidget)
        self.horizontalScrollContent.setAlignment(Qt.AlignLeft)
        self.scrollArea.setWidget(self.horizontalScrollWidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setFixedHeight(240)

        # Display the file name
        self.filenameLabel.setText(file_name) 

    def load(self):
        for page_num in range(len(self.pdf_document)):
            page = self.pdf_document.load_page(page_num)

            # Scale the PDF page once at a suitable resolution (e.g., 3.0)
            pix = page.get_pixmap(matrix=fitz.Matrix(3.0, 3.0))

            # Check if the pixmap is in RGBA or RGB format and set QImage format accordingly
            if pix.alpha:  # If pixmap has an alpha channel (RGBA)
                qimage = QImage(pix.samples, pix.width, pix.height, pix.stride, QImage.Format_RGBA8888)
            else:  # For RGB format
                qimage = QImage(pix.samples, pix.width, pix.height, pix.stride, QImage.Format_RGB888)

            # Check if QImage is valid before converting it to QPixmap
            if not qimage.isNull():
                page_label = ClickableLabel()
                page_label.setPixmap(QPixmap.fromImage(qimage).scaled(150, 200, Qt.KeepAspectRatio, Qt.SmoothTransformation))
                page_label.page_num = page_num
                self.page_labels.append(page_label)
                self.horizontalScrollContent.addWidget(page_label)
            else:
                print(f"Failed to convert pixmap to QImage for page {page_num}")

