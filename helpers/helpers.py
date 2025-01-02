import os
import sys
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

def resource_path(relative_path):
    """Get the absolute path to a resource, works for dev and PyInstaller."""
    if hasattr(sys, '_MEIPASS'):
        # PyInstaller temporary folder
        return os.path.join(sys._MEIPASS, relative_path)
    else:
        # Development mode
        return os.path.join(os.path.abspath("."), relative_path)
