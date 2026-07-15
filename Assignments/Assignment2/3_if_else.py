""" 3. Accept on number from user if number is less than 10 then print 
“Hello” otherwise print “Demo”. """

iValue = int(input("Enter the number : "))

def Display(iNo):
    if(iNo<10):
        print("Hello")
    else:
        print("Demo")
        
Display(iValue)