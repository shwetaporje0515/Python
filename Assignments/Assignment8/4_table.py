"""4.Write a program which accept number from user and display its table.  
Input : 2 
Output :  2 4 6 8 10 12 14 16 18 20
"""

iValue = int(input("Enter the number : "))

def Table(iNo):
    if(iNo <= 0):
        iNo = -iNo
    
    itable = 1
    for i in range (1,11):
        itable = iNo * i
        print(itable , end = " ")
        
Table(iValue)