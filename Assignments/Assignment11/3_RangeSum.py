"""3. Write a program which accept range from user and return addition of all numbers 
in between that range. (Range should contains positive numbers only) 
Input :  23 30  
Output :  212   

Input :  10 18
output : 126

input : -10 2
output : invalid range

input : 90 18
output : invalid range"""

iValue1 = int(input("Enter the starting point : "))
iValue2 = int(input("Enter the ending point : "))

def RangeSum(iStart , iEnd):
    if(iStart > iEnd):
        print("Invalid range")
        
    if(iStart < 0):
        print("Invalid range")
        
    iSum = 0
    for i in range(iStart, iEnd+1):
        iSum = iSum + i
    
    return iSum
    
def main():
    iRet = RangeSum(iValue1, iValue2)
    print("Addition is : ", iRet)

main()