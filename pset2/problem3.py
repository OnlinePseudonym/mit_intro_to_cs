balance = 999999
annualInterestRate = 0.18
monthlyInterestRate = annualInterestRate / 12.0
newBalance = balance
lowerBound = balance / 12.0
higherBound = (balance * (1 + monthlyInterestRate)**12) / 12.0

while True:
    payment = (lowerBound + higherBound) / 2.0
    for i in range(12):
        newBalance = newBalance - payment
        newBalance = newBalance + (newBalance * monthlyInterestRate)
    if abs(newBalance) < 0.01:
        break
    elif newBalance < 0:
        higherBound = payment
    else:
        lowerBound = payment
    newBalance = balance
print('Lowest Payment:', round(payment, 2))
