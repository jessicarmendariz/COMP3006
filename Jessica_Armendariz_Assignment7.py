#Week 7 Assignment – Loan Repayment Calculator

#In this assignment you will create a loan repayment calculator inspired by many of the online repayment calculators available like this one:
#https://www.calculator.net/loan-calculator.html?cloanamount=100,000&cloanterm=10&cloantermmonth=0&cinterestrate=6&ccompound=monthly&cpayback=month&x=Calculate&type=1#monthlyfixedr
#Please visit the website and see how to interact with the calculator. 
#You will write some of the code necessary for the backend computations, le creation and record keeping that is needed for the application. 
#The GUI (Graphic User Interface) will be provided and will not require any coding on your part. 
#You’re of course welcome to look at the source code.
#Your job will be to write classes, functions and create multiple les that make this application tick. 
#Projects like this are common when developing software, you’re given code from someone that you have to expand upon.
#The les you will create are for amortization tables and others will be log les. 
#You must pass the AmortizationTable class to the DebtAPP instance, i.e. DebtApp(AmortizationTable) in order to instantiate the class.

#Preparation
#Please download the Assignment 7 zip le. Within the zipped le you should nd a le, called dashboard and a package containing a le, called GUI.py.
#You will need to install tkinter and ttkbootstrap in order to use the GUI, make sure you install these packages and check that you get the GUI application working. 
#You should be able to install these libraries by using the following commands:
#pip3 install tk (Mac) pip install tk (Windows)
#pip3 install ttkbootstrap (Mac) pip install ttkbootstrap (Windows)
#All testing code must be inside an if __name__==“__main__”.
#Structure
#Assignment7: (folder)
#———dashboard.py
#———debt_repayment: (package)
#——————GUI.py
#——————tools: (package)
#—————————helper_functions.py
#—————————my_logger.py
#——————amortization_table: (package)
#—————————table.py

#Step 1: Helper Functions
#You will need to write 3 helper functions to help you calculate the monthly payments:
#The total amount that will be paid at the end of the repayment period and the total amount of interest paid over the course of the loan.
#In order to computer the monthly payments you will need to code the following formula:
#M = P * [ i * (1 + i) ** n ] / [ (1 + i) ** n - 1 ] 
#Where M is the monthly payment, P is the loan amount, i is the interest rate per month 
#(i.e. yearly interest rate divided by 12, note that an interest rate of 6.8% should be represented using 0.068) 
#And n is the number of monthly payments. 
#Make sure this formula is coded correctly (you can double check using the repayment calculator that’s online).
#If you’re clever/lazy you can use the monthly payment function to help you with the functions for the total amount to be paid and the total interest paid.
#All three functions must return their results. 
#Once the functions are completed (and work), remove the dummy functions inside of the GUI module and add a relative import statement at the top of the le for the three functions. 
#Make sure you’re importing the functions directly in the module, i.e. that you can call the function by their names directly. 
#Once this is done, run the GUI application, enter values for the loan balance, interest rates and remaining time elds and click the Calculate Payments button to verify that the functions work.

#Step 2: AmortizationTable class
#An amortization table is a spreadsheet that breaks down the repayment information to help you follow how you’re progressing in your repayment plan. 
#You will need to write a class that will create an amortization table using a pandas dataframe. 
#The class will be dened inside the debt_repayment folder in a subfolder called amortization_table, in the module table.py. 
#The class will be instantiated when you click the “Generate Amortization Table” button
#This class should implement the following methods:
#• __init__ – Constructor that takes loan_type (str), loan_balance (oat), interest_rate (oat), num_months (int) and monthly_payment (oat) as arguments. 
#The method should create an attribute for every argument passed in and an amortization_df attribute as an empty pandas DataFrame. 
#It should then make a call to the create_table method.
#• amortization_df: this is a pandas DataFrame.
#• loan_type: type of the loan (e.g. Student loan, Car, Home, etc…)
#• loan_balance: total amount borrowed (e.g. 200000)
#• interest_rate: annual percentage rate on the loan (e.g 6.8)
#• num_months: length of the loan in months (e.g. 120)
#• monthly_payment: amount due every month (e.g. 115.23)
#• create_table – Method takes no arguments and creates the amortization table using the amortization_df attribute with the following elds:
#• Pmt #: payment number, should start at 1
#• Due date: timestamp with the date the payment is due (could be the rst of every month. 
#Start date should be rst day of the next month.)
#• Payment amount: monthly payment
#• Principal paid: amount of the monthly payment that goes towards principal
#• Interest paid: amount of the monthly payment that goes towards paying the interest on the loan
#• Remaining balance: amount of principal remaining
#I recommend using a helper function to compute the principal paid, interest paid and remaining balance.
#Once the table is created, your code should call the save_table method described below
#• save_table - Method takes a pandas dataframe as an arguments. 
#The method should check if the folder “debt_repayment/les/tables/” exists, if it doesn’t you should create the necessary folders using the os module. 
#It should then save the amortization table passed in as a csv le with the name “loan_typeloan_balance-monthly_payment.csv”. 
#The loan_type, loan_amount and monthly_payment should be lled in dynamically.
#• more_principal - Method takes no arguments. 
#The method nds the number of months it will take you to start paying more towards principal than towards interest and returns it. 
#Use the amortization_df attribute for this. 
#The method will be called when you click the “Principal” button.
#• halfway - Method takes no arguments. 
#The method nds the number of months it will take to pay o half of your loan and returns it. 
#Use the amortization_df attribute for this. 
#The method will be called when you click the “Halfway” button.
#• update_payments - Method takes in a lump_sum (oat, default of 0.0) and extra_payment (oat, default of 0.0) as arguments. 
#The function should update the loan_balance attribute (if applicable) and the monthly_payment attribute (if applicable) respectively. 
#It should then make a call to the create_table method.
#The method will be called when you press the “Update Payment” button (lump sum or additional payment eld must have a value, otherwise you won’t see a change).

#Step 3: Logger
#This module will contain a custom logger that will be used inside the AmortizationTable class. 
#The method will check if the folder “debt_repayment/les/logs/” exists, if it doesn’t, it should create the necessary folders using the os module. 
#The custom logger will be dened inside the tools folder in a module called my_logger.py. 
#The logger will have a level of DEBUG. 
#It will write messages out to a le called ‘getting_out_of_debt.log’ which will be inside the “/debt_repayment/les/logs/” folder and will have the format:
#“timestamp - level - name - line_number: message”
#You will have a debug log message in the constructor of the AmortizedTable with the message: “Instantiating AmortizedTable Class”
#You will have a, info log message in the create_table method with the message:
#“Creating the amortized table”
#You will have an info log message in the update_payment method with the message:
#“Updating the loan repayment: monthly_payment, loan_balance”

#Upload
#Please ZIP the Assignment6 folder containing all folders and les described above including the data le. 
#Your code must be in the same hierarchy as shown at the beginning of the homework.
