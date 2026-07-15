""" 4.Write a program which accept number from user and return summation of all its 
non factors. 
Input :  12 
Output : 50 """ 

iValue = int(input("Enter a number : "))
# iMult = 1
# i = 0;

def SumNonFact(iNo):
    # iMult = 1
    i = 1
    iSum = 0
    for i in range(1,iNo):
        if(iNo % i != 0):
            print(i)
            iSum = iSum + i
    return iSum

iRet = SumNonFact(iValue)
print("Summation of Non factor is : ",iRet)