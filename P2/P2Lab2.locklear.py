# CTI 110
# Locklearc
# 9/15/26
# P2LAB2
# Dictionaries

# Car dictionary that lets us look up mpg
# From that ,pg, find gallons burned per X miles.

cars = {
    "Camaro" : 18.21,
    "Prius" : 52.36,
    "Model S" : 110,
    "Silverado" : 26,
}
print(cars)
car_keys = cars.keys()
print(car_keys)
# Choose the car
car = input("Enter a vechicle to see its mpg: ")
mpg = cars[car]
print(f"The MPG of a {car} is {mpg} is miles per gallon.")
# Ask user for miles, output gas used
miles = float(input(f"How many miles will you drive the {car}? "))
gallons_used = miles / mpg # miles divided by miles per gallong gives unit in gallons
print(f"Driving a {car} for {miles} miles will use {gallons_used:.2f} gallons of gas. ")