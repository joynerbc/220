"""
Name: Brianna Joyner
lab13.py
"""
from random import randint

def is_in_binary(search, values):
    midpoint = len(values) // 2
    while search != values[midpoint] and len(values) != 1:
        if search < values[midpoint]:
            values = values[midpoint:]
        else:
            values = values[:midpoint]
        midpoint = len(values) // 2
    if search == values[midpoint]:
        return True
    return False

def selection_sort(values):
    for i in range(len(values)):
        lowest = values[i]
        position = i
        for j in range(i, len(values)):
            if values[j] < lowest:
                lowest = values[j]
                position = j
        values[i], values[position] = values[position], values[i]

def get_area(rect):
    return randint(1, 100)

def rect_sort(values):
    dictionary = {}
    areas = []
    for rect in values:
        dictionary[get_area(rect)] = rect
        areas.append(get_area(rect))
    selection_sort(areas)
    for i in range(len(areas)):
        values[i] = dictionary[areas[i]]

def trade_alert(filename):
    in_file = open("trades.txt", "r")
    data = in_file.read().split()
    i = 0
    while i < len(data):
        num = eval(data[i])
        if num > 500 and num <= 830:
            print(i + 1, "warning!")
        if num > 830:
            print(i + 1, "alert!")

def main():
    print(is_in_binary(1, [1, 2, 3, 4, 5]))
    print(is_in_binary(10, [1, 2, 3, 4, 5]))
    x = [5, 2, 1, 3]
    selection_sort(x)
    print(x)
    pass

main()
