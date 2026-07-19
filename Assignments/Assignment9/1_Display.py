"""1.Write a program which accept number from user and display below pattern. 
Input : 5 
output : * * * * * # # # # # 
"""

iValue = int(input("Enter number : "))

def Display(iNo):
    if(iNo <= 0):
        iNo = -iNo
    for i in range(1,iNo+1):
        print("* ", end = " ")
    for i in range(1,iNo+1):
        print("# ", end = " ")
        
Display(iValue)