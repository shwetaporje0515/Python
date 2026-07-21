"""1.Write a program which accept range from user and display all numbers in between 
that range. 
Input :  23 35  
Output :  23 24 25 26 27 28 29 30 31 32 33 34 35  

Input : 10 18 
Output :  10 11 12 13 14 15 16 17 18 
Input : 10 10 
Output :  10  
Input : -10 2 
Output :  -10 -9 -8 -7 -6 -5 -4 -3 -2 -1 0 1 2
"""

iValue1 = int(input("Enter the starting value : "))
iValue2 = int(input("Enter the ending value : "))

def RangeDisplay(iStart,iEnd):
    if(iStart <= 0):
        iStart = -iStart
        
    for i in range(iStart ,iEnd+1):
        print(i)
        
    if(iStart > iEnd):
        print("Invalid range")
        
def main():
    RangeDisplay(iValue1, iValue2)
    
main()