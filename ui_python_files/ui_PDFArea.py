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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_PDFArea(object):
    def setupUi(self, PDFArea):
        if not PDFArea.objectName():
            PDFArea.setObjectName(u"PDFArea")
        PDFArea.resize(971, 266)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(PDFArea.sizePolicy().hasHeightForWidth())
        PDFArea.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(PDFArea)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(PDFArea)
        self.widget.setObjectName(u"widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy1)
        self.widget.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.filenameLabel = QLabel(self.widget)
        self.filenameLabel.setObjectName(u"filenameLabel")

        self.horizontalLayout.addWidget(self.filenameLabel)

        self.horizontalSpacer = QSpacerItem(50, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.closeButton = QPushButton(self.widget)
        self.closeButton.setObjectName(u"closeButton")

        self.horizontalLayout.addWidget(self.closeButton)

        self.selectButton = QPushButton(self.widget)
        self.selectButton.setObjectName(u"selectButton")

        self.horizontalLayout.addWidget(self.selectButton)

        self.addButton = QPushButton(self.widget)
        self.addButton.setObjectName(u"addButton")

        self.horizontalLayout.addWidget(self.addButton)


        self.verticalLayout.addWidget(self.widget)

        self.scrollArea = QScrollArea(PDFArea)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy2)
        self.scrollArea.setMinimumSize(QSize(0, 200))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 951, 198))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)


        self.retranslateUi(PDFArea)

        QMetaObject.connectSlotsByName(PDFArea)
    # setupUi

    def retranslateUi(self, PDFArea):
        PDFArea.setWindowTitle(QCoreApplication.translate("PDFArea", u"Form", None))
        self.filenameLabel.setText(QCoreApplication.translate("PDFArea", u"TextLabel", None))
        self.closeButton.setText(QCoreApplication.translate("PDFArea", u"Close File", None))
        self.selectButton.setText(QCoreApplication.translate("PDFArea", u"Select All", None))
        self.addButton.setText(QCoreApplication.translate("PDFArea", u"Add", None))
    # retranslateUi

