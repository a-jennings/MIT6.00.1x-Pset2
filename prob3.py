balance = 320000
annualInterestRate = 0.2
#Result 29157.09



def lowpay(balance, annualInterestRate):
    
    high = balance
    low = 0

    #while balance > 0:
    while True:
        fixedPay = (high + low)/2
        epsilon = 0.01
        currBalance = balance
        balancex = balance
        for i in range(12):
            balancex = balancex - fixedPay
            balancex = balancex + ((balancex*annualInterestRate/12))

        if abs(balancex)<= epsilon:
            return round(fixedPay, 2)
        elif balancex > 0: #guess is too little
            low = fixedPay
            
            

        elif balancex < 0: #guess is too much
            high = fixedPay




#This currently works but its THE WORST CODE EVER 





print("Lowest payment: " + str(lowpay(balance, annualInterestRate)))
