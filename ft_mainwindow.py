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
    QStatusBar, QTabWidget, QTableView, QTreeWidget,
    QTreeWidgetItem, QVBoxLayout, QWidget)

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
        self.actionAdd_Transaction_Category = QAction(MainWindow)
        self.actionAdd_Transaction_Category.setObjectName(u"actionAdd_Transaction_Category")
        self.actionAdd_Account = QAction(MainWindow)
        self.actionAdd_Account.setObjectName(u"actionAdd_Account")
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
        font = QFont()
        font.setPointSize(12)
        self.transactionFilterLineEdit.setFont(font)
        self.transactionFilterLineEdit.setAlignment(Qt.AlignCenter)
        self.splitter.addWidget(self.transactionFilterLineEdit)
        self.deleteTransactionButton = QPushButton(self.splitter)
        self.deleteTransactionButton.setObjectName(u"deleteTransactionButton")
        self.deleteTransactionButton.setFont(font)
        self.splitter.addWidget(self.deleteTransactionButton)
        self.splitter_2.addWidget(self.splitter)
        self.transaction_table = QTableView(self.splitter_2)
        self.transaction_table.setObjectName(u"transaction_table")
        self.transaction_table.setEnabled(True)
        sizePolicy.setHeightForWidth(self.transaction_table.sizePolicy().hasHeightForWidth())
        self.transaction_table.setSizePolicy(sizePolicy)
        self.transaction_table.setMinimumSize(QSize(0, 344))
        self.transaction_table.setFont(font)
        self.transaction_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.transaction_table.setAlternatingRowColors(False)
        self.transaction_table.setSortingEnabled(False)
        self.splitter_2.addWidget(self.transaction_table)
        self.transaction_table.horizontalHeader().setHighlightSections(False)
        self.transaction_table.verticalHeader().setCascadingSectionResizes(True)
        self.transaction_table.verticalHeader().setHighlightSections(False)

        self.verticalLayout_2.addWidget(self.splitter_2)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label = QLabel(self.transactions_tab)
        self.label.setObjectName(u"label")
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

        self.gridLayout_2.addWidget(self.label_3, 0, 4, 1, 1)

        self.accountComboBox = QComboBox(self.transactions_tab)
        self.accountComboBox.setObjectName(u"accountComboBox")
        self.accountComboBox.setFont(font)
        self.accountComboBox.setContextMenuPolicy(Qt.NoContextMenu)
        self.accountComboBox.setEditable(False)

        self.gridLayout_2.addWidget(self.accountComboBox, 1, 1, 1, 1)

        self.transactionDateEdit = QDateEdit(self.transactions_tab)
        self.transactionDateEdit.setObjectName(u"transactionDateEdit")
        self.transactionDateEdit.setFont(font)
        self.transactionDateEdit.setDate(QDate(2023, 1, 1))

        self.gridLayout_2.addWidget(self.transactionDateEdit, 1, 0, 1, 1)

        self.amountLineEdit = QLineEdit(self.transactions_tab)
        self.amountLineEdit.setObjectName(u"amountLineEdit")
        self.amountLineEdit.setFont(font)

        self.gridLayout_2.addWidget(self.amountLineEdit, 1, 4, 1, 1)

        self.categoryComboBox = QComboBox(self.transactions_tab)
        self.categoryComboBox.setObjectName(u"categoryComboBox")
        self.categoryComboBox.setFont(font)
        self.categoryComboBox.setEditable(True)

        self.gridLayout_2.addWidget(self.categoryComboBox, 1, 3, 1, 1)

        self.label_4 = QLabel(self.transactions_tab)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_4, 0, 3, 1, 1)

        self.payee_comboBox = QComboBox(self.transactions_tab)
        self.payee_comboBox.setObjectName(u"payee_comboBox")
        self.payee_comboBox.setFont(font)
        self.payee_comboBox.setEditable(True)
        self.payee_comboBox.setCurrentText(u"")

        self.gridLayout_2.addWidget(self.payee_comboBox, 1, 2, 1, 1)

        self.payee_label = QLabel(self.transactions_tab)
        self.payee_label.setObjectName(u"payee_label")
        self.payee_label.setFont(font)
        self.payee_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.payee_label, 0, 2, 1, 1)

        self.gridLayout_2.setColumnStretch(1, 1)
        self.gridLayout_2.setColumnStretch(2, 1)
        self.gridLayout_2.setColumnStretch(3, 1)

        self.verticalLayout_2.addLayout(self.gridLayout_2)

        self.splitter_3 = QSplitter(self.transactions_tab)
        self.splitter_3.setObjectName(u"splitter_3")
        self.splitter_3.setOrientation(Qt.Horizontal)
        self.descriptionTextEdit = QPlainTextEdit(self.splitter_3)
        self.descriptionTextEdit.setObjectName(u"descriptionTextEdit")
        self.descriptionTextEdit.setFont(font)
        self.descriptionTextEdit.setContextMenuPolicy(Qt.NoContextMenu)
        self.descriptionTextEdit.setTabChangesFocus(True)
        self.descriptionTextEdit.setOverwriteMode(False)
        self.splitter_3.addWidget(self.descriptionTextEdit)
        self.memoTextEdit = QPlainTextEdit(self.splitter_3)
        self.memoTextEdit.setObjectName(u"memoTextEdit")
        self.memoTextEdit.setFont(font)
        self.memoTextEdit.setTabChangesFocus(True)
        self.memoTextEdit.setOverwriteMode(False)
        self.splitter_3.addWidget(self.memoTextEdit)

        self.verticalLayout_2.addWidget(self.splitter_3)

        self.addTransactionButton = QPushButton(self.transactions_tab)
        self.addTransactionButton.setObjectName(u"addTransactionButton")
        self.addTransactionButton.setFont(font)

        self.verticalLayout_2.addWidget(self.addTransactionButton)

        self.main_tabWidget.addTab(self.transactions_tab, "")
        self.add_account_window = QWidget()
        self.add_account_window.setObjectName(u"accounts_tab")
        self.verticalLayout = QVBoxLayout(self.add_account_window)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.accounts_tree = QTreeWidget(self.add_account_window)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.accounts_tree.setHeaderItem(__qtreewidgetitem)
        self.accounts_tree.setObjectName(u"accounts_tree")

        self.verticalLayout.addWidget(self.accounts_tree)

        self.main_tabWidget.addTab(self.add_account_window, "")
        self.graph_tab = QWidget()
        self.graph_tab.setObjectName(u"graph_tab")
        self.main_tabWidget.addTab(self.graph_tab, "")

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
        QWidget.setTabOrder(self.main_tabWidget, self.transactionFilterLineEdit)
        QWidget.setTabOrder(self.transactionFilterLineEdit, self.deleteTransactionButton)
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
        self.menuEdit.addAction(self.actionAdd_Transaction_Category)
        self.menuEdit.addAction(self.actionAdd_Account)

        self.retranslateUi(MainWindow)

        self.main_tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionopen.setText(QCoreApplication.translate("MainWindow", u"open", None))
        self.actionsave.setText(QCoreApplication.translate("MainWindow", u"save", None))
        self.actionAdd_Transaction_Category.setText(QCoreApplication.translate("MainWindow", u"Add Transaction Category", None))
        self.actionAdd_Account.setText(QCoreApplication.translate("MainWindow", u"Add Account", None))
        self.transactionFilterLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here to filter table", None))
        self.deleteTransactionButton.setText(QCoreApplication.translate("MainWindow", u"Delete Transaction", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Date", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Account", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Amount", None))
        self.accountComboBox.setCurrentText("")
        self.amountLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.categoryComboBox.setCurrentText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Category", None))
        self.payee_label.setText(QCoreApplication.translate("MainWindow", u"Payee", None))
        self.descriptionTextEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Description", None))
        self.memoTextEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Memo", None))
        self.addTransactionButton.setText(QCoreApplication.translate("MainWindow", u"Add Transaction", None))
        self.main_tabWidget.setTabText(self.main_tabWidget.indexOf(self.transactions_tab), QCoreApplication.translate("MainWindow", u"Transactions", None))
        self.main_tabWidget.setTabText(self.main_tabWidget.indexOf(self.add_account_window), QCoreApplication.translate("MainWindow", u"My Accounts", None))
        self.main_tabWidget.setTabText(self.main_tabWidget.indexOf(self.graph_tab), QCoreApplication.translate("MainWindow", u"Graphs", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.menuWindow.setTitle(QCoreApplication.translate("MainWindow", u"Window", None))
    # retranslateUi

