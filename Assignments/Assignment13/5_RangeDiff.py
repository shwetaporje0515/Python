"""
5.Write a program which accept number from user and return difference between 
summation of even digits and summation of odd digits. 
Input :  2395  
Output :  -15 (2 - 17) 
Input :  1018 
Output :  6 (8 - 2) 
Input :  8440 
Output :  16  (16 - 0) 
Input :  5733 
Output :  -18 (0 - 18)
"""

iValue = int(input("Enter the number : "))

def CountDiff(iNo):
    if(iNo <= 0):
        iNo = -iNo
    
    iSum1 = 0
    iSum2 = 0
    for i in range(iNo):
        iDigit = iNo % 10
        
        if(iDigit % 2 == 0):
            iSum1 = iSum1 + iDigit
        elif(iDigit % 2 != 0):
            iSum2 = iSum2 + iDigit
        
        iNo = iNo // 10
        
        iDiff = iSum1 - iSum2
    
    return iDiff
    
def main():
    iRet = CountDiff(iValue)
    print(iRet)

main()
