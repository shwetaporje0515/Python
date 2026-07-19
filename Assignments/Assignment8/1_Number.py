"""1. Write a program which accept number from user and if number is less than 50 
then print small , if it is greater than 50 and less than 100 then print medium, if it is 
greater than 100 then print large.

Input : 75  
Output : Medium """

iValue = int(input("Enter the number : "))

def Number(iNo):
    if(iNo < 50):
        print("Small number")
    elif(iNo > 50 and iNo < 100):
        print("Medium number")
    elif(iNo > 100):
        printf("Large number")
        
Number(iValue)