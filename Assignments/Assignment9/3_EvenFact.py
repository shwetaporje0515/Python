"""3.Write a program to find even factorial of given number.  
Input :  5  
Output :  8   (4 * 2)
Input :  -5  
Output :  8   (4 * 2)
Input :  10  
Output :  3840  (10 * 8 * 6 * 4 * 2)
"""i

Value = int(input("Enter number : "))

def EvenFactorial(iNo):
    if(iNo <= 0):
        iNo = -iNo
    
    iFact = 1
    for i in range(1, iNo+1):
        if(i % 2 == 0):
            iFact = iFact * i
    return iFact
    

def main():
    iRet = EvenFactorial(iValue)
    print("Even factorial of number is : ",iRet)
    
main()