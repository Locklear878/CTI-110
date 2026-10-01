# Locklear, C
# 10/1/26
# P3HW2
# Pay stub

# ask the user to enter first and last name, hours worked, and pay rate
name = input("Enter your first and last name: ")
hours_worked = float(input("Enter the number of hours worked this week: "))
pay_rate = float(input("Enter your pay rate: "))
# set values to 0 we can adjust in the if statement
hours_worked = 0
reg_pay = 0
overtime = 0


# determine pay with if statement
if hours_worked >= 40:
    reg_pay = 40 * pay_rate
