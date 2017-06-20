#prob1

balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

for i in range(12):
    unpaidBalance = balance - (balance*monthlyPaymentRate)
    balance = unpaidBalance + (unpaidBalance * (annualInterestRate/12))
print('Remaining balance: ' + str(round(balance, 2)))
