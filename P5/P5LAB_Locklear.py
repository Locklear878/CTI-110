# Locklear, C
# 10/29/26
# P5LAB
# Self Checkout machine simulator - makes change
import random # required for random.unifrom()

# Put other functions here
# Turn the program P3LAB into a funstion called disperse_change. It should take one float parameter and have no return value.
def disperse_change(amount):
    # Print out the change needed
    # Input: float
    # Return: nothing
    print(f"Change is: ${amount:.2f}")
    print()
    # Put your P3LAB code here: Print the number of dollars, quarters, dimes, nickels, and pennies.    
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

# main
def main():
    # Declare variables
    cost = 0.0
    amount_paid = 0.0
    change_owed = 0.0
    print("Welcome to the self-checkout sim.")
    # Generate a random float value for the cost - uniform picks a number in this range
    cost = round(random.uniform(0.01, 100.00), 2)
    print(f"You owe: ${cost:.2f}")
    # Ask the user how much $ they put in
    amount_paid = float(input("How much money do you want to put in the self-checkout? $"))
    # Calculate change owed
    change_owed = amount_paid - cost

    print("Here is your change:")
    disperse_change(change_owed)




# Last line - start the program
main()