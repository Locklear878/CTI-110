# Locklear, C
# 10/8/26
# P4LAB2
# Loops

# warmups
"""
for number in (1,2,3,4):
    print(number)
for number in range(5):
    print(number)
for beer in range(99,-1):
    print(beer,"bottles of beer on the wall.")

# counting loop

for mult in range(1, 13):
    print(7 * mult)
"""

# Set up variables
# start the main loop 
again = "yes"
while again == "yes":
    # ask user for their chosen integer (0-12)
    multiplier = int(input("Enter a number 0-12: "))
    # validate (loop) number must be between 0-12
    while multiplier < 0 or multiplier > 12:
        print("That is not a valid answer.")
        multiplier = int(input("Enter a number 0-12: "))

    # print the times tables header
    print("Multiplication Table")
    print("-"*20)
    # print the times tables (loop)
    for number in range(1,13):
    # print(multiplier, "*", number, "=", number*multiplier)
        print(f"{multiplier} * {number} = {number * multiplier}")
    # ask if they want to repeat
    again = input("Run again? (yes/no) ")