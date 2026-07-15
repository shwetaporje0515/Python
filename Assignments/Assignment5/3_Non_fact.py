""" 3.Write a program which accept number from user and display all its non factors. 

Input :  12 
Output : 5 7 8 9 10 11 """


iValue = int(input("Enter a number : "))

# iMult = 1
# i = 0;

def NonFact(iNo):
    # iMult = 1
    i = 1
    for i in range(1,iNo):
        if(iNo % i != 0):
            print(i)

NonFact(iValue)
