balance = 320000
annualInterestRate = 0.2
#Result 29157.09



def lowpay(balance, annualInterestRate):
    currBalance = balance
    fixedPay = 0
    
    while balance > 0:
        currBalance = balance
        for i in range(12):
            balance = balance - fixedPay
            balance = balance + ((balance*annualInterestRate/12))
        if balance > 0:
            fixedPay += 0.01
            balance = currBalance
        else:
            return round(fixedPay, 2)


#This currently works but has no bisect search which is required





print("Lowest payment: " + str(lowpay(balance, annualInterestRate)))
