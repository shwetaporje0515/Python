"""5. Accept number from user and display below pattern. 
Input : 8 
Output : 2 4 6 8 10 12 14 16
"""

iValue = int(input("Enter number : "))

def Pattern(iNo):
    for i in range(1,(iNo+1)*2):
        if(i % 2 == 0):
            print(i)
            
Pattern(iValue)