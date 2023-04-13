import sqlite3
from datetime import datetime


class TransactionDatabase:
    def __init__(self):
        self.conn = sqlite3.connect('finance_tracker_data.db')
        self.c = self.conn.cursor()

    def create_table(self, table_name, column_names_str):
        with self.conn:
            self.c.execute(f'CREATE TABLE {table_name} {column_names_str}')

    def insert_row_of_data(self, database_table, data):
        with self.conn:
            column_names = '(Description, Category, Account, Amount, Date, Memo)'
            placeholders = ",".join("?" * len(data))
            self.c.execute(f"INSERT INTO {database_table} {column_names} VALUES ({placeholders})", data)

    def insert_type_of_account(self, database_table, data):
        with self.conn:
            column_names = '("Name of Account", "Type of Account", "Amount in Account")'
            placeholders = ",".join("?" * len(data))
            self.c.execute(f"INSERT INTO {database_table} {column_names} VALUES ({placeholders})", data)

    def close_connection(self):
        self.conn.close()

    def delete_table(self, table_name):
        self.c.execute(f"DROP TABLE {table_name}")

    def delete_rows(self, rows):
        with self.conn:
            for row in rows:
                self.c.execute("DELETE FROM transaction_database WHERE id=?", (row,))

    def get_account_names(self):
        with self.conn:
            self.c.execute('SELECT "Name of Account" FROM accounts_database')
            account_types = [row[0] for row in self.c.fetchall()]
        return account_types

    def get_transaction_categories(self):
        with self.conn:
            self.c.execute('SELECT transaction_category FROM transaction_categories')
            transaction_categories = [row[0] for row in self.c.fetchall()]
        return transaction_categories


    # def get_account_types(self):
    #     with self.conn:
    #         self.c.execute('SELECT "Type of Account" FROM accounts_database')
    #         account_types = [row[0] for row in self.c.fetchall()]
    #     return account_types


# db = TransactionDatabase()

# # Transaction database creation and testing code.
# transaction_table = "transaction_database"
# transaction_database_columns = '''(id INTEGER PRIMARY KEY AUTOINCREMENT,
#              Description TEXT,
#             Category TEXT,
#             Account TEXT,
#             Amount NUMERIC,
#             Date DATE,
#             Memo TEXT)'''
# transaction_database_data_testing = ('New Bike', 'Recreational', 'US Bank', 1, '1/10/2023', 'I get to ride!')
#
# # Accounts database creation and testing code.
# accounts_table = "accounts_database"
# accounts_database_columns = '''(id INTEGER PRIMARY KEY AUTOINCREMENT,
#              'Name of Account' TEXT,
#             'Type of Account' TEXT,
#             'Amount in Account' NUMERIC)'''
#
# accounts_database_data_testing = ('Wallet', 'Cash', 523)
# db.insert_type_of_account(accounts_table, accounts_database_data_testing)

# db.create_table(accounts_table, accounts_database_columns)
# db.insert_row_of_data(table, data_)
# db.delete_table(table)
