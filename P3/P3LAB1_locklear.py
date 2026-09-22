# CTI 110
# Locklear,C
# 09/22/26
# P3LAB1
# If statements 

# main() -- this is the programs starting points.
# you don't need to use it, but it's a very good idea.
def main():
    # Part 1 - Level Check
    print("Hello and welcome to the dungeon.")
    level = int(input("What level are you? "))
    if level >= 21:
        print("You can enter the dungeon.")
    else:
        print("Try leveling up first.")

    # Part 2 - List your potions
    # print("Time to enter the dungeon.")
    potions = int(input("How many health potions are you carrying? "))
    if potions == 0:
        print("Warning: You have no potions equipped! Entering without healing is dangerous.")
    elif potions ==1:
        print(f"You have {potions} health potion.")
    elif potions <=1:
        print(f"You have {potions} health potions.")
    else:
        print(f"How did you get {potions}???")
    # Part 3 - Boss Battle
    print ("You are facing the DELUXE OGRE MAGE!")
    print("This will be a hard fight...")
    if level >= 25:
        # You're tough enough to hit them
        if potions > 3:
            print("It takes three potions to get him to low health!")
            print("***YOU WIN***")
        else:
            print("You run out of healing before he's weakend.")
            print("***GAME OVER***")
    else:
        print("His armor is too strong!")
        print("***GAME OVER***")

# at the bottom -- start the program
main()