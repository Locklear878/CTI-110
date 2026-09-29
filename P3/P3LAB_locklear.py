# Locklear, C
# 9/28/26
# CTI-110
# P3LAB
# Make Change

# Get amount from user
# cents = round(amount * 100)
# For dollars, quarters, dimes, nickels, pennies:
#    count = cents // value
#    cents = cents % value
#    If count is 1, display the singular name
#    Else if count is more than 1, display the plural name

print("Enter the amount of money: ")
amount = float(input())
cents = round(amount * 100)

dollars = cents // 100
cents = cents % 100
if dollars ==1:
    print(dollars,"Dollar")
elif dollars >1:
    print(dollars,"Dollars")
# prints nothing if dollars is 0

quarters = cents // 25
cents = cents % 25
if quarters ==1:
    print(quarters,"Quarter")
elif quarters >1:
    print(quarters,"Quarter")

dimes = cents // 10
cents = cents %  10
if dimes ==1:
    print(dimes,"Dime")
elif dimes >1:
    print(dimes,"Dime")

nickels = cents // 5
cents = cents % 5
if nickels ==1:
    print(nickels,"Nickel")
elif nickels >1:
    print(nickels,"Nickels")
    
pennies = cents // 1
cents = cents % 1
if pennies ==1:
    print(pennies,"Penny")
elif pennies >1:
    print(pennies,"Pennies")
