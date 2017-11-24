balance = 3926
annualInterestRate = 0.2
newBalance = balance

if balance / 12 < 10:
    payment = 10
else:
    payment = round(balance / 12, -1)

while True:
    for i in range(12):
        newBalance = newBalance - payment
        newBalance = newBalance + (newBalance * (annualInterestRate / 12.0))
    if newBalance < 0:
        break
    payment += 10
    newBalance = balance
print('Lowest Payment:', payment)
