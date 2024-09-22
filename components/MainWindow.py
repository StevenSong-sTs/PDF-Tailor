from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QHBoxLayout, QScrollArea, QFrame
)
from ui_python_files.ui_MainWindow import Ui_MainWindow
from components.PDFPreview import PDFPreview
from components.PDFArea import PDFArea
import fitz 
import os 

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.inputScrollWidget = QWidget()
        self.inputScrollContent = QVBoxLayout(self.inputScrollWidget)
        self.inputScrollContent.setAlignment(Qt.AlignTop)
        self.inputScrollArea.setWidget(self.inputScrollWidget)
        self.inputScrollArea.setWidgetResizable(True)

        self.outputScrollWidget = QWidget()
        self.outputScrollContent = QHBoxLayout(self.outputScrollWidget)
        self.outputScrollContent.setAlignment(Qt.AlignLeft)
        self.outputScrollArea.setWidget(self.outputScrollWidget)
        self.outputScrollArea.setWidgetResizable(True)
        self.outputScrollArea.setFixedHeight(240)

        self.addFileButton.clicked.connect(self.add_file)
        self.exportButton.clicked.connect(self.export_to_pdf)
    
    def add_file(self):
        file_dialog = QFileDialog(self)
        file_path, _ = file_dialog.getOpenFileName(self, "Open PDF", "", "PDF Files (*.pdf)")

        if file_path:
            file_name = os.path.basename(file_path)
            pdf_document = fitz.open(file_path)
            pdf_area = PDFArea(pdf_document, file_name, self.outputScrollContent)
            pdf_area.load()
            self.inputScrollContent.addWidget(pdf_area)
            
            self.statusBar().showMessage(f"{file_path} has been loaded.", 3000)

    def export_to_pdf(self):
        selected_labels = []

        for i in range(self.outputScrollContent.count()):
            widget = self.outputScrollContent.itemAt(i).widget()
            if isinstance(widget, PDFPreview) and widget.selected:
                selected_labels.append(widget)

        if selected_labels:
            file_dialog = QFileDialog(self)
            save_path, _ = file_dialog.getSaveFileName(self, "Save PDF", "", "PDF Files (*.pdf)")

            if save_path:
                output_pdf = fitz.open()

                for label in selected_labels:
                    if label.page_num is not None and label.pdf_document is not None:
                        output_pdf.insert_pdf(label.pdf_document, from_page=label.page_num, to_page=label.page_num)

                output_pdf.save(save_path)
                output_pdf.close()

                self.statusBar().showMessage(f"PDF saved to {save_path}", 3000)