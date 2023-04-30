# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_account_window.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QLineEdit,
    QPushButton, QSizePolicy, QSplitter, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(835, 50)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.splitter = QSplitter(Dialog)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.account_name_lineEdit = QLineEdit(self.splitter)
        self.account_name_lineEdit.setObjectName(u"account_name_lineEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.account_name_lineEdit.sizePolicy().hasHeightForWidth())
        self.account_name_lineEdit.setSizePolicy(sizePolicy1)
        self.splitter.addWidget(self.account_name_lineEdit)
        self.account_category_comboBox = QComboBox(self.splitter)
        self.account_category_comboBox.setObjectName(u"account_category_comboBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(1)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.account_category_comboBox.sizePolicy().hasHeightForWidth())
        self.account_category_comboBox.setSizePolicy(sizePolicy2)
        self.account_category_comboBox.setEditable(True)
        self.splitter.addWidget(self.account_category_comboBox)
        self.add_account_pushButton = QPushButton(self.splitter)
        self.add_account_pushButton.setObjectName(u"add_account_pushButton")
        self.splitter.addWidget(self.add_account_pushButton)

        self.verticalLayout.addWidget(self.splitter)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Add Account Window", None))
        self.account_name_lineEdit.setPlaceholderText(QCoreApplication.translate("Dialog", u"Enter Account Name Here", None))
        self.account_category_comboBox.setCurrentText(QCoreApplication.translate("Dialog", u"Choose or Enter Account Category", None))
        self.add_account_pushButton.setText(QCoreApplication.translate("Dialog", u"Add Account", None))
    # retranslateUi

