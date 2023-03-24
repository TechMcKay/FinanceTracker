from ft_mainwindow import Ui_MainWindow
from emptyTransaction_Dialog import Ui_Dialog
from PySide6.QtWidgets import (
    QTableWidget, QTableWidgetItem, QPushButton, QDateEdit,
    QComboBox, QPlainTextEdit, QLineEdit, QDialog, QAbstractItemView

)
from PySide6 import QtWidgets
from PySide6.QtGui import QRegularExpressionValidator
from PySide6.QtCore import QRegularExpression, QDate
import pandas as pd
import openpyxl
import sys

# Import database spreadsheet as data frame.
transaction_data = pd.read_excel('transactionsSpreadsheet.xlsx', 0)
accounts_data = pd.read_excel('transactionsSpreadsheet.xlsx', 1)

transaction_spreadsheet = openpyxl.load_workbook("transactionsSpreadsheet.xlsx")
transaction_sheet = transaction_spreadsheet['Sheet1']


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
        # Adding filter button and signal
        self.filterButton = self.findChild(QPushButton, "transactionFilterButton")
        self.filterButton.clicked.connect(self.filter_table)
        self.filterLineEdit = self.findChild(QLineEdit, "transactionFilterLineEdit")
        # Adding clear filter button.
        self.clearTransactionFilterButton = self.findChild(QPushButton, "clearTransactionFilterButton")
        self.clearTransactionFilterButton.clicked.connect(self.clear_transaction_filter)
        # Adding delete Transaction button and variable.
        self.deleteTransactionButton.findChild(QPushButton, "deleteTransactionButton")
        self.deleteTransactionButton.clicked.connect(self.delete_transaction)
        self.transaction_table.cellClicked.connect(self.transaction_table_cell_clicked)
        self.row = None
        # transactionDateEdit signal & variable creation
        self.transactionDateEdit = self.findChild(QDateEdit, "transactionDateEdit")
        self.transactionDateEdit.setDate(QDate.currentDate())
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
        QAbstractItemView.scrollToBottom(self.transaction_table)
        self.transaction_data_flag = True

    # Filter table function.
    def filter_table(self):
        # Get the user input from the filterLineEdit.
        filter_text = self.filterLineEdit.text()

        # If the filter is empty, show all the rows.
        if not filter_text:
            for i in range(self.transaction_table.rowCount()):
                self.transaction_table.setRowHidden(i, False)
        else:
            # Iterate over the rows of the table and hide the rows that do not match the filter.
            for i in range(self.transaction_table.rowCount()):
                match_found = False
                for j in range(self.transaction_table.columnCount()):
                    cell_text = self.transaction_table.item(i, j).text()
                    if filter_text.lower() in cell_text.lower():
                        match_found = True
                        break
                self.transaction_table.setRowHidden(i, not match_found)

    # Clear filter on transaction table function.
    def clear_transaction_filter(self):
        self.filterLineEdit.clear()
        self.filter_table()

    # Delete transaction function.
    def transaction_table_cell_clicked(self, row):
        self.row = row

    def delete_transaction(self):

        if self.row is not None:
            self.transaction_table.removeRow(self.row)

            # Save changes to spreadsheet
            transaction_sheet.delete_rows((self.row + 2))
            self.row = None
            transaction_spreadsheet.save("transactionsSpreadsheet.xlsx")

    def transaction_table_modified(self, _row, _column):
        if self.transaction_data_flag:
            # Convert cell text to QTableWidgetItem.
            item_text = self.transaction_table.item(_row, _column).text()
            item = QTableWidgetItem(item_text)
            # Block signal while changing cell in QTableWidget.
            self.transaction_table.blockSignals(True)
            self.transaction_table.setItem(_row, _column, QTableWidgetItem(item.text()))
            self.transaction_table.blockSignals(False)

            # Update spreadsheet with edited cell
            # Add 2 to row(for header in spreadsheet and indexing used by openpyxl)
            # and 1 to column(indexing used by openpyxl).
            cell = transaction_sheet.cell(row=_row + 2, column=_column + 1)
            cell.value = item.text()
            transaction_spreadsheet.save("transactionsSpreadsheet.xlsx")

    # New transaction created method.
    def add_transaction_button_was_clicked(self):

        description = self.descriptionTextEdit.toPlainText()
        account = self.accountComboBox.currentText()
        amount = self.amountLineEdit.text()
        date = self.transactionDateEdit.date().toString("MM-dd-yyyy")
        memo = self.memoTextEdit.toPlainText()

        data_to_add = [description, account, amount, date, memo]
        # Checking for non NaN data.
        if data_to_add[0] and data_to_add[2]:

            # Add new row to transaction spreadsheet.
            transaction_sheet.append(data_to_add)
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

                QAbstractItemView.scrollToBottom(self.transaction_table)
            # Clear box content for next transaction.
            self.descriptionTextEdit.clear()
            self.memoTextEdit.clear()
            self.amountLineEdit.clear()
        # Dialog window pops up if cells required to be filler are empty.
        else:
            empty_transaction_dialog_window = EmptyTransactionDlg(self)
            empty_transaction_dialog_window.exec()


app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
