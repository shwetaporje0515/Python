iValue = int(input("enter the value :"))

def DisplayEven(iNo):
    if(iNo <= 0):
        return
    
    for i in range(1,(iNo*2)+1):
        if (i % 2 == 0):
            print(i)
            
            
DisplayEven(iValue)