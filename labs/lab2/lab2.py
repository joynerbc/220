"""
Name: Brianna Joyner
lab2.py

Problem: These functions execute arithmetic through for loops, mostly.
"""
import math

def sum_of_threes():
    bound = eval(input("enter an upper bound: "))
    acc = 0
    for i in range(0, bound + 1, 3):
        acc = i + acc
    print(acc)

def multiplication_table():
    for H in range(1, 11):
        print()
        for L in range(1, 11):
            print(H * L, end=" ")

def triangle_area():
    a = eval(input("enter length for side a: "))
    b = eval(input("enter length for side b: "))
    c = eval(input("enter length for side c: "))
    s = (a + b + c) / 2
    area = math.sqrt(s * (s-a) * (s-b) * (s-c))
    print(area)

def sumSquares():
    lower_bound = eval(input("enter a lower range: "))
    upper_bound = eval(input("enter an upper range: "))
    acc = 0
    for i in range(lower_bound, upper_bound + 1):
        acc = acc + i ** 2
    print(acc)

def power():
    base = eval(input("enter the base value: "))
    exponent = eval(input("enter the exponent: "))
    acc = 1
    for i in range(exponent):
        acc = acc * base
    print(acc)

sum_of_threes()
multiplication_table()
triangle_area()
sumSquares()
power()