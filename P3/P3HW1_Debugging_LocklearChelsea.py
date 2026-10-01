# Locklear, C
# 10/1/26
# Debugging
# Debug the current file


# This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules

mod_1 = float(input(" Enter the grade for Module 1: "))
mod_2 = float(input(" Enter the grade for Module 2: "))
mod_3 = float(input(" Enter the grade for Module 3: "))
mod_4 = float(input(" Enter the grade for Module 4: "))
mod_5 = float(input(" Enter the grade for Module 5: "))
mod_6 = float(input(" Enter the grade for Module 6: "))

# add grades entered to a list

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]
# TO DO: determine lowest, highest , sum and average for grades

low = min(grades)
high = max(grades)
sum = sum(grades)
average = sum / len(grades)

#print list of grades
print(f"{"Module 1:":<10} {mod_1:<10}")
print(f"{"Module 2:":<10} {mod_2:<10}")
print(f"{"Module 3:":<10} {mod_3:<10}")
print(f"{"Module 4:":<10} {mod_4:<10}")
print(f"{"Module 5:":<10} {mod_5:<10}")
print(f"{"Module 6:":<10} {mod_6:<10}")

#calulate the higest, lowest, average, and sum of grades
print("-" * 12 + "Results" + "-" *12)
print(f"{"Lowest Grade: ":<15} {min(grades):<10}")
print(f"{"Highest Grade: ":<15} {max(grades):<10}")
print(f"{"Sum of Grade: ":<15} {sum:<10}")
print(f"{"Average: ":<15} {average:<10.2f}")

print("-" * 40)

# determine letter grade for average
if average >= 90:
    print('Your grade is: A')
elif average >= 80:
    print('Your grade is: B')
elif average >= 70:
    print('Your grade is: C')
elif average >= 60:
    print('Your grade is: D')
else:
    print('Your grade is: F') # TO DO: finish this





