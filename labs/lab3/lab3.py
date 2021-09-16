"""
Name: Brianna Joyner
lab3.py

Problem: These functions execute for loops to do arithmetic.
"""
import math

def average():
    acc = 0
    hw = eval(input("enter the number of grades: "))
    for i in range(hw):
        grade = eval(input("enter your grade on HW " + str(i + 1)))
        acc = acc + grade
    print(acc / hw)

def tip_jar():
    acc = 0
    for i in range(5):
        donation = eval(input("enter the donation amount: "))
        acc = acc + donation
    print(acc)

def newton():
    x = eval(input("enter the value of x: "))
    refine = eval(input("enter the number of times to refine the approximation: "))
    approx = x / 2
    for i in range(refine):
        approx = (approx + (x / approx)) / 2
    print(approx)

def sequence():
    n = eval(input("enter the number of terms in the series: "))
    for i in range(1, n + 1):
        y = 1 + (i // 2 * 2)
        print(y)

def pi():
    acc = 1
    terms = eval(input("enter the number of terms in the series: "))
    for i in range(terms):
        num = 2 + (i // 2 * 2)
        denom = 1 + ((i + 1) // 2 * 2)
        frac = num / denom
        acc = acc * frac
    print(acc * 2)

average()
tip_jar()
newton()
sequence()
pi()