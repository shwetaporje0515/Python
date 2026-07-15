# 1.Program to divide two numbers 

def Divide(iValue1, iValue2):
    if(iValue2 == 0):
        return -1
    
    iAns = iValue1 / iValue2
    print(iAns)
    
Divide(15,5)