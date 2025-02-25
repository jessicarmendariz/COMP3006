import math
import debt_repayment.GUI

#Calculate The Regular Monthly Payment
def calculate_monthly_payment(principal, annual_rate, months):
    if principal <= 0 or months <= 0:
        return 0

    if annual_rate == 0:
        return round(principal / months, 2)
    monthly_rate = annual_rate / 100 / 12 
    
    try:
        payment = principal * (monthly_rate * (1 + monthly_rate) ** months) / ((1 + monthly_rate) ** months - 1)
        return round(payment, 2)
    except ZeroDivisionError:
        return 0 

#Calcualte The Payments Made Over the Length of the Loan
def calculate_total_payment(principal, annual_rate, months):
    monthly_payment = calculate_monthly_payment(principal, annual_rate, months)
    
    if monthly_payment is None:
        raise ValueError("Error: Monthly payment calculation returned None.")
    
    return round(monthly_payment * months, 2)

#Calcualte Interest Over the Loan Period
def calculate_total_interest(principal, annual_rate, months):
    return calculate_total_payment(principal, annual_rate, months) - principal
