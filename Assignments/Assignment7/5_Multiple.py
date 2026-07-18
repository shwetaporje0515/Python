"""5. Write a program which accept N and print first 5 multiples of N.  
Input :  4  
Output :  4  8  12  16  20

"""

iValue = int(input("Enter the number : "))

def MultipleDisplay(iNo):
    for i in range (1,6):
        iMul = iNo * i
        print(iMul , end =  " ")
    
MultipleDisplay(iValue)