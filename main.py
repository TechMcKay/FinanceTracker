from ft_mainwindow import Ui_MainWindow
from PySide6.QtWidgets import QTableWidget, QTableWidgetItem
from PySide6 import QtWidgets
import pandas as pd

import sys


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.transaction_table = self.findChild(QTableWidget, "transaction_table")

        # Populate the transaction table with data
        data = pd.DataFrame([
            ["Apple", "1.00", "2023-03-10"],
            ["Banana", "0.50", "2023-03-09"],
            ["Orange", "0.75", "2023-03-08"]
        ], columns=['Description', 'Amount', 'Date'], index=['Row 1', 'Row 2', 'Row 3'])

        # Add the column names as the first row of the table
        self.transaction_table.setColumnCount(len(data.columns))
        self.transaction_table.setRowCount(len(data.index) + 1)
        for i, col_name in enumerate(data.columns):
            item = QTableWidgetItem(col_name)
            self.transaction_table.setItem(0, i, item)

        # Populate the remaining rows with the data
        for i, row in enumerate(data.itertuples(index=False), start=1):
            for j, cell in enumerate(row):
                item = QTableWidgetItem(str(cell))
                self.transaction_table.setItem(i, j, item)


app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
