from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QHBoxLayout, QScrollArea, QFrame
)
from ui_python_files.ui_MainWindow import Ui_MainWindow
from components.PDFArea import PDFArea
import fitz 
import os 

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.addFileButton.clicked.connect(self.add_file)
        
        # setup input scroll area
        self.inputScrollWidget = QWidget()
        self.inputScrollContent = QVBoxLayout(self.inputScrollWidget)
        self.inputScrollContent.setAlignment(Qt.AlignTop)
        self.inputScrollArea.setWidget(self.inputScrollWidget)
        self.inputScrollArea.setWidgetResizable(True)

        # Setup output scroll area (where selected ClickableLabel will be moved)
        self.outputScrollWidget = QWidget()
        self.outputScrollContent = QHBoxLayout(self.outputScrollWidget)
        self.outputScrollContent.setAlignment(Qt.AlignLeft)
        self.outputScrollArea.setWidget(self.outputScrollWidget)
        self.outputScrollArea.setWidgetResizable(True)
    
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
