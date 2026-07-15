iValue = int(input("Enter the number : "))

def DisplayFactor(iNo):
    if(iNo <= 0):
        iNo = -iNo
        
    i = 1
    for i in range(1,iNo):
        if((iNo % i == 0) and (i % 2 == 0)):
            print(i)
            
DisplayFactor(iValue)