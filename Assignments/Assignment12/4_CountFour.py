"""4.Write a program which accept number from user and count frequency of 4 in it. 
Input :  2395  
Output :  0 
Input : 1018 
Output :  0 
Input : 9440
Output :  2 
Input : 922432
Output :  1 

"""


iValue = int(input("Enter the number : "))

def CountFour(iNo):
    if(iNo <= 0):
        iNo = -iNo
    
    iCount = 0
    while(iNo != 0):
        iDigit = iNo % 10
        
        if(iDigit == 4):
            iCount =+ 1

        iNo = iNo / 10
    
    return iCount


iRet = CountFour(iValue)
print(iRet)
        