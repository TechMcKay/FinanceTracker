# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'transactionCategoryWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QSplitter,
    QStatusBar, QTableView, QVBoxLayout, QWidget)

class Ui_transactionCategoryWindow(object):
    def setupUi(self, transactionCategoryWindow):
        if not transactionCategoryWindow.objectName():
            transactionCategoryWindow.setObjectName(u"transactionCategoryWindow")
        transactionCategoryWindow.resize(800, 600)
        self.centralwidget = QWidget(transactionCategoryWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName(u"tableView")

        self.verticalLayout.addWidget(self.tableView)

        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.transation_category_lineEdit = QLineEdit(self.splitter)
        self.transation_category_lineEdit.setObjectName(u"transation_category_lineEdit")
        self.splitter.addWidget(self.transation_category_lineEdit)
        self.add_new_categoryButton = QPushButton(self.splitter)
        self.add_new_categoryButton.setObjectName(u"add_new_categoryButton")
        self.splitter.addWidget(self.add_new_categoryButton)

        self.verticalLayout.addWidget(self.splitter)

        transactionCategoryWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(transactionCategoryWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        transactionCategoryWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(transactionCategoryWindow)
        self.statusbar.setObjectName(u"statusbar")
        transactionCategoryWindow.setStatusBar(self.statusbar)

        self.retranslateUi(transactionCategoryWindow)

        QMetaObject.connectSlotsByName(transactionCategoryWindow)
    # setupUi

    def retranslateUi(self, transactionCategoryWindow):
        transactionCategoryWindow.setWindowTitle(QCoreApplication.translate("transactionCategoryWindow", u"Add Transaction Categories", None))
        self.transation_category_lineEdit.setPlaceholderText(QCoreApplication.translate("transactionCategoryWindow", u"Enter New Transaction Category", None))
        self.add_new_categoryButton.setText(QCoreApplication.translate("transactionCategoryWindow", u"Add New Category", None))
    # retranslateUi

