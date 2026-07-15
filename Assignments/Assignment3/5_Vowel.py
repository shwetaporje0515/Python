cValue = input("Enter the character : ")

def DisplayConvert(cValue):
    if(cValue == ('a' or 'A') or ('e' or 'E') or ('i' or 'I') or ('o' or 'O') or ('u' or 'U')):
        return True
    else:
        return False
        
bRet = False        
bRet = DisplayConvert(cValue)

if(bRet == True):
    print("Vowel")
else:
    print("not vowel")

