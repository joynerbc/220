"""
Name: Brianna Joyner
lab1.py

Problem: These functions calculate different equations with inputs
"""


def calc_area():
    length = 20
    width = 5
    area = length * width
    print("Area =", area)


def calc_rec_area():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    area = length * width
    print("Area =", area)


def calc_volume():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    height = eval(input("Enter the height: "))
    volume = length * width * height
    print("Volume =", volume)


def shooting_percentage():
    total_shots = eval(input("Enter the total shots: "))
    shots_made = eval(input("Enter the shots made: "))
    percentage = (shots_made / total_shots) * 100
    print("Shooting percentage =", percentage)


def coffee():
    pounds = eval(input("Enter the number of pounds: "))
    pounds_coffee = 10.50 * pounds
    pounds_shipping = 0.86 * pounds
    fixed = 1.50
    total_price = fixed + pounds_coffee + pounds_shipping
    print("Price of coffee =", total_price)


def kilometers_to_miles():
    kilometers = eval(input("Enter the number of kilometers: "))
    miles = kilometers / 1.61
    print("Number of miles =", miles)

calc_area()
calc_rec_area()
calc_volume()
shooting_percentage()
coffee()
kilometers_to_miles()