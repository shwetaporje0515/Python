"""2.Write a program which accept number from user and check whether it contains 0 
in it or not. 
Input :  
2395  
Output :  There is no Zero 
Input : 
 10
18 
Output :  It Contains Zero 
Input : 
 90
00 
Output :  It Contains Zero 
Input : 
 10
687 
Output :  It Contains Zero
"""

iValue = int(input("Enter the number : "))

def ChkZero(iNo):
    if(iNo <= 0):
        iNo = -iNo
    
    while(iNo != 0):
        iDigit = iNo % 10
        
        if(iDigit == 0):
            return True
        else:
            return False
            
        iNo = iNo / 10
    
def main():
    bRet = False
    bRet = ChkZero(iValue)

    
    if(bRet == True):
        print("It contains zero")
    else:
        print("It does not contains zero")
        
main()