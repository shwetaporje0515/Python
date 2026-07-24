"""
2. Accept number from user and display below pattern. 

Input = 5
output = 5 # 4 # 3 # 2 # 1 # 

"""

iValue = int(input("Enter number : "))

def Pattern(iNo):
    i = 1
    for i in range(iNo , i-1, -1):
        print(i, "#", end = " ")
    
            
Pattern(iValue)