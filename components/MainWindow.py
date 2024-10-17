from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QHBoxLayout, QScrollArea, QFrame
)
from PySide6.QtGui import QPixmap
from ui_python_files.ui_MainWindow import Ui_MainWindow
from components.PDFPage import PDFPage
from components.PDFArea import PDFArea
from helpers.helpers import get_system_theme_color
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

        if get_system_theme_color() == 'light':
            pixmap = QPixmap("assets/text_logo_transparent_light.png")
        else:
            pixmap = QPixmap("assets/text_logo_transparent_dark.png")

        scaled_pixmap = pixmap.scaled(140, 100, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        self.titleLabel.setPixmap(scaled_pixmap)
        
        self.addFileButton.clicked.connect(self.add_file)
        self.exportButton.clicked.connect(self.export_to_pdf)
        self.removeSelectedPagesButton.clicked.connect(self.remove_selected_pages)
        self.apply_stylesheet()
    
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
        output_pages = []

        for i in range(self.outputScrollContent.count()):
            widget = self.outputScrollContent.itemAt(i).widget()
            if isinstance(widget, PDFPage) :
                output_pages.append(widget)

        if output_pages:
            file_dialog = QFileDialog(self)
            save_path, _ = file_dialog.getSaveFileName(self, "Save PDF", "", "PDF Files (*.pdf)")

            if save_path:
                output_pdf = fitz.open()

                for page in output_pages:
                    if page.page_num is not None and page.pdf_document is not None:
                        output_pdf.insert_pdf(page.pdf_document, from_page=page.page_num, to_page=page.page_num)

                output_pdf.save(save_path)
                output_pdf.close()
                self.statusBar().showMessage(f"PDF saved to {save_path}", 3000)

                try:
                    if os.name == 'nt':  # For Windows
                        os.startfile(save_path)
                    elif os.name == 'posix':  # For macOS and Linux
                        subprocess.call(('open' if sys.platform == 'darwin' else 'xdg-open', save_path))
                except Exception as e:
                    print(f"Failed to open PDF file: {e}")

    def remove_selected_pages(self):
        selected_labels = []

        for i in reversed(range(self.outputScrollContent.count())):
            widget_item = self.outputScrollContent.itemAt(i)
            widget = widget_item.widget()
            if isinstance(widget, PDFPage) and widget.selected:
                selected_labels.append(widget)

        for label in selected_labels:
            self.outputScrollContent.removeWidget(label)
            label.setParent(None)
            label.deleteLater()
    
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
        self.addFileButton.setStyleSheet(button_stylesheet)
        self.removeSelectedPagesButton.setStyleSheet(button_stylesheet)
        self.exportButton.setStyleSheet(button_stylesheet)

