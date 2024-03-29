from PySide6.QtCore import Qt, QRegularExpression, QDate, Signal, QSortFilterProxyModel
from PySide6.QtGui import QRegularExpressionValidator, QAction
from PySide6.QtSql import QSqlDatabase, QSqlTableModel, QSqlQuery
from PySide6.QtWidgets import (
    QTableView, QPushButton, QDateEdit,
    QComboBox, QPlainTextEdit, QLineEdit, QAbstractItemView,
    QDialog, QMainWindow
)

from accounts_tab import AddAccountWindow, AccountsTab
from data_base_module import TransactionDatabase
from emptyTransaction_Dialog import Ui_Dialog
from ft_mainwindow import Ui_MainWindow
from payee_same_as_accountTransaction_Dialog import Ui_PayeeIsAccountDialog
from transactionCategoryWindow import Ui_transactionCategoryWindow


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


class PayeeSameAsAccountDlg(Ui_PayeeIsAccountDialog, QDialog):
    """Payee Same as Account Dialog Box"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)


class AmountDisplayProxyModel(QSortFilterProxyModel):
    def __init__(self, *args, **kwargs):
        super(AmountDisplayProxyModel, self).__init__(*args, **kwargs)

    def data(self, index, role):
        if role == Qt.DisplayRole and index.column() == 5:
            value = super(AmountDisplayProxyModel, self).data(index, role)
            if value is not None and value != '':
                if isinstance(value, (int, float)):
                    value = str(value)
                    if value != float:
                        value = float(value.replace(",", ""))
                    value = "{:,.2f}".format(value)
            else:
                value = ''

            # Add dollar sign to the formatted value
            if value != '':
                value = '$' + value

            return value
        return super(AmountDisplayProxyModel, self).data(index, role)


class TransactionTab(Ui_MainWindow):

    def __init__(self, parent):
        super().__init__()
        self.proxy_model = None
        self.model = None
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
        # Set up accounts_tab connections
        self.add_account_window = AddAccountWindow()
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
        self.payee_comboBox = self.parent.findChild(QComboBox, "payee_comboBox")
        # Set up amountLineEdit and formatting.
        self.amountLineEdit = self.parent.findChild(QLineEdit, "amountLineEdit")
        dollar_format = QRegularExpression(r'^-?\d{0,8}(\.\d{0,2})?$')
        validator = QRegularExpressionValidator(dollar_format)
        self.amountLineEdit.setValidator(validator)
        self.amountLineEdit.setMaxLength(11)

        # Set up signal for add transaction Category.
        self.actionEnter_Edit_Transaction_Categories = self.parent.findChild(QAction, "actionAdd_Transaction_Category_2")
        self.actionEnter_Edit_Transaction_Categories.triggered.connect(self.open_transaction_category_window)

        # Populate account names combo box with existing account names.
        self.populate_account_combobox()

        # Populate payee combobox with accounts
        self.populate_payee_combobox()

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
            # Format table
            self.transaction_table.resizeColumnsToContents()
            self.transaction_table.horizontalHeader().setStretchLastSection(True)

            # Connect the dataChanged signal to the submit_changes method
            QAbstractItemView.scrollToBottom(self.transaction_table)
            self.model.dataChanged.connect(self.submit_changes)
            db.close()
        else:
            print("Error: Unable to open the database.")

    def submit_changes(self):
        diff = None
        for row in range(self.model.rowCount()):
            # Check to see if the transaction value has changed and find difference in amounts
            if self.model.isDirty(self.model.index(row, 5)):
                dirty_record = self.model.record(row)
                row_id = dirty_record.value("id")
                # Get original row data
                query = QSqlQuery(self.model.database())
                query_string = f'SELECT * FROM transaction_database WHERE id = {row_id}'
                query.exec(query_string)
                query.first()
                original_record = query.record()
                original_amount = original_record.value("Amount")
                new_amount = dirty_record.value("Amount")
                # Variable creation to link to other databases
                account = dirty_record.value("Account")
                category = dirty_record.value("Category")
                payee = dirty_record.value("Payee")
                # Strip commas from string
                if type(original_amount) == str:
                    original_amount = original_amount.replace(",", "")
                if type(new_amount) == str:
                    new_amount = new_amount.replace(",", "")
                # Find difference in amounts
                diff = -1 * (float(original_amount) - float(new_amount))
                # Close connection
                query.clear()
            else:
                continue
        self.model.submitAll()
        if diff:
            self.db.apply_amount_to_databases(account, diff, category)
            self.transaction_table.resizeColumnsToContents()
            self.transaction_table.horizontalHeader().setStretchLastSection(True)
            if payee:
                diff = -1 * diff
                self.db.apply_amount_to_databases(payee, diff, category)

        AccountsTab.populate_account_tree(self.parent)

    # Add transactions to database.
    def add_transaction(self):
        description = self.descriptionTextEdit.toPlainText()
        category = self.categoryComboBox.currentText()
        category = category.title()
        account = self.accountComboBox.currentText()
        payee = self.payee_comboBox.currentText()
        amount_text = self.amountLineEdit.text()
        if amount_text:
            if amount_text != str:
                amount = "{:,.2f}".format(float(amount_text))
            else:
                amount = "{:,.2f}".format(amount_text)
            date = self.transactionDateEdit.date().toString("MM-dd-yyyy")
            memo = self.memoTextEdit.toPlainText()
            # Creation of data to add list
            data_to_add = [description, category, account, payee, amount, date, memo]
            # Checking for non NaN data
            if data_to_add[0] and data_to_add[1] and data_to_add[5]:
                # Check to see if account is the same as payee
                if account != payee:
                    self.db.apply_amount_to_databases(account, float(amount_text), category)
                    # Add data to transaction data base
                    self.db.insert_row_of_data("transaction_database", data_to_add)
                    self.model.select()  # Refresh the view with updated data

                    # Reformat table for content
                    self.transaction_table.resizeColumnsToContents()
                    self.transaction_table.horizontalHeader().setStretchLastSection(True)
                    QAbstractItemView.scrollToBottom(self.transaction_table)
                    # Clear Input Widgets
                    self.descriptionTextEdit.clear()
                    self.memoTextEdit.clear()
                    self.amountLineEdit.clear()
                    self.payee_comboBox.clear()
                    self.populate_payee_combobox()
                    # Check for Payee to be an account
                    account_names = self.db.get_account_names()
                    if payee in account_names:
                        self.db.apply_amount_to_databases(payee, (-1 * float(amount_text)), category)
                    AccountsTab.populate_account_tree(self.parent)
                else:
                    payee_is_account_dlg = PayeeSameAsAccountDlg(self.parent)
                    payee_is_account_dlg.exec()

            else:
                empty_transaction_dlg = EmptyTransactionDlg(self.parent)
                empty_transaction_dlg.exec()
        else:
            empty_transaction_dlg = EmptyTransactionDlg(self.parent)
            empty_transaction_dlg.exec()

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
        # Subtract value from other databases
        for row_id in selected_row_ids:
            query = QSqlQuery(self.model.database())
            query_string = f'SELECT * FROM transaction_database WHERE id = {row_id}'
            query.exec(query_string)
            query.first()
            row_data = query.record()
            amount_deleted = row_data.value("Amount")
            # Variable creation to link to other databases
            account = row_data.value("Account")
            category = row_data.value("Category")
            # Strip commas from string
            if type(amount_deleted) == str:
                amount_deleted = float(amount_deleted.replace(",", ""))
            amount_deleted = -1 * amount_deleted
            # Close connection
            query.clear()
            self.db.apply_amount_to_databases(account, amount_deleted, category)
        self.db.delete_rows(selected_row_ids)
        self.model.select()  # Refresh the view with updated data
        AccountsTab.populate_account_tree(self.parent)

    # Populate account names combo box.
    def populate_account_combobox(self):
        account_names = self.db.get_account_names()
        self.accountComboBox.clear()
        self.accountComboBox.addItems(account_names)
        model = self.accountComboBox.model()
        model.sort(0)

    def populate_payee_combobox(self):
        account_names = self.db.get_account_names()
        self.payee_comboBox.clear()
        self.payee_comboBox.addItems(account_names)
        model = self.payee_comboBox.model()
        model.sort(0)
        self.payee_comboBox.setCurrentIndex(-1)

    def populate_transaction_categories(self):
        transaction_categories = self.db.get_transaction_categories()
        self.categoryComboBox.clear()
        self.categoryComboBox.addItems(transaction_categories)
        model = self.categoryComboBox.model()
        model.sort(0)
        self.categoryComboBox.setCurrentIndex(0)
        self.payee_comboBox.setCurrentIndex(-1)

    def apply_filter(self, text):
        # Use a regular expression pattern for case-insensitive substring matching
        filter_pattern = QRegularExpression(f"(?i){text}")

        # Set the filter pattern for the proxy model
        self.proxy_model.setFilterRegularExpression(filter_pattern)

        # Set the filter key column to -1, which means the filter is applied to all columns
        self.proxy_model.setFilterKeyColumn(-1)

    def open_transaction_category_window(self):
        transaction_category_window = TransactionCategoryWindow(self.parent, self)
        transaction_category_window.new_category_signal.connect(self.add_new_transaction_category)
        transaction_category_window.show()

    def add_new_transaction_category(self, new_category_text):
        if new_category_text:
            new_category_text = new_category_text.title()
            if self.categoryComboBox.findText(new_category_text) != 0:
                self.db.add_transaction_category(new_category_text)
                self.populate_transaction_categories()
        else:
            print("No category added")
