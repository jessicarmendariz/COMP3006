from debt_repayment.amortization_table.table import AmortizationTable
import debt_repayment.GUI  # Ensure GUI has access to this module

#Define Data
debt_repayment.GUI.data = AmortizationTable("Loan", 10000, 5.0, 60, 200)  # Assign a default instance

#Start the GUI App
if __name__ == "__main__":
    app = debt_repayment.GUI.DebtAPP(AmortizationTable)
