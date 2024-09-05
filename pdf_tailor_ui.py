import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget

WINDOW_SIZE = 800

class PdfTailorWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PDf Tailor")
        self.resize(WINDOW_SIZE, WINDOW_SIZE)
        centralWidget = QWidget(self)
        self.setCentralWidget(centralWidget)

def main():
    """PyCalc's main function."""
    app = QApplication([])
    window = PdfTailorWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()