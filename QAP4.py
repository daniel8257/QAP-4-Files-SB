
# Comment like a pro.
# programming  for insurance company to calculate the insurance premium 
# Start Date:2023-11-28; End Date:2023-12-17;
# Author: Shiva(Danny) Biera



# Import required libraries.
import datetime
from datetime import datetime
import FormatValues as FV






# Define program constants.

POLICY_NUM = 1994
BAS_PREM = 869.00
DISC_ADD_CARS = 0.25
EXLBTY_CRG = 130.00
GLS_CRG = 86.00
LNR_CAR = 58.00
HST = 0.15
PROS_FEE = 39.99



# Start the main program.




while True:
    # Define use inputs.
    
    
    FstName = input("Enter customer First Name: ").title()
    LstName = input("Enter customer Last Name: ").title()
    StrName = input("Enter the Street Address: ").title()
    City = input("Enter the City name: ").title()
    #Prov = input("Enter the Province name: ")
    ProvLst = ["NL", "NS", "PE", "NB", "QC", "ON", "MB", "SK", "AB", "BC", "YT", "NT", "NV"]
    while True:
        Prov = input("Enter the province (XX): ").upper()
        if Prov == "":
            print("Error - Province cannot be blank - Please reenter.")
        elif len(Prov) != 2:
            print("Error - Province is a 2 digit code - please reenter.")
        elif Prov not in ProvLst:
            print("Error - Not a valid province - please reenter.")
        else:
            break

    PostCd = input("Enter the Postal code: ").upper()
    PhNo   = input("Enter customer Phone number(999-999-9999): ")
    NumCars = int(input("Enter the number of cars to be insured: "))
    Liabty = input("Do you want extra extra liability of up to $1,000,000 for your car (enter Y / N):  ").upper()
    GlscCr = input("Do you want to add a glass coverage option to your policy (Y/N): ").upper()
    LnrcCr = input("Do you want to add a Lonaer vehicle option to your policy (Y/N):").upper()
    
    PmtOptLst = ["Full", "Monthly" ]
    while True:
        PmtOpt = input("How would you like to pay ?(Full or Monthly ): ").title()
        if PmtOpt == "":
            print("Error - Status cannot be blank - please reenter.")
        elif PmtOpt not in PmtOptLst:
            print("Error - invalid entry - must be Full, Monthly - please reenter.")  
        else:
            break
    if PmtOpt == "Full":
        DownPay =float(input ("Please enter how much you would like to  put as down payment: "))
    elif PmtOpt == "Monthly":
        DownPay =float(input ("Please enter how much you would like to  put as down payment: "))
    else:
        DownPay = 0  
        
    PvsClmDtLst = []
    while True:
        
        PvsClmDt = input ("Please enter the dates of any (all) previous claims in the past in YYYY-MM-DD (press ENTER to finish) :").upper()
        
        if PvsClmDt == "ENTER":
            break
        PvsClmDtLst.append(PvsClmDt)
        PvsClmDtDsp = datetime.strptime(PvsClmDt, "%Y-%m-%d")   
        
              
    PvsClmAmtLst = []    
    while True:
        
        PvsClmAmt = input("Please enter the amount of any (all) previous claims in the past (press ENTER to finish) :").upper()

        if PvsClmAmt == "ENTER":
            break

        PvsClmAmt = float(PvsClmAmt)
        PvsClmAmtLst.append(PvsClmAmt)
        
    # Calculate required results.
    
    BasRate = BAS_PREM
    NewDisc = 0
    FnRate = 0
    if NumCars >1 :
        
        BasRate = BAS_PREM * NumCars
        NewDisc = BAS_PREM * DISC_ADD_CARS * (NumCars - 1)
        FnRate =  BasRate - NewDisc 





    if Liabty == "Y":
        
        LiabtyAmt = EXLBTY_CRG * NumCars
        
    else:
        LiabtyAmt = 0
        
    if GlscCr == "Y":
        
        GlscCrAmt = GLS_CRG * NumCars

    else:
        GlscCrAmt = 0

    if LnrcCr == "Y":
        
        LnrcCrAmt = LNR_CAR * NumCars
        
    else:
        LnrcCrAmt = 0
        
        
    TotExCost = LiabtyAmt + GlscCrAmt + LnrcCrAmt

    InsPrem = FnRate + TotExCost
    HstAmt = InsPrem * HST
    TotCst = InsPrem + HstAmt

    if PmtOpt == "Full":
        
        TotCst = InsPrem + HstAmt  + PROS_FEE- DownPay
        
    elif PmtOpt == "Monthly":
        
        TotCst = (InsPrem + HstAmt  + PROS_FEE- DownPay) / 8
        
        
            
    # Print results.
    
    
    print(f"")

    print(f"                One Stop Insurance Company")
    print()
    print()
    print(f"---------------------------------------------------------")
    print()
    print()
    Name = FstName + " " + LstName

    print (f"Customer Name   : {Name:<20s}")
    print (f"Customer Address: {StrName}")
    Add = City + "," + Prov
    print (f"                  {Add:<20s}")  
    print (f"                  {PostCd:<20s}")
    print (f"Customer Phone  : {PhNo:12s}")
    print()
    print()
    print(f"No. of cars insured      :                              {NumCars:<1}")
    print(f"Extra liability coverage :                              {Liabty:<1s}")
    print(f"Glass coverage           :                              {GlscCr:<1s}")
    print(f"Loaner car coverage      :                              {LnrcCr:<1s}")
    print(f"Payment Method           :                        {PmtOpt:<8s}")
    print(f"How much you would like pay as down payment:   {FV.FDollar2(DownPay):>10s}")
    print()
    print(f"---------------------------------------------------------")
    print()
    print()
    print(f"Billing Information")
    print()
    print()
    print(f"Basic Rate               :                     {FV.FDollar2(BasRate):>10s}")
    print(f"Total Rate after discount:                     {FV.FDollar2(FnRate):>10s}")
    print(f"Extra Cost               :                     {FV.FDollar2(TotExCost):>10s}")
    print(f"Insurance Premium        :                     {FV.FDollar2(InsPrem):>10s}")
    print(f"HST                      :                     {FV.FDollar2(HstAmt):>10s}")
    print(f"Processing Fee           :                     {FV.FDollar2(PROS_FEE):>10s}")
    print(f"Total Cost               :                     {FV.FDollar2(TotCst):>10s}")
    print()
    print(f"---------------------------------------------------------")
    print()
    print()
    print(f"Previous Claims information:")
    print()
    print()
    
    print(f"                        Claim #  Claim Date        Amount") 
    print(f"                        ---------------------------------")
    for i, (amount, date) in enumerate(zip(PvsClmAmtLst, PvsClmDtLst), start=1):
        date = datetime.strptime(date, "%Y-%m-%d")
        AmtDsp  = FV.FDollar2(amount)
        DateDsp  = FV.FDateS(date)
        print(f"                        {i:<3d}      {DateDsp:>10s}    {AmtDsp:>10s}")

                                                      
    print()
    print()
    
    

    # loop to continue or exit
    Cont =input("would you like to process another insurance ????? (Y / N): ").upper()
    if Cont == "N":
        break



