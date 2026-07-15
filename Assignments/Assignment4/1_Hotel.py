iValue = int(input("Enter your income : "))


def IncomeTax(iAmount):
    if(iAmount < 500000):
        print("No Income tax!")
    elif(iAmount < 500000 and iAmount > 1000000):
        iAmount1 = (iAmount/100) * 10
        print("You have to pay the income tax of : ")
    elif(iAmount < 1000000 and iAmount > 2000000):
        iAmount2 = (iAmount/100) * 20
        print("You have to pay the income tax of : ",iAmount2)
    elif(iAmount > 2000000):
        iAmount3 = (iAmount/100) * 30
        print("You have to pay the income tax of : ",iAmount3)
        
IncomeTax(iValue)