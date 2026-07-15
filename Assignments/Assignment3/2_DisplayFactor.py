iValue = int(input("Enter the number : "))

def DisplayFactor(iNo):
    if(iNo <= 0):
        iNo = -iNo
        
    i = 1
    for i in range(1,iNo+1):
        if(iNo % i == 0):
            a = i
            i =+ 1
            if(a % 2 == 0):
                print(a)
            
DisplayFactor(iValue)