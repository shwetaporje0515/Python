"""5. Write a program which accept number from user and display its table in reverse 
order.  
Input :  2 
Output :  20 18 16 14 12 10 8 6 4 2

Input : 5 
Output :  50 45 40 35 30 25 20 15 10 5 
Input : wh -5 
Output :  50 45 40 35 30 25 20 15 10 5
"""

iValue = int(input("Enter the number : "))

def TableRev(iNo):
    if(iNo <= 0):
        iNo = -iNo
    
    itable = 1
    for i in range (10,1):
        itable = iNo * i
        print(itable , end = " ")
        i =- 1
        
TableRev(iValue)