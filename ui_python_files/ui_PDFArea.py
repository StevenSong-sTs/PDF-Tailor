# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PDFArea.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QPushButton, QScrollArea,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_PDFArea(object):
    def setupUi(self, PDFArea):
        if not PDFArea.objectName():
            PDFArea.setObjectName(u"PDFArea")
        PDFArea.resize(992, 272)
        self.verticalLayout = QVBoxLayout(PDFArea)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(PDFArea)
        self.widget.setObjectName(u"widget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.removeButton = QPushButton(self.widget)
        self.removeButton.setObjectName(u"removeButton")

        self.horizontalLayout.addWidget(self.removeButton)

        self.addButton = QPushButton(self.widget)
        self.addButton.setObjectName(u"addButton")

        self.horizontalLayout.addWidget(self.addButton)


        self.verticalLayout.addWidget(self.widget, 0, Qt.AlignmentFlag.AlignRight)

        self.scrollArea = QScrollArea(PDFArea)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy1)
        self.scrollArea.setMinimumSize(QSize(0, 200))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 972, 198))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)


        self.retranslateUi(PDFArea)

        QMetaObject.connectSlotsByName(PDFArea)
    # setupUi

    def retranslateUi(self, PDFArea):
        PDFArea.setWindowTitle(QCoreApplication.translate("PDFArea", u"Form", None))
        self.removeButton.setText(QCoreApplication.translate("PDFArea", u"Remove", None))
        self.addButton.setText(QCoreApplication.translate("PDFArea", u"Add", None))
    # retranslateUi

