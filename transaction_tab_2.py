import data_base_module
from ft_mainwindow import Ui_MainWindow
from data_base_module import TransactionDatabase
from emptyTransaction_Dialog import Ui_Dialog
from transactionCategoryWindow import Ui_transactionCategoryWindow
from PySide6.QtWidgets import (
    QTableView, QTableWidgetItem, QPushButton, QDateEdit,
    QComboBox, QPlainTextEdit, QLineEdit, QAbstractItemView,
    QDialog, QMainWindow, QStyledItemDelegate
)
from PySide6.QtSql import QSqlDatabase, QSqlTableModel
from PySide6 import QtWidgets
from PySide6.QtGui import QRegularExpressionValidator, QAction
from PySide6.QtCore import Qt, QRegularExpression, QDate, QIdentityProxyModel, Signal, QSortFilterProxyModel


class TransactionCategoryWindow(QMainWindow, Ui_transactionCategoryWindow):
    """Transaction Category Window"""
    new_category_signal = Signal(str)

    def __init__(self, parent=None, transaction_tab=None):
        super().__init__(parent)
        self.ui = Ui_transactionCategoryWindow()
        self.ui.setupUi(self)
        self.transaction_tab = transaction_tab
        self.ui.add_new_categoryButton.clicked.connect(self.emit_new_category_signal)

    def emit_new_category_signal(self):
        new_category_text = self.ui.transaction_category_lineEdit.text()
        self.new_category_signal.emit(new_category_text)
        self.ui.transaction_category_lineEdit.clear()


class EmptyTransactionDlg(Ui_Dialog, QDialog):
    """Transaction Empty Dialog Box"""

    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)


class AmountDisplayProxyModel(QSortFilterProxyModel):
    def __init__(self, *args, **kwargs):
        super(AmountDisplayProxyModel, self).__init__(*args, **kwargs)

    def data(self, index, role):
        if role == Qt.DisplayRole and index.column() == 4:
            value = super(AmountDisplayProxyModel, self).data(index, role)
            try:
                value = float(value)
                return "${:,.2f}".format(value)
            except ValueError:
                pass
        return super(AmountDisplayProxyModel, self).data(index, role)


class TransactionTab(QMainWindow):
    def __init__(self, parent):
        super().__init__()
        self.proxy_model = None
        self.model = None
        self.ui = Ui_MainWindow()
        self.parent = parent

        # Set up buttons and user inputs.
        self.deleteTransactionButton = self.parent.findChild(QPushButton, "deleteTransactionButton")
        self.filterLineEdit = self.parent.findChild(QLineEdit, "transactionFilterLineEdit")
        self.filterLineEdit.textChanged.connect(self.apply_filter)

        # Set up delete transaction button signal.
        self.deleteTransactionButton.clicked.connect(self.delete_transaction)
        # Set up transaction table connection
        self.transaction_table = self.parent.findChild(QTableView, "transaction_table")

        # set up transactions database connection.
        self.db = TransactionDatabase()

        # Call the create_table_model function
        self.create_table_model()

        # Add all inputs and signals for add transactions.
        self.parent.addTransactionButton.clicked.connect(self.add_transaction)
        self.descriptionTextEdit = self.parent.findChild(QPlainTextEdit, "descriptionTextEdit")
        self.transactionDateEdit = self.parent.findChild(QDateEdit, "transactionDateEdit")
        self.parent.transactionDateEdit.setDate(QDate.currentDate())
        self.categoryComboBox = self.parent.findChild(QComboBox, "categoryComboBox")
        self.memoTextEdit = self.parent.findChild(QPlainTextEdit, "memoTextEdit")
        self.accountComboBox = self.parent.findChild(QComboBox, "accountComboBox")
        # Set up amountLineEdit and formatting.
        self.amountLineEdit = self.parent.findChild(QLineEdit, "amountLineEdit")
        dollar_format = QRegularExpression(r'^-?\d{0,8}(\.\d{0,2})?$')
        validator = QRegularExpressionValidator(dollar_format)
        self.amountLineEdit.setValidator(validator)
        self.amountLineEdit.setMaxLength(11)

        # Populate account names combo box with existing account names.
        self.populate_account_combobox()

        # Populate transaction categories combobox.
        self.populate_transaction_categories()

    def create_table_model(self):
        # Create a database connection
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('finance_tracker_data.db')

        # Open the connection to the database
        if db.open():
            # Create a QSqlTableModel for the 'transaction_database' table
            self.model = QSqlTableModel(db=db)
            self.model.setTable('transaction_database')
            self.model.select()

            # Create an AmountDisplayProxyModel and set the source model
            self.proxy_model = AmountDisplayProxyModel()
            self.proxy_model.setSourceModel(self.model)

            # Set the proxy model for the transaction_table view
            self.transaction_table.setModel(self.proxy_model)

            # Hide the ID column
            self.transaction_table.hideColumn(0)
            self.transaction_table.resizeColumnsToContents()
            self.transaction_table.horizontalHeader().setStretchLastSection(True)

            # Connect the dataChanged signal to the submit_changes method
            self.model.dataChanged.connect(self.submit_changes)
            QAbstractItemView.scrollToBottom(self.transaction_table)
        else:
            print("Error: Unable to open the database.")

    # Add transactions to database.
    def add_transaction(self):
        description = self.descriptionTextEdit.toPlainText()
        category = self.categoryComboBox.currentText()
        category = category.title()
        account = self.accountComboBox.currentText()
        if self.amountLineEdit.text():
            amount = "{:,.2f}".format(float(self.amountLineEdit.text()))
        else:
            amount = False
        date = self.transactionDateEdit.date().toString("MM-dd-yyyy")
        memo = self.memoTextEdit.toPlainText()
        # Creation of data to add list.
        data_to_add = [description, category, account, amount, date, memo]
        # Checking for non NaN data.
        if data_to_add[0] and data_to_add[3]:
            # Add data to transaction data base.
            self.db.insert_row_of_data("transaction_database", data_to_add)
            self.model.select()  # Refresh the view with updated data
            QAbstractItemView.scrollToBottom(self.transaction_table)

            self.descriptionTextEdit.clear()
            self.memoTextEdit.clear()
            self.amountLineEdit.clear()
        else:
            empty_transaction_dlg = EmptyTransactionDlg(self.parent)
            empty_transaction_dlg.exec()

    def submit_changes(self):
        self.model.submitAll()

    def get_selected_rows(self):

        # Get the current selection model from the transaction_table view
        selection_model = self.transaction_table.selectionModel()

        # Get the selected rows as QModelIndexList
        selected_rows = selection_model.selectedRows()

        # Extract the row IDs from the QModelIndexList and map them to the source model
        source_row_ids = [self.proxy_model.mapToSource(index).data() for index in selected_rows]

        return source_row_ids

    def delete_transaction(self):
        selected_row_ids = self.get_selected_rows()
        self.db.delete_rows(selected_row_ids)
        self.model.select()  # Refresh the view with updated data

    # Populate account names combo box.
    def populate_account_combobox(self):
        account_names = self.db.get_account_names()
        self.accountComboBox.addItems(account_names)

    def populate_transaction_categories(self):
        transaction_categories = self.db.get_transaction_categories()
        self.categoryComboBox.addItems(transaction_categories)

    def apply_filter(self, text):
        # Use a regular expression pattern for case-insensitive substring matching
        filter_pattern = QRegularExpression(f"(?i){text}")

        # Set the filter pattern for the proxy model
        self.proxy_model.setFilterRegularExpression(filter_pattern)

        # Set the filter key column to -1, which means the filter is applied to all columns
        self.proxy_model.setFilterKeyColumn(-1)




