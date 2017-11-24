balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

for i in range(12):
    balance = balance - (balance * monthlyPaymentRate)
    balance = balance + (balance * (annualInterestRate / 12.0))

print('Remaining balance:', round(balance, 2))
