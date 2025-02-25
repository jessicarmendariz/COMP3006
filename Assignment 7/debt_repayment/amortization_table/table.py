import pandas as pd
import os

#Creates an Amortization Table with 6 Methods
class AmortizationTable:
    #Creates Amortization Table with Pandas Data Frame
    def __init__(self, loan_type, loan_balance, interest_rate, num_months, monthly_payment):
        self.loan_type = loan_type
        self.loan_balance = loan_balance
        self.interest_rate = interest_rate
        self.num_months = num_months
        self.monthly_payment = monthly_payment

        #Empty Data Frame
        self.amortization_df = pd.DataFrame(columns=["Pmt #", "Due date", "Payment amount", 
                                                     "Principal paid", "Interest paid", "Remaining balance"])

        #Generates Table
        self.create_table()
    
    #Creates the Amortization Table
    def create_table(self):
        payment_number = 1
        balance = self.loan_balance
        monthly_interest_rate = (self.interest_rate / 100) / 12
        payment_date = pd.Timestamp.today().normalize() + pd.DateOffset(months=1)
        table_data = []

        while balance > 0 and payment_number <= self.num_months:
            interest_paid = round(balance * monthly_interest_rate, 2)
            principal_paid = round(self.monthly_payment - interest_paid, 2)

            if balance - principal_paid < 0:
                principal_paid = balance
                self.monthly_payment = interest_paid + principal_paid
            balance = round(balance - principal_paid, 2)
            table_data.append([payment_number, payment_date, self.monthly_payment, 
                               principal_paid, interest_paid, balance])
            payment_number += 1
            payment_date += pd.DateOffset(months=1)

        #Convert Information to DataFrame
        self.amortization_df = pd.DataFrame(table_data, columns=["Pmt #", "Due date", "Payment amount", 
                                                                 "Principal paid", "Interest paid", "Remaining balance"])

        self.save_table()

    #Saves Table as CSV File
    def save_table(self):
        directory = "debt_repayment/files/tables/"
        if not os.path.exists(directory):
            os.makedirs(directory)
        filename = f"{self.loan_type}_{self.loan_balance}-{self.monthly_payment}.csv"
        self.amortization_df.to_csv(os.path.join(directory, filename), index=False)

    #Finds the Month When Principal Payments Are More Than Interest Payments
    def more_principal(self):
        return (self.amortization_df["Principal Paid"] > self.amortization_df["Interest Paid"]).idxmax() + 1

    #Find When the Loan is Halfway to Repayment
    def halfway(self):
        halfway_balance = self.loan_balance / 2
        return (self.amortization_df["Remaining Balance"] <= halfway_balance).idxmax() + 1

    #Apply Lump Sum or Extra Monthly Payments
    def update_payments(self, lump_sum=0.0, extra_payment=0.0):
        self.loan_balance -= lump_sum
        self.monthly_payment += extra_payment
        self.create_table()
