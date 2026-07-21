"""4.Write a program which accept number from user and return multiplication of all 
digits. 

Input : 2395
Output : 270
Input : 1018 
Output :  8 
Input :  9440 
Output :  144 
Input : 922432 
Output :  864
"""


iValue = int(input("Enter the number : "))

def MultRange(iNo):
    if(iNo <= 0):
        iNo = -iNo
    
    iMul = 1
    for i in range(iNo):
        iDigit = iNo % 10
        iMul = iMul * iDigit
        
        iNo = iNo // 10
    
    return iMul
    
def main():
    iRet = MultRange(iValue)
    print(iRet)

main()