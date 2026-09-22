# Locklear, Chelsea
# 09/22/26
# P2HW2
# Understanding list

# Greet the user
print("Hello!")
# ask user for module 1 grade
module1 = float(input("What is the grade for Module 1? "))
# ask use for module 2 grade
module2 = float(input("What is the grade for Module 2? "))
# ask user for module 3 grade
module3 = float(input("What is the grade for Module 3? "))
# ask user for module 4 grade
module4 = float(input("What is the grade for Module 4? "))
# ask user for module 5 grade
module5 = float(input("What is the grade for Module 5? "))
# ask user for module 6 grade
module6 = float(input("What is the grade for Module 6? "))
# make list of all grades
# commented out the lines below
"""
module1 = 65.5
module2 = 88
module3 = 78.5
module4 = 90
module5 = 61
module6 = 92
"""
# print list of grades
print(f"{"Module 1:":<10} {module1:<10}")
print(f"{"Module 2:":<10} {module2:<10}")
print(f"{"Module 3:":<10} {module3:<10}")
print(f"{"Module 4:":<10} {module4:<10}")
print(f"{"Module 5:":<10} {module5:<10}")
print(f"{"Module 6:":<10} {module6:<10}")

grades = [module1,module2,module3,module4,module4,module5,module6]

# calculate lowest grade
print("Lowest grade is",min(grades))
# calculate highest grade
print("Highest grade is",max(grades))
# calculate sum of grades
sum = sum(grades)
print("Total grade is ",sum)
# average 
size = len(grades)
average = sum / size
print("The average of grades is",average)