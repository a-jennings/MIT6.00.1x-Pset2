balance = 3926
annualInterestRate = 0.2
fixedPay = 360
#Result 360

def lowpay(balance, annualInterestRate, fixedPay):
    
    while balance > 0:
        currBalance = balance
        for i in range(12):
            balance = balance - fixedPay
            balance = balance + ((balance*annualInterestRate/12))
        if balance > 0:
            return lowpay(currBalance, annualInterestRate, fixedPay+10)
        else:
            return fixedPay


print("Lowest payment: " + str(lowpay(balance, annualInterestRate, fixedPay)))

