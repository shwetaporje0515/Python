"""3. Write a program which accept distance in kilometre and convert it into meter. (1 
kilometre = 1000 Meter)

input : 5
output : 5000

"""


iValue = int(input("Enter distance : "))

def KMtoMeter(iNo):
    KM = 1000
    KMtoM = iNo * KM
    return KMtoM

iRet = KMtoMeter(iValue)
print("kilometer to meter is : ",iRet)