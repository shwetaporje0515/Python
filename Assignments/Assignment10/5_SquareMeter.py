"""5. Write a program which accept area in square feet and convert it into square 
meter. (1 square feet = 0.0929 Square meter) 
Input : 5 
Output :  0.464515

Input : 7 
Output :  0.650321
"""

iValue = int(input("Enter area in square feet : "))

def SquareMeter(iNo):
    Square_Meter = 0.0929
    Ans = Square_Meter * iNo
    return Ans

dRet = SquareMeter(iValue)
print("converted area to square meter is  : ", dRet)