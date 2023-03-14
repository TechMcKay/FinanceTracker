from ft_mainwindow import Ui_MainWindow
from emptyTransaction_Dialog import Ui_Dialog
from PySide6.QtWidgets import (
    QTableWidget, QTableWidgetItem, QPushButton, QDateEdit,
    QComboBox, QPlainTextEdit, QLineEdit, QDialog
)
from PySide6 import QtWidgets
from PySide6.QtGui import QRegularExpressionValidator, QValidator
from PySide6.QtCore import QRegularExpression

import pandas as pd
import openpyxl

import sys

# Import database spreadsheet
transaction_data = pd.read_excel('transactionsSpreadsheet.xlsx', 0, parse_dates=['Date'])
accounts_data = pd.read_excel('transactionsSpreadsheet.xlsx', 1)


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.transaction_table = self.findChild(QTableWidget, "transaction_table")
        # Creating addTransactionButton and signal
        self.addTransactionButton = self.findChild(QPushButton, "addTransactionButton")
        self.addTransactionButton.clicked.connect(self.addTransactionButton_wasClicked)
        # transactionDateEdit signal & variable creation
        self.transactionDateEdit = self.findChild(QDateEdit, "transactionDateEdit")
        # amountLineEdit signal and set Regular expression filter.
        self.amountLineEdit = self.findChild(QLineEdit, "amountLineEdit")
        dollar_format = QRegularExpression(r'^\d{0,8}(\.\d{0,2})?$')
        validator = QRegularExpressionValidator(dollar_format)
        self.amountLineEdit.setValidator(validator)
        self.amountLineEdit.setMaxLength(11)
        # accountComboBox population of account names
        self.accountComboBox = self.findChild(QComboBox, "accountComboBox")
        self.accountComboBox.addItems(accounts_data["Name of Account"])
        # descriptionTextEdit signals and variable creation
        self.descriptionTextEdit = self.findChild(QPlainTextEdit, "descriptionTextEdit")
        # memoTextEdit signals and variable creation
        self.memoTextEdit = self.findChild(QPlainTextEdit, "memoTextEdit")

        # New transaction created

    def addTransactionButton_wasClicked(self):

        description = self.descriptionTextEdit.toPlainText()
        account = self.accountComboBox.currentText()
        amount = self.amountLineEdit.text()
        date = self.transactionDateEdit.date().toString("MM-dd-yyyy")
        memo = self.memoTextEdit.toPlainText()

        data_to_add = [description, account, amount, date, memo]
        # Checking for NaN data.
        if data_to_add[0] and data_to_add[2]:

            # Add new row to transaction spreadsheet.
            transaction_spreadsheet = openpyxl.load_workbook("transactionsSpreadsheet.xlsx")
            sheet = transaction_spreadsheet['Sheet1']
            sheet.append(data_to_add)
            transaction_spreadsheet.save("transactionsSpreadsheet.xlsx")

            # Add new data to QTableWidget
            lastRowPosition = self.transaction_table.rowCount()
            self.transaction_table.insertRow(lastRowPosition)
            for i in range(self.transaction_table.columnCount()):
                item = QTableWidgetItem(str(data_to_add[i]))
                self.transaction_table.setItem(lastRowPosition, i, item)
        else:
            empty_transaction_dialog_window = EmptyTransactionDlg(self)
            empty_transaction_dialog_window.exec()






        # Add the column names as the first row of the table
        self.transaction_table.setColumnCount(len(transaction_data.columns))
        self.transaction_table.setRowCount(len(transaction_data.index))
        self.transaction_table.setHorizontalHeaderLabels(['Description', 'Amount', 'Date', 'Description', 'Memo'])

        # Populate the remaining rows with the data

        for i, row in enumerate(transaction_data.itertuples(index=False)):
            for j, cell in enumerate(row):
                item = QTableWidgetItem(str(cell))
                self.transaction_table.setItem(i, j, item)
                # Resize table to contents
                self.transaction_table.resizeColumnsToContents()
class EmptyTransactionDlg(Ui_Dialog, QDialog):
    """Transaction Empty Dialog Box"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)



app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
