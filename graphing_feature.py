from PySide6.QtCharts import QChart, QChartView, QPieSeries
from PySide6.QtCore import Qt
from PySide6.QtGui import QPainter
from PySide6.QtWidgets import QDialog, QSplitter

from data_base_module import TransactionDatabase
from graphing_criteria_Dialog import Ui_Dialog


class GraphingCriteriaWindow(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        # Move window
        self.move(400, 100)

        self.account_chart_splitter = QSplitter()
        self.category_chart_splitter = QSplitter()

        # Connect buttons
        self.pushButton_graph_accounts.clicked.connect(self.account_pie_charts)
        self.pushButton_graph_transaciton_categories.clicked.connect(self.transaction_categories_pie_charts)

        # Set connection to database
        self.db = TransactionDatabase()

        # Flag to track whether charts are displayed
        self.account_charts_displayed = False
        self.transaction_charts_displayed = False

    def open_window(self):
        self.exec()

    def account_pie_charts(self):
        if self.transaction_charts_displayed:
            self.category_chart_splitter.deleteLater()
            self.transaction_charts_displayed = False
            self.category_chart_splitter = QSplitter()
        if not self.account_charts_displayed:

            # Create asset pie chart
            asset_chart = QChart()
            asset_series = QPieSeries()
            asset_chart_view = QChartView(asset_chart)
            asset_chart_view.setRenderHint(QPainter.Antialiasing)
            asset_chart.addSeries(asset_series)
            asset_chart.setTitle('Account Totals')
            asset_chart.legend().setAlignment(Qt.AlignLeft)

            # Create debt pie chart
            debt_chart = QChart()
            debt_series = QPieSeries()
            debt_chart_view = QChartView(debt_chart)
            debt_chart_view.setRenderHint(QPainter.Antialiasing)
            debt_chart.addSeries(debt_series)
            debt_chart.setTitle('Debt Totals')
            debt_chart.legend().setAlignment(Qt.AlignLeft)

            # get data from database
            data = self.db.pie_chart_data("accounts_database")

            # Populate asset pie charts with data
            for account_info in data:
                if float(account_info[2]) >= 1:
                    asset_series.append(account_info[0], float(account_info[2]))
                    slice_label = f"{account_info[0]}\nTotal Amount: {str(account_info[2])}"
                    asset_series.slices()[-1].setLabel(slice_label)
                elif float(account_info[2]) < 0:
                    debt_series.append(account_info[0], float(account_info[2]))
                    slice_label = f"{account_info[0]}\nTotal Amount: {str(account_info[2])}"
                    debt_series.slices()[-1].setLabel(slice_label)

            # Add pie charts to splitter
            self.account_chart_splitter.setObjectName(u"account_chart_splitter")
            self.account_chart_splitter.setOrientation(Qt.Vertical)
            self.account_chart_splitter.addWidget(asset_chart_view)
            self.account_chart_splitter.addWidget(debt_chart_view)
            self.account_chart_splitter.setSizes([1, 1])

            # Place splitter in window
            self.verticalLayout.addWidget(self.account_chart_splitter)
            self.resize(900, 900)

            # Set flag to True
            self.account_charts_displayed = True

    def transaction_categories_pie_charts(self):
        if self.account_charts_displayed:
            self.account_chart_splitter.deleteLater()
            self.account_charts_displayed = False
            self.account_chart_splitter = QSplitter()
        if not self.transaction_charts_displayed:

            # Create category series
            category_income_series = QPieSeries()
            category_spent_series = QPieSeries()

            # get data from database
            data = self.db.pie_chart_data("transaction_categories")

            # Create category charts
            category_income_chart = QChart()
            category_income_view = QChartView(category_income_chart)
            category_income_view.setRenderHint(QPainter.Antialiasing)
            category_spent_chart = QChart()
            category_spent_view = QChartView(category_spent_chart)
            category_spent_view.setRenderHint(QPainter.Antialiasing)

            # Populate category pie charts with data
            for account_info in data:
                if float(account_info[1]) >= 1:
                    category_income_series.append(account_info[0], float(account_info[1]))
                    slice_label = f"{account_info[0]}\nTotal Amount: {str(account_info[1])}"
                    category_income_series.slices()[-1].setLabel(slice_label)
                elif float(account_info[1]) < 0:
                    category_spent_series.append(account_info[0], float(account_info[1]))
                    slice_label = f"{account_info[0]}\nTotal Amount: {str(account_info[1])}"
                    category_spent_series.slices()[-1].setLabel(slice_label)

            # Create Category Totals(Income) pie chart
            category_income_chart.addSeries(category_income_series)
            category_income_chart.setTitle('Category Totals(Income)')
            category_income_chart.legend().setAlignment(Qt.AlignLeft)
            category_income_view = QChartView(category_income_chart)

            # Create debt pie chart
            category_spent_chart.addSeries(category_spent_series)
            category_spent_chart.setTitle('Category Totals(Spent)')
            category_spent_chart.legend().setAlignment(Qt.AlignLeft)
            category_spent_view = QChartView(category_spent_chart)

            # Add pie charts to splitter
            self.category_chart_splitter.setObjectName(u"category_chart_splitter")
            self.category_chart_splitter.setOrientation(Qt.Vertical)
            self.category_chart_splitter.addWidget(category_income_view)
            self.category_chart_splitter.addWidget(category_spent_view)
            self.category_chart_splitter.setSizes([1, 1])

            # Place splitter in window
            self.verticalLayout.addWidget(self.category_chart_splitter)
            self.resize(900, 900)

            # Set flag to True
            self.transaction_charts_displayed = True
