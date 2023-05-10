# FinanceTracker
This application was created to provide a simple solution for managing finances.

## Program Description:
This program allows users to easily track all of their financial accounts along with all transactions. Users can generate graphs in order to analyze the data to aid in financial decisions or just understand there overall financial position.
This program utilizes the following Python libraries:
		Pyside6 - To create user interface.
		SQLite3 - For storing and accessing data.

## Dependencies

In addition to the above libraries, you will need to have Python 3.x installed on your system to run FinanceTracker.

## How to install and run:
To install and run FinanceTracker, follow these steps:
1. Clone main branch from repository.
2. Install Pyside6 and SQlite3.
3. Run Main.py file.

## How to use Program:
When the main.py files is ran the program will open to the transaction tab. The required first steps you need to take are listed below:

1. Click on the file drop down menu.
2. Select "Add Account".  When the Add Account Window opens up type the name of the account you would like to add first in the first box. Then in the next box type the account type(i.e, Savings, Checking, Credit, Cash) and then press the add account button.  Repeat this step until all the accounts you would like to track are added and then close the window.
3. Click the file drop down menu again and click on "Add Transaction Category".  The Add Transaction Category window will open up.  Type in the first box the type of Transaction Category you would like to add(i.e., Bills, Transportation, Groceries, Housing, Utilities).  Repeat this step until all the different categories you would like are entered and then close the window.
	
After the steps above are completed you can now start recording transactions. To record a transaction follow these steps:
1. If not already on the transaction tab, click on it to to display it.
2. Fill out the boxes with the appropriate data(is required unless marked "optional"):
*  Date - This is the Date that the transaction was made.
*  Account - The account that the money is coming/going to.
*  Payee(optional, unless transferring from one account to another) - The business/person you are paying, or your account that your transferring to.
*  Category - The category that is associated with the transaction.
*  Amount - The amount that is associated with the transaction.  If you are spending money or transferring from the account the amount should be negative, if you are receiving money the amount should be positive.
*  Description - The description of the transaction.
*  Memo(optional) - Any other comments you may want to not on the transaction.
3. Press the "Add Transaction" button and the transaction will be recorded.

## Program Features:
*  Filter Transactions: If you would like to filter through your transaction, make sure you are on the transaction tab and at the top of the tab you will see a box that says "Type here to filter table".  Type in letters or numbers to filter the table by and the table will automatically start sorting.  To clear the filter just clear/delete the letters/numbers in the filter box that you just filled out.
*  Delete Transactions: To delete a transaction select one or multiple transactions in the table and press the "Delete Transaction" button.  The transaction will then be deleted.
*  Edit Transactions: To edit a transaction double click in the transaction cell(on the transaction table) and edit what you want to. Once done editing press enter or click somewhere else to exit out of the cell and save the edit.
*  Accounts Tab: Click on the Accounts tab to display all of your accounts and the amounts that are in them at that time.
*  Graphing: There are 2 pie chart functions that the program will create for you to analyze.  One is the Account Pie Charts that will show all your account totals in one pie chart and then will show all your debt accounts in another.  The other pie chart function will show all your positive categories(income) in one pie chart and show all your spending categories in the other.  To show these pie charts follow the steps listed below:
	1. Click the file drop down menu and select "Create Graphs" and the Graphing window will pop up.
	2. Depending on what graphs you want to analyze(Accounts/Transaction Categories) click the associated button and those graphs will populate in the graphing window.

## License:GNU GENERAL PUBLIC LICENSE