"""1.Write a program which accept number from user and return the count of even 
digits. 
Input :  2395  
Output :  1 
Input :  1018 
Output :  2 
Input :  -1018 
Output :  2 
Input : 8462
Output :  4
"""

iValue = int(input("Enter the number : "))

def CountEven(iNo):
    if(iNo <= 0):
        iNo = -iNo
    
    iCount = 0
    for i in range(iNo):
        iDigit = iNo % 10
        if(iDigit % 2 == 0):
            iCount += 1
        
        iNo = iNo // 10
    
    return iCount
    
def main():
    iRet = CountEven(iValue)
    print(iRet)

main()