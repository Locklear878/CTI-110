# Locklear, Chelsea
# 10/22/26
# P4HW1 
# Building on P2HW2

# ask the user how many scores they want to enter
scores = int(input("How many scores do you want to enter? "))
# create a list
scores = []
average = 0
# create a loop 
for i in range(5):
    score = float(input(f"Enter score #{i + 1}: "))
    scores.append(score)
    
    while score < 0 or score > 100:
            print("INVALID Score Entered!!!")
            print("Score entered should be between 0 and 100")
            score = int(input("Enter score #3 again: "))

# print lowest score
lowest_score = min(scores)
# creat a modified list and drop the lowest score
modified_scores = scores.copy()
modified_scores.remove(lowest_score)
 # Calculate the average
average = sum(modified_scores) / len(modified_scores)
            
# determine letter grade
if average >= 90:
    letter_grade = "A"
elif average >= 80:
    letter_grade = "B"
elif average >= 70:
    letter_grade = "C"
elif average >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"

# Display the results
print("-" * 10 + "Results" + "-" * 10)
print(f"Lowest Score  : {lowest_score}")
print(f"Modified List : {modified_scores}")
print(f"Scores Average: {average}")
print(f"{"Grade         :"} {letter_grade}")
print("-" * 40)