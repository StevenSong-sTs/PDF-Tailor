import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QHBoxLayout, QScrollArea, QFrame
)
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtCore import Qt
import fitz  # PyMuPDF for PDF handling
from PIL import Image
from PIL.ImageQt import ImageQt
import io

class ClickableLabel(QLabel):
    """ Custom QLabel to make it clickable """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFrameStyle(QFrame.StyledPanel | QFrame.Plain)
        self.setLineWidth(2)
        self.selected = False
        self.unselect()

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


class PDFTailorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PDF Tailor")
        self.setGeometry(100, 100, 800, 600)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # PDF File Label
        self.pdf_label = QLabel("No file selected")
        self.layout.addWidget(self.pdf_label)

        # Area to display the pages
        self.page_scroll = QScrollArea()
        self.page_widget = QWidget()
        self.page_layout = QVBoxLayout(self.page_widget)
        self.page_scroll.setWidget(self.page_widget)
        self.page_scroll.setWidgetResizable(True)
        self.layout.addWidget(self.page_scroll)

        # Load File Button
        self.load_button = QPushButton("Add new file")
        self.load_button.clicked.connect(self.load_pdf)
        self.layout.addWidget(self.load_button)

        # Export Button
        self.export_button = QPushButton("Export")
        self.export_button.clicked.connect(self.export_selected_pages)
        self.export_button.setEnabled(False)
        self.layout.addWidget(self.export_button)

        self.pdf_document = None
        self.page_labels = []

    def load_pdf(self):
        file_dialog = QFileDialog(self)
        file_path, _ = file_dialog.getOpenFileName(self, "Open PDF", "", "PDF Files (*.pdf)")
        
        if file_path:
            self.pdf_label.setText(file_path)
            self.pdf_document = fitz.open(file_path)
            self.display_pdf_pages()
            self.export_button.setEnabled(True)

    def display_pdf_pages(self):
        # Clear any previous pages
        for i in reversed(range(self.page_layout.count())):
            self.page_layout.itemAt(i).widget().deleteLater()

        self.page_labels.clear()

        for page_num in range(len(self.pdf_document)):
            page = self.pdf_document.load_page(page_num)
            pix = page.get_pixmap(matrix=fitz.Matrix(1.5, 1.5))  # Scale for higher resolution
            img = Image.open(io.BytesIO(pix.tobytes("png")))

            # Convert to QPixmap to display in QLabel
            qimage = QPixmap.fromImage(ImageQt(img))
            page_label = ClickableLabel()
            page_label.setPixmap(qimage.scaled(150, 200, Qt.KeepAspectRatio))
            page_label.page_num = page_num  # Store page number
            self.page_labels.append(page_label)

            # Add page preview to layout
            hbox = QHBoxLayout()
            hbox.addWidget(page_label)
            self.page_layout.addLayout(hbox)

    def export_selected_pages(self):
        selected_pages = [label.page_num for label in self.page_labels if label.selected]

        if not selected_pages:
            return  # No pages selected

        file_dialog = QFileDialog(self)
        save_path, _ = file_dialog.getSaveFileName(self, "Save PDF", "", "PDF Files (*.pdf)")

        if save_path:
            new_pdf = fitz.open()  # Create a new PDF

            for page_num in selected_pages:
                new_pdf.insert_pdf(self.pdf_document, from_page=page_num, to_page=page_num)

            new_pdf.save(save_path)
            new_pdf.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PDFTailorApp()
    window.show()
    sys.exit(app.exec())
