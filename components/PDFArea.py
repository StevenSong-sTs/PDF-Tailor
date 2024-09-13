from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QHBoxLayout, QScrollArea, QFrame
)
from ui_python_files.ui_PDFArea import Ui_PDFArea
import fitz
from components.ClickableLabel import ClickableLabel
from PIL import Image
from PIL.ImageQt import ImageQt
import io
from PySide6.QtGui import QPixmap, QImage

class PDFArea(QWidget, Ui_PDFArea):
    def __init__(self, document):
        super().__init__()
        self.setupUi(self)
        self.pdf_document = document
        self.page_labels = []

        # setup horizontal scrolling
        self.horizontalScrollWidget = QWidget()
        self.horizontalScrollContent = QHBoxLayout(self.horizontalScrollWidget)
        self.scrollArea.setWidget(self.horizontalScrollWidget)
        self.scrollArea.setWidgetResizable(True)

    def load(self):
        for page_num in range(len(self.pdf_document)):
            page = self.pdf_document.load_page(page_num)
            pix = page.get_pixmap(matrix=fitz.Matrix(2.0, 5.0))  # Scale for higher resolution
            img = Image.open(io.BytesIO(pix.tobytes("png")))

            # Convert to QPixmap to display in QLabel
            qimage = QPixmap.fromImage(ImageQt(img))
            page_label = ClickableLabel()
            page_label.setPixmap(qimage.scaled(300, 400, Qt.KeepAspectRatio))
            page_label.page_num = page_num  # Store page number
            self.page_labels.append(page_label)

            # Add page label to the hbox
            self.horizontalScrollContent.addWidget(page_label)