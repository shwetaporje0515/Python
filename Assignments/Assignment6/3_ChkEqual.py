"""3. Write a program which accept two numbers and check whether numbers are 
equal or not.  


Input : 10 10  
Output : Equal  
Input : 10 12  
Output : Not Equal 
Input : 10 -10  
Output : Not Equal
"""

iValue1 = int(input("Enter the number 1: "))
iValue2 = int(input("Enter the number 2: "))

# bRet = False

if(bRet == True):
    print("Equal")
else:
    print("Not Equal")

def ChkEqual(iNo1, iNo2):
    if(iNo1 == iNo2):
        return True
    else:
        return False
        

ChkEqual(iValue1,iValue2)


