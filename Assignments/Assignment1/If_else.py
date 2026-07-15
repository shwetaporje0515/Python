// 4. Accept one number and check whether is is divisible by 5 or not.  

True = 1
False = 0

iValue = int(input("Enter the no:"))
print(iValue)

if(bRet == True):
    print("Divisible by 5")
else:
    print("Not divisible by 5")

def Check(iNo):
	if((iNo % 5)==0):
		return True
	else:
		return False

Check(5)
