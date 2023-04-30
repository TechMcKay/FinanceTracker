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
            column_names = '(Description, Category, Account, Payee, Amount, Date, Memo)'
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
        with self.conn:
            self.c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table_name,))
            result = self.c.fetchone()
            if result:
                self.c.execute(f"DROP TABLE {table_name}")
                print(f"Table '{table_name}' has been deleted.")
            else:
                print(f"Table '{table_name}' does not exist.")

    def delete_rows(self, rows):
        with self.conn:
            for row in rows:
                self.c.execute("DELETE FROM transaction_database WHERE id=?", (row,))

    def get_account_names(self):
        with self.conn:
            self.c.execute('SELECT "Name of Account" FROM accounts_database')
            account_types = [row[0] for row in self.c.fetchall()]
        return account_types

    def get_account_categories(self):
        with self.conn:
            self.c.execute('SELECT "Type of Account" FROM accounts_database')
            account_categories = [row[0] for row in self.c.fetchall()]
        return account_categories

    def get_transaction_categories(self):
        with self.conn:
            self.c.execute('SELECT transaction_category FROM transaction_categories')
            transaction_categories = [row[0] for row in self.c.fetchall()]
        return transaction_categories

    def add_transaction_category(self, text):
        text = text.title()
        with self.conn:
            self.c.execute('INSERT INTO transaction_categories VALUES (?,?)', (text, 0))

    def apply_amount_to_databases(self, account, amount, trans_category):
        with self.conn:
            self.c.execute(
                '''UPDATE accounts_database SET "Amount in Account" = "Amount in Account" + ?
                WHERE "Name of Account" = ?''', (amount, account))
            self.c.execute(
                '''UPDATE transaction_categories SET transaction_category_amount = transaction_category_amount + ?
                WHERE transaction_category = ?''', (amount, trans_category))


    def add_account(self, account_name, account_category):
        with self.conn:
            self.c.execute(
                f'INSERT INTO accounts_database ("Name of Account", "Type of Account", "Amount in Account")'
                f' VALUES ("{account_name}", "{account_category}", 0);')


# # Create connection to database
# db = TransactionDatabase()
#
# # Transaction database creation and testing code.
# transaction_table = "transaction_database"
# transaction_database_columns = '''(id INTEGER PRIMARY KEY AUTOINCREMENT,
#                                     Description TEXT,
#                                     Category TEXT,
#                                     Account TEXT,
#                                     Payee TEXT,
#                                     Amount NUMERIC,
#                                     Date DATE,
#                                     Memo TEXT)'''
#
# db.delete_table(transaction_table)
# db.create_table(transaction_table, transaction_database_columns)
#
# # Accounts database creation.
# accounts_table = "accounts_database"
# accounts_database_columns = '''('Name of Account' TEXT,
#                                 'Type of Account' TEXT,
#                                 'Amount in Account' NUMERIC)'''
# db.delete_table(accounts_table)
# db.create_table(accounts_table, accounts_database_columns)
#
# # Create transaction category database.
# transaction_categories_table = "transaction_categories"
# transaction_categories_columns = '''(transaction_category TEXT,
#                                     transaction_category_amount NUMERIC)'''
# db.delete_table(transaction_categories_table)
# db.create_table(transaction_categories_table, transaction_categories_columns)

# # Create account data
# db.add_account("US Bank Checking", "Checking")
# db.add_account("US Bank Savings", "Savings")
# db.add_account("Cash in Wallet", "Cash")
#
# # Create transaction categories
# db.add_transaction_category("Income")
# db.add_transaction_category("Recreation")
# db.add_transaction_category("Bills")
