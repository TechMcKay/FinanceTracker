# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'payee_same_as_accountTransaction_Dialog.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QLabel, QSizePolicy, QVBoxLayout, QWidget)

class Ui_PayeeIsAccountDialog(object):
    def setupUi(self, PayeeIsAccountDialog):
        if not PayeeIsAccountDialog.objectName():
            PayeeIsAccountDialog.setObjectName(u"PayeeIsAccountDialog")
        PayeeIsAccountDialog.resize(543, 119)
        self.verticalLayout = QVBoxLayout(PayeeIsAccountDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(PayeeIsAccountDialog)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.buttonBox = QDialogButtonBox(PayeeIsAccountDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(PayeeIsAccountDialog)
        self.buttonBox.clicked.connect(PayeeIsAccountDialog.accept)

        QMetaObject.connectSlotsByName(PayeeIsAccountDialog)
    # setupUi

    def retranslateUi(self, PayeeIsAccountDialog):
        PayeeIsAccountDialog.setWindowTitle(QCoreApplication.translate("PayeeIsAccountDialog", u"Payee can't be Account", None))
        self.label.setText(QCoreApplication.translate("PayeeIsAccountDialog", u"Payee can not be the same as the account being withdrawn from.", None))
    # retranslateUi

