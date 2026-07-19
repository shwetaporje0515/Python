"""4. Write a program to find odd factorial of given number.  
Input :  5  
Output :  15   (5 * 3 * 1)
Input :  -5  
Output :  15   (5 * 3 * 1)
Input :	  10  
Output :  945  (9 * 7 * 5 * 3 * 1)

"""

iValue = int(input("Enter number : "))

def OddFactorial(iNo):
    if(iNo <= 0):
        iNo = -iNo
    
    iFact = 1
    for i in range(1, iNo+1):
        if(i % 2 != 0):
            iFact = iFact * i
    return iFact
    

def main():
    iRet = OddFactorial(iValue)
    print("Odd factorial of number is : ",iRet)
    
main()