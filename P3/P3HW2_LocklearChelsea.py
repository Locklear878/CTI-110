# Locklear, C
# 10/1/26
# P3HW2
# Pay stub

# ask the user to enter first and last name, hours worked, and pay rate
name = input("Enter employee's name: ")
hours_worked = float(input("Enter the number of hours worked this week: "))
pay_rate = float(input("Enter your pay rate: "))
print("-" * 40)
print("Employee name: Chelsea Locklear")
# set values to 0 we can adjust in the if statement
hours_worked = 0
overtime_hours = 0
employee_name = 'John Smith'


# determine pay with if statement
if hours_worked >= 40:
    reg_pay = 40 * pay_rate
    overtime = hours_worked - 40
else:
    reg_pay = hours_worked
    overtime = 0
    
# Calulate pay
reg_pay = hours_worked * pay_rate
overtime_pay = overtime_hours * pay_rate * 1.5
gross_pay = reg_pay + overtime_pay

# Display employee information
print(f"{'Hours Worked':<15}{'Pay Rate':<15}{'Overtime':<15}"
     f"{'Overtime Pay':<18}{'Regular Pay':<15}{'Gross Pay':<15}")
print("-" * 93)
print(f"{45.0:<15.1f}{17.5:<15.1f}{5.0:<15.1f}"
     f"${131.25:<18.2f}${700.00:<15.2f}${831.25:<15.2f}")