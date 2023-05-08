# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'graphing_criteria_Dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QPushButton, QSizePolicy,
    QSplitter, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(610, 45)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.splitter = QSplitter(Dialog)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.pushButton_graph_accounts = QPushButton(self.splitter)
        self.pushButton_graph_accounts.setObjectName(u"pushButton_graph_accounts")
        font = QFont()
        font.setPointSize(12)
        self.pushButton_graph_accounts.setFont(font)
        self.splitter.addWidget(self.pushButton_graph_accounts)
        self.pushButton_graph_transaciton_categories = QPushButton(self.splitter)
        self.pushButton_graph_transaciton_categories.setObjectName(u"pushButton_graph_transaciton_categories")
        self.pushButton_graph_transaciton_categories.setFont(font)
        self.splitter.addWidget(self.pushButton_graph_transaciton_categories)

        self.verticalLayout.addWidget(self.splitter)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.pushButton_graph_accounts.setText(QCoreApplication.translate("Dialog", u"Graph Accounts", None))
        self.pushButton_graph_transaciton_categories.setText(QCoreApplication.translate("Dialog", u"Graph Transaction Categories", None))
    # retranslateUi

