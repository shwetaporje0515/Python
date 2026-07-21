"""3.Write a program which accept number from user and return the count of digits in 
between 3 and 7. 
Input :  2395  
Output :  1 
Input : 1018 
Output :  0 
Input : 4521
output : 2
Input : 9922
Output : 0

"""


iValue = int(input("Enter the number : "))

def CountRange(iNo):
    if(iNo <= 0):
        iNo = -iNo
    
    iCount = 0
    for i in range(iNo):
        iDigit = iNo % 10
        if(iDigit > 3 and iDigit < 7):
            iCount += 1
        
        iNo = iNo // 10
    
    return iCount
    
def main():
    iRet = CountRange(iValue)
    print(iRet)

main()