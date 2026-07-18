"""4. Write a program which accepts N from user and print all odd numbers up to N.

input : 8
output : 1 3 5 7 9 11 13 15 17

"""

iValue = int(input("Enter the number : "))

def OddDisplay(iNo):
    for i in range (1,iNo):
        if(i % 2 != 0):
            print(i, end = " " )
    
OddDisplay(iValue)