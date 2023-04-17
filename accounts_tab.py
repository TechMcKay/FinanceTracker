from PySide6.QtWidgets import (
    QTreeWidget, QTreeWidgetItem
)
from PySide6.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel
from ft_mainwindow import Ui_MainWindow
from data_base_module import TransactionDatabase


class AccountsTab(Ui_MainWindow):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent

        # Creation of need variables
        self.model = None

        # Setting up Accounts Tree(QTreeWidget).
        self.accounts_tree = self.parent.accounts_tree.findChild(QTreeWidget, "accounts_tree")
        self.parent.accounts_tree.setColumnCount(2)
        self.parent.accounts_tree.setHeaderLabels(['Accounts', 'Amount'])
        self.parent.accounts_tree.setColumnWidth(0, 300)

        # set up transactions database connection.
        self.db = TransactionDatabase()

        # Create a database connection
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('finance_tracker_data.db')

        # Open the connection to the database
        if db.open():
            # Create a QSqlTableModel for the 'transaction_database' table
            self.model = QSqlTableModel(db=db)
            self.model.setTable('accounts_database')
            self.model.select()

            # Set up and execute query
            query = QSqlQuery(self.model.database())
            query_text = 'SELECT * FROM accounts_database'
            query.exec(query_text)

            # Create dictionary of parents and children
            data_dict = {}
            while query.next():
                print(query.value(1))
                print(query.value(2))
                print(query.value(3))
                tree_parent = query.value(2)
                child = query.value(1)
                amount = query.value(3)
                if tree_parent not in data_dict:
                    data_dict[tree_parent] = []
                data_dict[tree_parent].append((child,amount))

            print(data_dict.items())

            # Populate tree with dictionary
            for tree_parent, children in data_dict.items():
                parent_item = QTreeWidgetItem(self.accounts_tree, [tree_parent])
                for child in children:
                    child_item = QTreeWidgetItem(parent_item, child)
                    child_item.setText(1, str(child[1]))
                ## Not sure how to get the tree to populate from here
                self.parent.accounts_tree.insertTopLevelItem(0, parent_item)
                parent_item.setExpanded(True)
            self.db.close_connection()