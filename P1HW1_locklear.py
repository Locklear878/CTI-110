# CTI-110
# P1HW1 - Math 
# Locklear, C
# 9/8/26
# Do some math processing

# PART 1 - EXPONENTS

# PART 2 - ADDITION SUBTRACTION
# 3 numbers, start, add_this, sub_this
start = int(input("Enter the staring interger: "))
print("you typed", start)
add_this = int(input("Enter interger to add: "))
sub_this = int(input("Enter integer to subtract: "))
#Calculate the anser
answer = start + add_this - sub_this
# Print the anser
print()
print() # That gives 2 newlines, so would print("\n")
# should look like: "10 + 4 - 2 is equal to 12"
print(start, "+", add_this, "-", sub_this, "is equal to", answer)
print(f"{start} + {add_this} - {sub_this} is equal to {answer}")
