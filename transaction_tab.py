from ft_mainwindow import Ui_MainWindow
from emptyTransaction_Dialog import Ui_Dialog
from PySide6.QtWidgets import (
    QTableWidget, QTableWidgetItem, QPushButton, QDateEdit,
    QComboBox, QPlainTextEdit, QLineEdit, QAbstractItemView,
    QDialog, QMainWindow
)
from PySide6.QtGui import QRegularExpressionValidator
from PySide6.QtCore import QRegularExpression, QDate
import pandas as pd
import openpyxl

transaction_data = pd.read_excel('transactionsSpreadsheet.xlsx', 0)
accounts_data = pd.read_excel('transactionsSpreadsheet.xlsx', 1)

transaction_spreadsheet = openpyxl.load_workbook("transactionsSpreadsheet.xlsx")
transaction_sheet = transaction_spreadsheet['Sheet1']


class EmptyTransactionDlg(Ui_Dialog, QDialog):
    """Transaction Empty Dialog Box"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)


class TransactionTab(Ui_MainWindow):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent

        self.transaction_table = self.parent.findChild(QTableWidget, "transaction_table")
        self.transaction_table.cellChanged.connect(self.transaction_table_modified)
        self.transaction_data_flag = False
        self.parent.addTransactionButton.clicked.connect(self.add_transaction_button_was_clicked)
        self.parent.filterButton.clicked.connect(self.filter_table)
        self.parent.deleteTransactionButton = self.parent.findChild(QPushButton, "deleteTransactionButton")
        self.parent.deleteTransactionButton.clicked.connect(self.delete_transaction)
        self.transaction_table.cellClicked.connect(self.transaction_table_cell_clicked)
        self.row = None
        self.parent.transactionDateEdit = self.parent.findChild(QDateEdit, "transactionDateEdit")
        self.parent.transactionDateEdit.setDate(QDate.currentDate())
        self.parent.amountLineEdit = self.parent.findChild(QLineEdit, "amountLineEdit")
        dollar_format = QRegularExpression(r'^\d{0,8}(\.\d{0,2})?$')
        validator = QRegularExpressionValidator(dollar_format)
        self.parent.amountLineEdit.setValidator(validator)
        self.parent.amountLineEdit.setMaxLength(11)
        self.parent.accountComboBox = self.parent.findChild(QComboBox, "accountComboBox")
        self.parent.accountComboBox.addItems(accounts_data["Name of Account"])
        self.parent.descriptionTextEdit = self.parent.findChild(QPlainTextEdit, "descriptionTextEdit")
        self.parent.memoTextEdit = self.parent.findChild(QPlainTextEdit, "memoTextEdit")
        self.transaction_table.setColumnCount(len(transaction_data.columns))
        self.transaction_table.setRowCount(len(transaction_data.index))
        self.transaction_table.setHorizontalHeaderLabels(
            ['Description', 'Account', 'Amount', 'Date', 'Memo'])

        for i, row in enumerate(transaction_data.itertuples(index=False)):
            for j, cell in enumerate(row):
                item = QTableWidgetItem(str(cell))
                if item.text() == 'nan' or item.text() == 'NaT':
                    item = QTableWidgetItem('')
                self.transaction_table.setItem(i, j, item)
                self.transaction_table.resizeColumnsToContents()
        QAbstractItemView.scrollToBottom(self.transaction_table)
        self.transaction_data_flag = True

    # Filter table function.
    def filter_table(self):
        # Get the user input from the filterLineEdit.
        filter_text = self.parent.filterLineEdit.text()

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
        self.parent.filterLineEdit.clear()
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
        print("add_transaction_button_was_clicked called")
        description = self.parent.descriptionTextEdit.toPlainText()
        account = self.parent.accountComboBox.currentText()
        amount = self.parent.amountLineEdit.text()
        date = self.parent.transactionDateEdit.date().toString("MM-dd-yyyy")
        memo = self.parent.memoTextEdit.toPlainText()

        data_to_add = [description, account, amount, date, memo]
        # Checking for non NaN data.
        if data_to_add[0] and data_to_add[2]:

            # Add new row to transaction spreadsheet.
            transaction_sheet.append(data_to_add)
            transaction_spreadsheet.save("transactionsSpreadsheet.xlsx")

            # Add new data to QTableWidget
            last_row_position = self.parent.transaction_table.rowCount()
            self.parent.transaction_table.insertRow(last_row_position)
            for i in range(self.parent.transaction_table.columnCount()):
                if not data_to_add[i]:
                    data_to_add[i] = ''
                item = QTableWidgetItem(str(data_to_add[i]))
                self.parent.transaction_table.setItem(last_row_position, i, item)
                self.parent.transaction_table.resizeColumnsToContents()
                self.parent.transaction_table.horizontalHeader().setStretchLastSection(True)

                QAbstractItemView.scrollToBottom(self.transaction_table)
            # Clear box content for next transaction.
            self.parent.descriptionTextEdit.clear()
            self.parent.memoTextEdit.clear()
            self.parent.amountLineEdit.clear()
        # Dialog window pops up if cells required to be filler are empty.
        else:
            empty_transaction_dlg = EmptyTransactionDlg(self.parent)
            empty_transaction_dlg.exec()
