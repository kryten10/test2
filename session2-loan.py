LoanAmount = float(input("Loan amount?"))
MonthlyInterestRate = float(input("Monthly Interest Rate (e.g. 1.0)?")) / 100
NumberOfYears = float(input("number of years to pay off loan?"))
MonthlyPayment = (LoanAmount * MonthlyInterestRate) / (1 - (1 / ((1 + MonthlyInterestRate) ** (NumberOfYears *12))))
TotalPayment = MonthlyPayment * NumberOfYears * 12
print(MonthlyPayment)
print(TotalPayment)