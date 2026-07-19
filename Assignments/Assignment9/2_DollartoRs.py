"""2. Accept amount in US dollar and return its corresponding value in Indian currency. 
Consider 1$ as 70 rupees.  
Input : 10
Output :  700 
Input :  3 
Output :  270
"""

iValue = int(input("Enter number : "))

def DollarToINR(iNo):
    iRs = iNo * 70
    return iRs
    
iRet = DollarToINR(iValue)
print("Value in INR is : ",iRet)