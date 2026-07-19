"""3.Write a program to find factorial of given number.  
Input :  5  
Output :  120   (5*4*3*2*1)
Input :  -5  
Output :  120   (5*4*3*2*1)
"""

iValue = int(input("Enter the number : "))

def Factorial(iNo):
    iMul = 1
    if(iNo <= 0):
        iNo = -iNo
    for i in range (1,iNo+1):
        iMul = iMul * i
    return iMul
    
iRet = Factorial(iValue)
print("Factorial of number is : ",iRet)