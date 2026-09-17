# Locklear, C
# 09/17/26
# P2HW1
# Travel Expenses

# Greet the user
print("Hello!")
# Ask the user to enter the budget
budget = float(input("What is your budget? "))
# Ask user to enter destination
destination = input("Where is your destination? ")
# Ask user for amount they will spend on gas
gas = float(input("How much will you spend on gas? "))
# Ask user how much they will spend on hotel
hotel = float(input("How much will you spend on hotel? "))
# Ask user how much they will spend on food 
food = float(input("How much will you spend on food? "))
# Add expenses
expenses = gas + hotel + food

destination = "Raleigh"
budget      = 2000
expenses    = 1300
remaining   = budget - expenses

# print expenses
print(f"{"Destination:":<18} {destination:<18}")
print(f"{"Budget:":<18} ${budget:<18.2f}")
print(f"{"Gas:":<18} ${gas:<18.2f}")
print(f"{"Hotel:":<18} ${hotel:<18.2f}")
print(f"{"Food:":<18} ${food:<18.2f}")
print(f"{"Remaining:":<18} ${remaining:<18.2f}")
# print expenses
print("Total Expenses is  $" + format(expenses,".2f"))
# Subtract expenses
balance = budget - expenses
# Display results
print("Your balance is    $" + format(balance,".2f"))
