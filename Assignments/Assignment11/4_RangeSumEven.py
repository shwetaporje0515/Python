"""4.Write a program which accept range from user and return addition of all even 
numbers in between that range. (Range should contains positive numbers only) 
Input :  23 30  
Output :  108   

Input : 10 18 
Output :  70 
Input : -10 2 
Output :  Invalid range 
Input : 90 18 
Output :  Invalid range 
"""


iValue1 = int(input("Enter the starting point : "))
iValue2 = int(input("Enter the ending point : "))

def RangeSumEven(iStart , iEnd):
    if(iStart > iEnd):
        print("Invalid range")
        
    if(iStart < 0):
        print("Invalid range")
        
    iSum = 0
    for i in range(iStart, iEnd+1):
        if(i % 2 == 0):
            iSum = iSum + i
    
    return iSum
    
def main():
    iRet = RangeSumEven(iValue1, iValue2)
    print("Addition is : ", iRet)

main()