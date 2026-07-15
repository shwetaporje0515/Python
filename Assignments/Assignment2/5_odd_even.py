# 5. Accept number from user and check whether number is even or 
# odd.  

iValue = int(input("Enter the number : "))

def ChkEven(iNo):
    if(iNo % 2 == 0):
        print("Number is even")
    else:
        print("Number is odd")
        
ChkEven(iValue)