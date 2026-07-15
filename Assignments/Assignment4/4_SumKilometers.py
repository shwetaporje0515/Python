"""
4. We have to design application for tourist company.  
Tourist company provides cars on rent.  
Depends on the running of car they apply rent.  
If running is less than 100 kilometres then they charge 25 rupees per kilometre .  
And if running is more than 100 kilometres then they apply 15 rupees per kilometre after 
100 kilometres.  
We have to accept number of kilometres from user and return the estimated rent. 
Input : 73	Output : 1825    
Input : 132   	Output : 2980 
Input : 189   	Output : 3835 
"""


iValue = int(input("Enter the kilometers you travelled : "))

def TouristBill(iKilometers):
    if(iKilometers < 100):
        iKilometers = iKilometers * 25
        print(iKilometers)
    elif(iKilometers > 100):
        iSum1 = 100 * 25
        iKilometers = iKilometers - 100
        iSum2 = iKilometers * 15
        iCharge = iSum1 + iSum2
        print(iCharge)
        
    
TouristBill(iValue)
    