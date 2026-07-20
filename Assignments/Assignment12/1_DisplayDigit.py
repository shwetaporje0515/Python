"""1.Write a program which accept number from user and display its digits in reverse 
order. 
Input :  2395  
Output :  5 
  9
  3
  2
Input :  1018 
Output :  8 
  1
  0
  1
Input : -1018 
Output :  8 
  1
  0
  1
Input : 9000 
Output :  0 
  0
  0
  9

"""

iValue = int(input("Enter the number : "))

def DisplayDigit(iNo):
    if(iNo <= 0):
        iNo = -iNo
    
    iDigit = 0
    while(iNo != 0):
        iDigit = iNo % 10
        print(iDigit,"\n")
        
        iNo = iNo / 10
    
def main():
    DisplayDigit(iValue)
    
main()