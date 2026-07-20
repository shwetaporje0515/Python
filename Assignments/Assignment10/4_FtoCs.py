"""4. Write a program which accept temperature in Fahrenheit and convert it into 
celsius. (1 celsius = (Fahrenheit -32) * (5/9)) 
Input : 10
Output :  -12.2222 (10 - 32) * (5/9)

Input : 34
Output :  1.11111 (34 - 32) * (5/9)
"""

fValue = float(input("Enter the temperature in Fahrenheit : "))

def FhtoCs(iTemp):
    celcius = (iTemp - 32) * (5/9)
    return celcius
    
dRet = FhtoCs(fValue)
print("Converted temperature : ",dRet)