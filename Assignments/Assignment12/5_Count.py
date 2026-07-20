"""5.Write a program which accept number from user and count frequency of such a 
digits which are less than 6. 
Input :  2395  
Output :  3 
Input : 1018 
Output :  3 
Input : 9440
Output :  3 
Input : 96672 
Output :  1
"""

iValue = int(input("Enter the number : "))

def Count(iNo):
    if(iNo <= 0):
        iNo = -iNo
    
    iCount = 0
    while(iNo != 0):
        iDigit = iNo % 10
        
        if(iDigit < 6):
            iCount =+ 1

        iNo = iNo / 10
    
    return iCount


iRet = Count(iValue)
print(iRet)
        