""" 5.Write a program which accept number from user and return difference between 
summation of all its factors and non factors.

Input :  12 
Output : -34 (16 - 50)  
Input :   10  
Output : -29 (8 - 37) """

iValue = int(input("Enter a number : "))
# iMult = 1
# i = 0;

def FactDiff(iNo):
    # iMult = 1
    i = 1
    iSumFact = 0
    iSumNonFact = 0
    iDiff = 0
    for i in range(1,iNo):
        if(iNo % i == 0):
            # print(i)
            iSumFact = iSumFact + i
        elif(iNo % i != 0):
            iSumNonFact = iSumNonFact + i
    
    iDiff = iSumFact - iSumNonFact
    return iDiff

iRet = FactDiff(iValue)
print("Summation of Non factor is : ",iRet)