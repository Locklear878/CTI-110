# Locklear, Chelsea
# 9/8/26
# P1HW2 
# Calculating travel expense

# Greet the user
print("Hello!")

# Ask user to enter their budget
# print("Enter your budget")
budget = float(input("What is your budget? "))
# Ask user to enter travel destination
# print("Enter travel destination")
destination = input("Where is your destination? ")
# Ask user for amount they will spend on gas
gas = float(input("How much will you spend on gas? "))
# Ask user for amount they will spend on accommodation
accommodation = float(input("How much will you spend on accommodation? "))
# Ask user for amount they will spend on food
food = float(input("How much will you spend on food? "))
# Add expenses
expenses = gas + accommodation + food
# print expenses
print("Total Expenses $", format(expenses,".2f"))
# Subtract expenses
balance = budget - expenses
# Display results
print("Your balance is $", format(balance,".2f"))
