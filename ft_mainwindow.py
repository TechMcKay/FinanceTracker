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
    QGridLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPlainTextEdit,
    QPushButton, QSizePolicy, QSplitter, QStatusBar,
    QTabWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
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
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
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
        self.verticalLayout_2 = QVBoxLayout(self.transactions_tab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.splitter_2 = QSplitter(self.transactions_tab)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Vertical)
        self.splitter = QSplitter(self.splitter_2)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.transactionFilterLineEdit = QLineEdit(self.splitter)
        self.transactionFilterLineEdit.setObjectName(u"transactionFilterLineEdit")
        self.transactionFilterLineEdit.setAlignment(Qt.AlignCenter)
        self.splitter.addWidget(self.transactionFilterLineEdit)
        self.transactionFilterButton = QPushButton(self.splitter)
        self.transactionFilterButton.setObjectName(u"transactionFilterButton")
        self.splitter.addWidget(self.transactionFilterButton)
        self.clearTransactionFilterButton = QPushButton(self.splitter)
        self.clearTransactionFilterButton.setObjectName(u"clearTransactionFilterButton")
        self.splitter.addWidget(self.clearTransactionFilterButton)
        self.deleteTransactionButton = QPushButton(self.splitter)
        self.deleteTransactionButton.setObjectName(u"deleteTransactionButton")
        self.splitter.addWidget(self.deleteTransactionButton)
        self.splitter_2.addWidget(self.splitter)
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

        self.verticalLayout_2.addWidget(self.splitter_2)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label = QLabel(self.transactions_tab)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(self.transactions_tab)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(Qt.LeftToRight)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_2, 0, 1, 1, 1)

        self.label_3 = QLabel(self.transactions_tab)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_3, 0, 2, 1, 1)

        self.transactionDateEdit = QDateEdit(self.transactions_tab)
        self.transactionDateEdit.setObjectName(u"transactionDateEdit")
        self.transactionDateEdit.setDate(QDate(2023, 1, 1))

        self.gridLayout_2.addWidget(self.transactionDateEdit, 1, 0, 1, 1)

        self.accountComboBox = QComboBox(self.transactions_tab)
        self.accountComboBox.setObjectName(u"accountComboBox")
        self.accountComboBox.setFont(font)
        self.accountComboBox.setContextMenuPolicy(Qt.NoContextMenu)
        self.accountComboBox.setEditable(False)

        self.gridLayout_2.addWidget(self.accountComboBox, 1, 1, 1, 1)

        self.amountLineEdit = QLineEdit(self.transactions_tab)
        self.amountLineEdit.setObjectName(u"amountLineEdit")

        self.gridLayout_2.addWidget(self.amountLineEdit, 1, 2, 1, 1)

        self.gridLayout_2.setColumnStretch(1, 1)

        self.verticalLayout_2.addLayout(self.gridLayout_2)

        self.splitter_3 = QSplitter(self.transactions_tab)
        self.splitter_3.setObjectName(u"splitter_3")
        self.splitter_3.setOrientation(Qt.Horizontal)
        self.descriptionTextEdit = QPlainTextEdit(self.splitter_3)
        self.descriptionTextEdit.setObjectName(u"descriptionTextEdit")
        self.descriptionTextEdit.setContextMenuPolicy(Qt.NoContextMenu)
        self.descriptionTextEdit.setTabChangesFocus(True)
        self.descriptionTextEdit.setOverwriteMode(False)
        self.splitter_3.addWidget(self.descriptionTextEdit)
        self.memoTextEdit = QPlainTextEdit(self.splitter_3)
        self.memoTextEdit.setObjectName(u"memoTextEdit")
        self.memoTextEdit.setTabChangesFocus(True)
        self.memoTextEdit.setOverwriteMode(False)
        self.splitter_3.addWidget(self.memoTextEdit)

        self.verticalLayout_2.addWidget(self.splitter_3)

        self.addTransactionButton = QPushButton(self.transactions_tab)
        self.addTransactionButton.setObjectName(u"addTransactionButton")

        self.verticalLayout_2.addWidget(self.addTransactionButton)

        self.main_tabWidget.addTab(self.transactions_tab, "")

        self.verticalLayout.addWidget(self.main_tabWidget)

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
        QWidget.setTabOrder(self.main_tabWidget, self.transactionFilterLineEdit)
        QWidget.setTabOrder(self.transactionFilterLineEdit, self.transactionFilterButton)
        QWidget.setTabOrder(self.transactionFilterButton, self.clearTransactionFilterButton)
        QWidget.setTabOrder(self.clearTransactionFilterButton, self.deleteTransactionButton)
        QWidget.setTabOrder(self.deleteTransactionButton, self.transaction_table)
        QWidget.setTabOrder(self.transaction_table, self.transactionDateEdit)
        QWidget.setTabOrder(self.transactionDateEdit, self.accountComboBox)
        QWidget.setTabOrder(self.accountComboBox, self.amountLineEdit)
        QWidget.setTabOrder(self.amountLineEdit, self.descriptionTextEdit)
        QWidget.setTabOrder(self.descriptionTextEdit, self.memoTextEdit)
        QWidget.setTabOrder(self.memoTextEdit, self.addTransactionButton)

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
        self.transactionFilterLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Add text here and press filter button to filter.", None))
        self.transactionFilterButton.setText(QCoreApplication.translate("MainWindow", u"Filter", None))
        self.clearTransactionFilterButton.setText(QCoreApplication.translate("MainWindow", u"Clear Filter", None))
        self.deleteTransactionButton.setText(QCoreApplication.translate("MainWindow", u"Delete Transaction", None))
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

