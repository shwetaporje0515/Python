"""2. Write a program which accept width & height of rectangle from user and calculate 
its area. (Area = Width * Height) 
Input :  5.3  9.78 
Output :  51.834
"""

fValue1 = float(input("Enter width : "))
fValue2 = float(input("Enter height : "))

def RectArea(fWidth, fHeight):
    Area = fWidth * fHeight
    return Area

dRet = RectArea(fValue1, fValue2)
print(f"Area of circle is : {dRet: .3f}")