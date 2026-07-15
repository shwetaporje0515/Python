"""4. Accept two numbers from user and display first number in second 
number of times. """

iValue = int(input("Enter the value : "))
iCount = int(input("Enter the frequency : "))

def Display(iNo, iFrequency):
    
    for i in range(iFrequency):
        print(iNo)
        
Display(iValue,iCount)