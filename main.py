from ft_mainwindow import Ui_MainWindow
from transaction_tab import TransactionTab
from accounts_tab import AccountsTab
from PySide6.QtGui import QAction
from PySide6.QtWidgets import (
    QMainWindow, QApplication, QLineEdit, QPushButton

)
from PySide6 import QtWidgets
import sys


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        # Transaction Tab.
        self.transaction_tab = TransactionTab(self)
        # Accounts Tab
        self.accounts_tab = AccountsTab(self)


app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
