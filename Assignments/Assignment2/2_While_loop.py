#2. Accept one number from user and print that number of * on screen. 

iValue = int(input("Enter the number : "))
iCnt = 0

def Display(iNo):
    while(iNo > iCnt):
        print("*")
        iNo-=1
        
Display(iValue)