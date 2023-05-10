import sys

from PySide6.QtWidgets import (
    QMainWindow, QApplication

)

from accounts_tab import AccountsTab
from ft_mainwindow import Ui_MainWindow
from graphing_feature import GraphingCriteriaWindow
from transaction_tab import TransactionTab


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        # Transaction Tab.
        self.transaction_tab = TransactionTab(self)
        # Accounts Tab
        self.accounts_tab = AccountsTab(self)
        # Connection to graphing_feature file
        self.graphing_criteria_dlg = GraphingCriteriaWindow()
        # Opens graphing_criteria_dlg
        self.actionCreate_Graphs_2.triggered.connect(self.graphing_criteria_dlg.open_window)


app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
