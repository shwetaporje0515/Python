#1.Accept one number from user and print that number of * on screen.  

iValue = int(input("Enter the number : "))

def Display(iNo):
    iCnt = 0
    while(iCnt < iNo):
        print("*")
        iCnt+=1
        
Display(iValue)