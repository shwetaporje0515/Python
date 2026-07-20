"""3.Write a program which accept number from user and count frequency of 2 in it. 
Input :  2395  
Output :  1 
Input : 1018 
Output :  0 
Input : 9000
Output :  0 
Input : 922432
Output :  3
"""



iValue = int(input("Enter the number : "))

def CountTwo(iNo):
    if(iNo <= 0):
        iNo = -iNo
    
    iCount = 0
    while(iNo != 0):
        iDigit = iNo % 10
        
        if(iDigit == 2):
            iCount =+ 1

        iNo = iNo / 10
    
    return iCount


iRet = CountTwo(iValue)
print(iRet)
        