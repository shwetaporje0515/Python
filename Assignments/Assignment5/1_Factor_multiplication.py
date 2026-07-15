"""1.Write a program which accept number from user and display its multiplication of 
factors. 
Input :  12
Output : 144	(1 * 2 * 3 * 4 * 6)
Input : 13 
Output : 1 	(1)
Input :  10   
Output : 10  	(1 * 2 * 5) """
 

iValue = int(input("Enter a number : "))
# iMult = 1
# i = 0;

def MultFact(iNo):
    iMult = 1
    i = 1
    for i in range(1,iNo):
        if(iNo % i == 0):
            print(i)
            iMult = iMult * i
    return iMult
    
Ans = MultFact(iValue)
print("Multiplication of factors is : ",Ans) 