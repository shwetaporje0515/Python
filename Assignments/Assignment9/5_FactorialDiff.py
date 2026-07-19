"""5. Write a program which returns difference between Even factorial and odd factorial 
of given number.  
Input :  5  
Output :  -7   (8 - 15)
Input :  -5  
Output :  -7   (8 - 15
Input :  10  
Output :  2895  (3840 - 945)

"""

iValue = int(input("Enter number : "))

def FactorialDiff(iNo):
    if(iNo <= 0):
        iNo = -iNo
    
    iFact1 = 1
    iFact2 = 1
    for i in range(1, iNo+1):
        if(i % 2 == 0):
            iFact1 = iFact1 * i
        elif(i % 2 != 0):
            iFact2 = iFact2 * i
    return iFact1 - iFact2
    

def main():
    iRet = FactorialDiff(iValue)
    print("Factorial difference is : ",iRet)
    
main()