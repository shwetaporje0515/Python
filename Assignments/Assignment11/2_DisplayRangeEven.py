"""2. Write a program which accept range from user and display all even numbers in 
between that range. 
Input :  23 35  
Output :  24 26 28 30 32 34   

Input : 10 18 
Output :  10 12 14 16 18 
Input : 10 10 
Output :  10  
Input : -10 2 
Output :  -10 -8 -6 -4 -2 0 2 
Input : 90 18 
Output :  Invalid range
"""

iValue1 = int(input("Enter the starting value : "))
iValue2 = int(input("Enter the ending value : "))

def RangeDisplay(iStart,iEnd):
    if(iStart <= 0):
        iStart = -iStart
        
    for i in range(iStart ,iEnd+1):
        if(i % 2 == 0):
            print(i)
        
    if(iStart > iEnd):
        print("Invalid range")
        
def main():
    RangeDisplay(iValue1, iValue2)
    
main()