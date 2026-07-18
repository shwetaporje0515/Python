"""1.Write a program which accept number from user and print that number of $ & * 
on screen. 

Input : 5 
Output :  $ * $ * $ * $ * $ * 
"""

iValue = int(input("Enter the number : "))

def Pattern(iNo):
    if(iNo <= 0):
        iNo = -iNo
    for i in range (iNo):
        print("$ * ", end = " ")
    
Pattern(iValue)