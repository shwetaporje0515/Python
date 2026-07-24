"""4. Accept number from user and display below pattern. 
Input :  
Output : 4 
# 1 * # 2 * # 3 * # 4 * 
"""


iValue = int(input("Enter number : "))

def Pattern(iNo):
    for i in range(1,iNo+1):
        print("#",i,"*", end = " ")
        
Pattern(iValue)