from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QPalette

def get_system_theme_color():
    app = QApplication.instance()
    if app is None:
        raise RuntimeError("QApplication instance must be created before calling this function.")
    
    palette = app.palette()
    if palette.color(QPalette.Window).lightness() > 128:  # Light mode
        return "light" 
    else:  # Dark mode
        return "dark"
