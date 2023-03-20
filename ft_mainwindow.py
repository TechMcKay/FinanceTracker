# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ft_mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QComboBox, QDateEdit,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPlainTextEdit, QPushButton, QSizePolicy, QSplitter,
    QStatusBar, QTabWidget, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1183, 825)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.actionopen = QAction(MainWindow)
        self.actionopen.setObjectName(u"actionopen")
        self.actionsave = QAction(MainWindow)
        self.actionsave.setObjectName(u"actionsave")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy1)
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.main_tabWidget = QTabWidget(self.centralwidget)
        self.main_tabWidget.setObjectName(u"main_tabWidget")
        sizePolicy.setHeightForWidth(self.main_tabWidget.sizePolicy().hasHeightForWidth())
        self.main_tabWidget.setSizePolicy(sizePolicy)
        self.main_tabWidget.setTabsClosable(False)
        self.accounts_tab = QWidget()
        self.accounts_tab.setObjectName(u"accounts_tab")
        self.main_tabWidget.addTab(self.accounts_tab, "")
        self.transactions_tab = QWidget()
        self.transactions_tab.setObjectName(u"transactions_tab")
        self.transactions_tab.setEnabled(True)
        self.horizontalLayout_2 = QHBoxLayout(self.transactions_tab)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.splitter_2 = QSplitter(self.transactions_tab)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Vertical)
        self.transaction_table = QTableWidget(self.splitter_2)
        self.transaction_table.setObjectName(u"transaction_table")
        self.transaction_table.setEnabled(True)
        sizePolicy.setHeightForWidth(self.transaction_table.sizePolicy().hasHeightForWidth())
        self.transaction_table.setSizePolicy(sizePolicy)
        self.transaction_table.setMinimumSize(QSize(0, 344))
        self.transaction_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.transaction_table.setAlternatingRowColors(False)
        self.transaction_table.setSortingEnabled(True)
        self.splitter_2.addWidget(self.transaction_table)
        self.transaction_table.horizontalHeader().setCascadingSectionResizes(False)
        self.transaction_table.horizontalHeader().setStretchLastSection(True)
        self.transaction_table.verticalHeader().setCascadingSectionResizes(False)
        self.layoutWidget = QWidget(self.splitter_2)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(Qt.LeftToRight)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 2)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 0, 3, 1, 1)

        self.transactionDateEdit = QDateEdit(self.layoutWidget)
        self.transactionDateEdit.setObjectName(u"transactionDateEdit")
        self.transactionDateEdit.setDate(QDate(2023, 1, 1))

        self.gridLayout.addWidget(self.transactionDateEdit, 1, 0, 1, 1)

        self.accountComboBox = QComboBox(self.layoutWidget)
        self.accountComboBox.setObjectName(u"accountComboBox")
        self.accountComboBox.setFont(font)
        self.accountComboBox.setContextMenuPolicy(Qt.NoContextMenu)
        self.accountComboBox.setEditable(False)

        self.gridLayout.addWidget(self.accountComboBox, 1, 1, 1, 1)

        self.amountLineEdit = QLineEdit(self.layoutWidget)
        self.amountLineEdit.setObjectName(u"amountLineEdit")

        self.gridLayout.addWidget(self.amountLineEdit, 1, 2, 1, 2)

        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout.setColumnMinimumWidth(2, 1)
        self.splitter_2.addWidget(self.layoutWidget)
        self.splitter = QSplitter(self.splitter_2)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Vertical)
        self.descriptionTextEdit = QPlainTextEdit(self.splitter)
        self.descriptionTextEdit.setObjectName(u"descriptionTextEdit")
        self.descriptionTextEdit.setContextMenuPolicy(Qt.NoContextMenu)
        self.descriptionTextEdit.setTabChangesFocus(True)
        self.descriptionTextEdit.setOverwriteMode(False)
        self.splitter.addWidget(self.descriptionTextEdit)
        self.memoTextEdit = QPlainTextEdit(self.splitter)
        self.memoTextEdit.setObjectName(u"memoTextEdit")
        self.memoTextEdit.setTabChangesFocus(True)
        self.memoTextEdit.setOverwriteMode(False)
        self.splitter.addWidget(self.memoTextEdit)
        self.splitter_2.addWidget(self.splitter)
        self.addTransactionButton = QPushButton(self.splitter_2)
        self.addTransactionButton.setObjectName(u"addTransactionButton")
        self.splitter_2.addWidget(self.addTransactionButton)

        self.horizontalLayout_2.addWidget(self.splitter_2)

        self.main_tabWidget.addTab(self.transactions_tab, "")

        self.horizontalLayout.addWidget(self.main_tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1183, 21))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuWindow = QMenu(self.menubar)
        self.menuWindow.setObjectName(u"menuWindow")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuWindow.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionopen)
        self.menuFile.addAction(self.actionsave)

        self.retranslateUi(MainWindow)

        self.main_tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionopen.setText(QCoreApplication.translate("MainWindow", u"open", None))
        self.actionsave.setText(QCoreApplication.translate("MainWindow", u"save", None))
        self.main_tabWidget.setTabText(self.main_tabWidget.indexOf(self.accounts_tab), QCoreApplication.translate("MainWindow", u"My Accounts", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Date", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"From Account", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Amount", None))
        self.accountComboBox.setCurrentText("")
        self.amountLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.descriptionTextEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Description", None))
        self.memoTextEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Memo", None))
        self.addTransactionButton.setText(QCoreApplication.translate("MainWindow", u"Add Transaction", None))
        self.main_tabWidget.setTabText(self.main_tabWidget.indexOf(self.transactions_tab), QCoreApplication.translate("MainWindow", u"Transactions", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.menuWindow.setTitle(QCoreApplication.translate("MainWindow", u"Window", None))
    # retranslateUi

