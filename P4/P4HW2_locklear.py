# Locklear, C
# 10/25/26
# P4HW2 building off of P3HW2
# Pay stub
# set variables
hours_worked = 0
overtime_hours = 0
num_employess = 0
total_overtime_pay = 0
total_gross_pay = 0
total_reg_pay = 0
# for employee name
name = input("Enter employee's name or 'Done' to terminate: ")
# start the loop
while name != 'Done':
    # employee counter
    num_employess += 1
       # hours
    hours_worked = float(input(f"How many hours did {name} work? "))
    # payrate
    pay_rate = float(input(f"Enter the {name}'s pay rate: "))
    # determine pay with if statement
    if hours_worked >= 40:
        reg_pay = 40 * pay_rate
        overtime = hours_worked - 40
    else:
        reg_pay = hours_worked
        overtime = 0
        reg_pay = hours_worked * pay_rate
     # calculations
    overtime_pay = overtime * pay_rate * 1.5
    gross_pay = reg_pay + overtime_pay
    # Display results
    print(f"Employee name: {name}")
    print(f"{'Hours Worked':<15}{'Pay Rate':<15}{'Overtime':<15}"
     f"{'Overtime Pay':<18}{'Regular Pay':<15}{'Gross Pay':<15}")
    print("-" * 93)
    print(f"{hours_worked:<15.1f}{pay_rate:<15.2f}{overtime:<15.1f}"
        f"{overtime_pay:<18.2f}${reg_pay:<15.2f}${gross_pay:<15.2f}")
    name = input(f"Enter employee's name or 'Done' to terminate: ")
    # caluclations for amounts paid
    total_overtime_pay += overtime_pay
    total_reg_pay += reg_pay
    total_gross_pay += gross_pay
# Display results
print(f"Total number of employees enetered: {num_employess}")
print(f"Total amount paid for overtime: ${total_overtime_pay:,.2f}")
print(f"Total amount paid for regular hours: ${total_reg_pay:,.2f}")
print(f"Total amount paid on gross: ${total_gross_pay:,.2f}")

