"""2.Write a program which accept number from user and print numbers till that  
number. 
Input :  
8  
Output :  1  2 3 4 5 6 7 8 
"""

iValue = int(input("Enter the number : "))

def Display(iNo):
    if(iNo <= 0):
        iNo = -iNo
    for i in range (1,iNo+1):
        print(i, end = " " )
    
Display(iValue)