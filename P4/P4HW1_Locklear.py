# Locklear, Chelsea
# 10/22/26
# P4HW1 
# Building on P2HW2

# ask the user how many scores they want to enter
scores = int(input("How many scores do you want to enter? "))
# create a loop 
for i in range(scores):
    score = int(input(f"Enter score #{i + 1}: "))
    while score < 0 or score > 100:
        print("INVALID Score Entered!!!")
        print("Score entered should be between 0 and 100")
        score = int(input("Enter score #3 again: "))
scores = []
print("-" * 10 + "Results" + "-" * 10)
# print lowest score
low = min(scores)

average = sum / len(scores)

