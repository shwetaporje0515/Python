"""1.Write a program which accept radius of circle from user and calculate its area. 
Consider value of PI as 3.14. (Area = PI * Radius * Radius) 
Input :  5.3  
Output :  88.2026  

Input :  
10.4  
Output :  339.6224 
"""

fValue = float(input("Enter radius : "))

def CircleArea(fRadius):
    PI = 3.14
    Area = 0
    
    Area = PI * fRadius * fRadius
    
    return Area

dRet = CircleArea(fValue)
print(f"Area of circle is : {dRet: .4f}")