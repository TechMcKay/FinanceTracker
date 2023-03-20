from ft_mainwindow import Ui_MainWindow
from emptyTransaction_Dialog import Ui_Dialog
from PySide6.QtWidgets import (
    QTableWidget, QTableWidgetItem, QPushButton, QDateEdit,
    QComboBox, QPlainTextEdit, QLineEdit, QDialog
)
from PySide6 import QtWidgets
from PySide6.QtGui import QRegularExpressionValidator
from PySide6.QtCore import QRegularExpression
import pandas as pd
import openpyxl
import sys

# Import database spreadsheet
transaction_data = pd.read_excel('transactionsSpreadsheet.xlsx', 0)

accounts_data = pd.read_excel('transactionsSpreadsheet.xlsx', 1)


class EmptyTransactionDlg(Ui_Dialog, QDialog):
    """Transaction Empty Dialog Box"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.transaction_table = self.findChild(QTableWidget, "transaction_table")
        # Transaction table modified signal creation.
        self.transaction_table.cellChanged.connect(self.transaction_table_modified)
        self.transaction_data_flag = False
        # Creating addTransactionButton and signal
        self.addTransactionButton = self.findChild(QPushButton, "addTransactionButton")
        self.addTransactionButton.clicked.connect(self.add_transaction_button_was_clicked)
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
        # Add the column names as the first row of the table
        self.transaction_table.setColumnCount(len(transaction_data.columns))
        self.transaction_table.setRowCount(len(transaction_data.index))
        self.transaction_table.setHorizontalHeaderLabels(
            ['Description', 'Account', 'Amount', 'Date', 'Memo'])

        # Populate transaction table with existing data

        for i, row in enumerate(transaction_data.itertuples(index=False)):
            for j, cell in enumerate(row):
                item = QTableWidgetItem(str(cell))
                # print(type(item))
                # Check for empty cells and replace with empty string.
                if item.text() == 'nan' or item.text() == 'NaT':
                    item = QTableWidgetItem('')
                self.transaction_table.setItem(i, j, item)
                # Resize table to contents
                self.transaction_table.resizeColumnsToContents()
        self.transaction_data_flag = True

    def transaction_table_modified(self, _row, _column):
        if self.transaction_data_flag:
            item = self.transaction_table.cellWidget(_row, _column)
            # Block signal while changing cell.
            self.transaction_table.blockSignals(True)
            self.transaction_table.setItem(_row, _column, QTableWidgetItem(item.text()))
            self.transaction_table.blockSignals(False)

            # Update spreadsheet with edited cell
            transaction_spreadsheet = openpyxl.load_workbook("transactionsSpreadsheet.xlsx")
            sheet = transaction_spreadsheet['Sheet1']
            # Add 2 to row(for header in spreadsheet and indexing used by openpyxl)
            # and 1 to column(indexing used by openpyxl).
            cell = sheet.cell(row=_row + 2, column=_column + 1)
            cell.value = item.text()
            transaction_spreadsheet.save("transactionsSpreadsheet.xlsx")

    # New transaction created method.
    def add_transaction_button_was_clicked(self):

        description = self.descriptionTextEdit.toPlainText()
        self.descriptionTextEdit.clear()
        account = self.accountComboBox.currentText()
        amount = self.amountLineEdit.text()
        date = self.transactionDateEdit.date().toString("MM-dd-yyyy")
        memo = self.memoTextEdit.toPlainText()
        self.memoTextEdit.clear()

        data_to_add = [description, account, amount, date, memo]
        # Checking for non NaN data.
        if data_to_add[0] and data_to_add[2]:

            # Add new row to transaction spreadsheet.
            transaction_spreadsheet = openpyxl.load_workbook("transactionsSpreadsheet.xlsx")
            sheet = transaction_spreadsheet['Sheet1']
            sheet.append(data_to_add)
            transaction_spreadsheet.save("transactionsSpreadsheet.xlsx")

            # Add new data to QTableWidget
            last_row_position = self.transaction_table.rowCount()
            self.transaction_table.insertRow(last_row_position)
            for i in range(self.transaction_table.columnCount()):
                if not data_to_add[i]:
                    data_to_add[i] = ''
                item = QTableWidgetItem(str(data_to_add[i]))
                self.transaction_table.setItem(last_row_position, i, item)
                self.transaction_table.resizeColumnsToContents()
                self.transaction_table.horizontalHeader().setStretchLastSection(True)
        # Dialog window pops up if cells required to be filler are empty.
        else:
            empty_transaction_dialog_window = EmptyTransactionDlg(self)
            empty_transaction_dialog_window.exec()


app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
