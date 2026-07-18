"""3. Write a program which accept number from user and print its numbers line. 
Input :  
4  
Output :  -4  -3  -2  -1  0  1  2  3  4
"""

iValue = int(input("Enter the number : "))

def Display(iNo):
    if(iNo <= 0):
        iNo = -iNo
    for i in range (-iNo,iNo+1):
        print(i, end = " " )
    
Display(iValue)