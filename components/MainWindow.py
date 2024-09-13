from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QHBoxLayout, QScrollArea, QFrame
)
from ui_python_files.ui_MainWindow import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.addFileButton.clicked.connect(self.add_file)


    
    def add_file(self):
        file_dialog = QFileDialog(self)
        file_path, _ = file_dialog.getOpenFileName(self, "Open PDF", "", "PDF Files (*.pdf)")

        if file_path:
            self.statusBar().showMessage(f"{file_path} has been loaded.", 3000)