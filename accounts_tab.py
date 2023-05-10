from PySide6.QtCore import Qt
from PySide6.QtGui import QAction
from PySide6.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel
from PySide6.QtWidgets import (
    QTreeWidget, QTreeWidgetItem, QDialog, QPushButton, QLineEdit,
    QComboBox, QTabWidget
)
from add_account_window import Ui_Dialog
from data_base_module import TransactionDatabase
from ft_mainwindow import Ui_MainWindow


class AddAccountWindow(QDialog, Ui_Dialog):
    """Add Account Window"""

    def __init__(self, parent=None, accounts_tab=None, transaction_tab=None):
        super().__init__(parent)
        self.model = None
        self.add_account_ui = Ui_Dialog()
        self.add_account_ui.setupUi(self)
        self.accounts_tab = accounts_tab
        self.transaction_tab = transaction_tab

        self.account_name_lineEdit = self.findChild(QLineEdit, "account_name_lineEdit")
        self.account_category_comboBox = self.findChild(QComboBox, "account_category_comboBox")
        self.add_account_pushButton = self.findChild(QPushButton, "add_account_pushButton")
        self.add_account_pushButton.clicked.connect(self.add_account)

    def add_account(self):
        account_name = self.account_name_lineEdit.text()
        account_category = self.account_category_comboBox.currentText()
        account_category = account_category.title()
        if account_name and account_category:
            self.accounts_tab.db.add_account(account_name, account_category)
            # Update UI displays for user
            self.accounts_tab.populate_account_tree()
            # Checking to see if account_category already exists in the combo box
            if self.account_category_comboBox.findText(account_category) == -1:
                self.account_category_comboBox.addItem(account_category)
            # Clear user input
            self.account_name_lineEdit.clear()

        # Updating Transaction tab with new accounts
        self.transaction_tab.populate_account_combobox()
        self.transaction_tab.populate_payee_combobox()


class AccountsTab(Ui_MainWindow):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent

        # Creation of needed variables
        self.model = None

        # Setting up Accounts Tree(QTreeWidget)
        self.accounts_tree = self.parent.findChild(QTreeWidget, "accounts_tree")
        self.parent.accounts_tree.setColumnCount(2)
        self.parent.accounts_tree.setHeaderLabels(['Accounts', 'Amount'])
        self.parent.accounts_tree.setColumnWidth(0, 300)

        # Setting up Add Account window signals and connections
        self.actionAdd_Account = self.parent.findChild(QAction, "actionAdd_Account_2")
        self.actionAdd_Account.triggered.connect(self.open_add_account_window)
        self.main_tabWidget = self.parent.findChild(QTabWidget, "main_tabWidget")
        self.add_account_window = AddAccountWindow(self.parent, self, self.parent.transaction_tab)

        # set up transactions database connection
        self.db = TransactionDatabase()

        AccountsTab.populate_account_tree(self)

    def populate_account_tree(self):
        # Create a database connection
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('finance_tracker_data.db')

        # Open the connection to the database
        if db.open():

            # Clear existing data
            self.accounts_tree.clear()
            # Create a QSqlTableModel for the 'transaction_database' table
            self.model = QSqlTableModel(db=db)
            self.model.setTable('accounts_database')
            self.model.select()

            # Set up and execute query
            query = QSqlQuery(self.model.database())
            query_text = "SELECT * FROM accounts_database ORDER BY 'Type of Account'"
            query.exec(query_text)

            # Create dictionary of parents and children
            data_dict = {}
            while query.next():
                tree_parent = query.value(1)
                child = query.value(0)
                amount = query.value(2)
                if tree_parent not in data_dict:
                    data_dict[tree_parent] = []
                data_dict[tree_parent].append((child, amount))

            # Populate tree with dictionary
            for tree_parent, children in data_dict.items():
                parent_item = QTreeWidgetItem(self.accounts_tree, [tree_parent])
                for child in children:
                    child_item = QTreeWidgetItem(parent_item, child)
                    child_item.setText(1, str(child[1]))
                self.accounts_tree.insertTopLevelItem(0, parent_item)
                parent_item.setExpanded(True)
            # Close Query connection
            query.clear()
            # Sort tree view
            self.accounts_tree.sortByColumn(0, Qt.AscendingOrder)

    def open_add_account_window(self):
        # Go to My Account tab
        self.main_tabWidget.setCurrentIndex(1)
        self.add_account_window.show()
        self.populate_account_category_combobox()

    def populate_account_category_combobox(self):
        account_categories = set(self.db.get_account_categories())
        self.add_account_window.account_category_comboBox.clear()
        self.add_account_window.account_category_comboBox.addItems(account_categories)
