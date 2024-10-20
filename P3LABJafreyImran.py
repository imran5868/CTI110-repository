# JafreyiImran
# Program to calculate the most efficient way to represent a float money amount in dollars, quarters, dimes, nickels, and pennies.
amount = float(input("Enter the amount of money as a float: $"))
cents = int(round(amount * 100))
dollars = cents // 100
cents = cents % 100
quarters = cents // 25
cents = cents % 25
dimes = cents // 10
cents = cents % 10
nickels = cents // 5
cents = cents % 5
pennies = cents
if amount == 0:
    print("No change")
else:
    if dollars > 0:
        if dollars == 1:
            print(f"{dollars} Dollar")
        else:
            print(f"{dollars} Dollars")
    
    if quarters > 0:
        if quarters == 1:
            print(f"{quarters} Quarter")
        else:
            print(f"{quarters} Quarters")

    if dimes > 0:
        if dimes == 1:
            print(f"{dimes} Dime")
        else:
            print(f"{dimes} Dimes")

    if nickels > 0:
        if nickels == 1:
            print(f"{nickels} Nickel")
        else:
            print(f"{nickels} Nickels")
    
    if pennies > 0:
        if pennies == 1:
            print(f"{pennies} Penny")
        else:
            print(f"{pennies} Pennies")
