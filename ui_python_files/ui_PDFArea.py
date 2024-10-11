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
import resource_rc

class Ui_PDFArea(object):
    def setupUi(self, PDFArea):
        if not PDFArea.objectName():
            PDFArea.setObjectName(u"PDFArea")
        PDFArea.resize(977, 328)
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
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.filenameLabel.setFont(font)

        self.horizontalLayout.addWidget(self.filenameLabel)

        self.horizontalSpacer = QSpacerItem(50, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.closeButton = QPushButton(self.widget)
        self.closeButton.setObjectName(u"closeButton")
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setKerning(False)
        self.closeButton.setFont(font1)
        self.closeButton.setStyleSheet(u"")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.WindowClose))
        self.closeButton.setIcon(icon)

        self.horizontalLayout.addWidget(self.closeButton)


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
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 957, 198))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        self.widget_2 = QWidget(PDFArea)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.selectButton = QPushButton(self.widget_2)
        self.selectButton.setObjectName(u"selectButton")
        self.selectButton.setFont(font)
        self.selectButton.setStyleSheet(u"QPushButton {\n"
"    border: 2px solid rgb(18, 18, 18);\n"
"    border-radius: 15px;\n"
"    padding: 5px;\n"
"}")

        self.horizontalLayout_2.addWidget(self.selectButton)

        self.addButton = QPushButton(self.widget_2)
        self.addButton.setObjectName(u"addButton")
        self.addButton.setFont(font)
        self.addButton.setStyleSheet(u"QPushButton {\n"
"    border: 2px solid rgb(18, 18, 18);\n"
"    border-radius: 15px;\n"
"    padding: 5px;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/add.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.addButton.setIcon(icon1)

        self.horizontalLayout_2.addWidget(self.addButton)


        self.verticalLayout.addWidget(self.widget_2, 0, Qt.AlignmentFlag.AlignRight)


        self.retranslateUi(PDFArea)

        QMetaObject.connectSlotsByName(PDFArea)
    # setupUi

    def retranslateUi(self, PDFArea):
        PDFArea.setWindowTitle(QCoreApplication.translate("PDFArea", u"Form", None))
        self.filenameLabel.setText(QCoreApplication.translate("PDFArea", u"TextLabel", None))
        self.closeButton.setText("")
        self.selectButton.setText(QCoreApplication.translate("PDFArea", u"Select All", None))
        self.addButton.setText(QCoreApplication.translate("PDFArea", u"Add", None))
    # retranslateUi

