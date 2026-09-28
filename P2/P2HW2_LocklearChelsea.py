# Locklear, Chelsea
# 09/22/26
# P2HW2
# Understanding list

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

# print list of grades
print(f"{"Module 1:":<10} {module1:<10}")
print(f"{"Module 2:":<10} {module2:<10}")
print(f"{"Module 3:":<10} {module3:<10}")
print(f"{"Module 4:":<10} {module4:<10}")
print(f"{"Module 5:":<10} {module5:<10}")
print(f"{"Module 6:":<10} {module6:<10}")

grades = [module1,module2,module3,module4,module5,module6]
print("-" * 12 + "Results" + "-" * 12)
# calculate lowest grade
print("Lowest grade:  ",min(grades))
# calculate highest grade
print("Highest grade: ",max(grades))
# calculate sum of grades
grade_sum = sum(grades)
print("Sum of Grades: ",grade_sum)
# average 
size = len(grades)
average = grade_sum / size
print("Average grade:  " + format(average,".2f"))

print("-" * 31)