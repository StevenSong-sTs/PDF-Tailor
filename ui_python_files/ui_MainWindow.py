# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QMenu, QMenuBar, QPushButton, QScrollArea,
    QSizePolicy, QStatusBar, QVBoxLayout, QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1165, 930)
        self.actionAdd = QAction(MainWindow)
        self.actionAdd.setObjectName(u"actionAdd")
        self.actionClear = QAction(MainWindow)
        self.actionClear.setObjectName(u"actionClear")
        self.actionExport = QAction(MainWindow)
        self.actionExport.setObjectName(u"actionExport")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.titleLabel = QLabel(self.centralwidget)
        self.titleLabel.setObjectName(u"titleLabel")
        font = QFont()
        font.setPointSize(14)
        self.titleLabel.setFont(font)
        self.titleLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.titleLabel)

        self.inputLabel = QLabel(self.centralwidget)
        self.inputLabel.setObjectName(u"inputLabel")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.inputLabel.setFont(font1)

        self.verticalLayout.addWidget(self.inputLabel)

        self.inputContainer = QWidget(self.centralwidget)
        self.inputContainer.setObjectName(u"inputContainer")
        self.inputContainer.setMinimumSize(QSize(0, 460))
        self.verticalLayout_2 = QVBoxLayout(self.inputContainer)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.inputScrollArea = QScrollArea(self.inputContainer)
        self.inputScrollArea.setObjectName(u"inputScrollArea")
        self.inputScrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 1127, 380))
        self.inputScrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_2.addWidget(self.inputScrollArea)

        self.addFileButtonContainer = QWidget(self.inputContainer)
        self.addFileButtonContainer.setObjectName(u"addFileButtonContainer")
        self.addFileButtonContainer.setStyleSheet(u"QPushButton:hover {\n"
"	background-color: rgb(161, 161, 161);\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.addFileButtonContainer)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.addFileButton = QPushButton(self.addFileButtonContainer)
        self.addFileButton.setObjectName(u"addFileButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addFileButton.sizePolicy().hasHeightForWidth())
        self.addFileButton.setSizePolicy(sizePolicy)
        self.addFileButton.setBaseSize(QSize(0, 0))
        self.addFileButton.setFont(font1)
        self.addFileButton.setAutoFillBackground(False)
        self.addFileButton.setStyleSheet(u"QPushButton {\n"
"    border: 2px solid rgb(18, 18, 18);\n"
"    border-radius: 15px;\n"
"    padding: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(214, 214, 214);\n"
"}")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.FolderNew))
        self.addFileButton.setIcon(icon)
        self.addFileButton.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.addFileButton)


        self.verticalLayout_2.addWidget(self.addFileButtonContainer)


        self.verticalLayout.addWidget(self.inputContainer)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_3 = QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.outputLabel = QLabel(self.widget)
        self.outputLabel.setObjectName(u"outputLabel")
        self.outputLabel.setFont(font1)

        self.horizontalLayout_3.addWidget(self.outputLabel)

        self.removeSelectedPagesButton = QPushButton(self.widget)
        self.removeSelectedPagesButton.setObjectName(u"removeSelectedPagesButton")
        sizePolicy.setHeightForWidth(self.removeSelectedPagesButton.sizePolicy().hasHeightForWidth())
        self.removeSelectedPagesButton.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        self.removeSelectedPagesButton.setFont(font2)
        self.removeSelectedPagesButton.setStyleSheet(u"QPushButton {\n"
"    border: 2px solid rgb(18, 18, 18);\n"
"    border-radius: 15px;\n"
"    padding: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(214, 214, 214);\n"
"}")

        self.horizontalLayout_3.addWidget(self.removeSelectedPagesButton)


        self.verticalLayout.addWidget(self.widget)

        self.outputContainer = QWidget(self.centralwidget)
        self.outputContainer.setObjectName(u"outputContainer")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.outputContainer.sizePolicy().hasHeightForWidth())
        self.outputContainer.setSizePolicy(sizePolicy1)
        self.outputContainer.setMinimumSize(QSize(0, 0))
        self.verticalLayout_3 = QVBoxLayout(self.outputContainer)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.outputScrollArea = QScrollArea(self.outputContainer)
        self.outputScrollArea.setObjectName(u"outputScrollArea")
        sizePolicy1.setHeightForWidth(self.outputScrollArea.sizePolicy().hasHeightForWidth())
        self.outputScrollArea.setSizePolicy(sizePolicy1)
        self.outputScrollArea.setMinimumSize(QSize(0, 200))
        self.outputScrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1127, 198))
        self.outputScrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_3.addWidget(self.outputScrollArea)

        self.outputButtonContainer = QWidget(self.outputContainer)
        self.outputButtonContainer.setObjectName(u"outputButtonContainer")
        self.horizontalLayout_2 = QHBoxLayout(self.outputButtonContainer)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.exportButton = QPushButton(self.outputButtonContainer)
        self.exportButton.setObjectName(u"exportButton")
        sizePolicy.setHeightForWidth(self.exportButton.sizePolicy().hasHeightForWidth())
        self.exportButton.setSizePolicy(sizePolicy)
        self.exportButton.setFont(font1)
        self.exportButton.setStyleSheet(u"QPushButton {\n"
"    border: 2px solid rgb(18, 18, 18);\n"
"    border-radius: 15px;\n"
"    padding: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(214, 214, 214);\n"
"}")
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MailForward))
        self.exportButton.setIcon(icon1)
        self.exportButton.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.exportButton)


        self.verticalLayout_3.addWidget(self.outputButtonContainer, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout.addWidget(self.outputContainer)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1165, 33))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionAdd)
        self.menuFile.addAction(self.actionClear)
        self.menuFile.addAction(self.actionExport)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionAdd.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.actionClear.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.actionExport.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        self.titleLabel.setText("")
        self.inputLabel.setText(QCoreApplication.translate("MainWindow", u"Input:", None))
        self.addFileButton.setText(QCoreApplication.translate("MainWindow", u"Add File", None))
        self.outputLabel.setText(QCoreApplication.translate("MainWindow", u"Output:", None))
        self.removeSelectedPagesButton.setText(QCoreApplication.translate("MainWindow", u"Remove Selected Pages", None))
        self.exportButton.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

