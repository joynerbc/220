"""
Name: Brianna Joyner
mean.py

Problem: This code calculates average means

Certification of Authenticity:
I certify that this assignment is entirely my own work.

Questions:
1) This program will calculate three different means.
2) The number of values and actual values will be entered and the three means will be outputted
3) The program will ask the user for a number of values, the actual values,
then store those as variables, and then compute the calculations through the math library
"""
from math import *

def main():
    acc = 0
    rms_total = 0
    harm_total = 0
    geo_total = 1
    n = eval(input("enter the number of values: "))
    for _ in range(n):
        value = eval(input("enter the value: "))
        rms_total = rms_total + value ** 2
        harm_total = harm_total + (1 / value)
        geo_total = geo_total * value
    rms_average = sqrt(rms_total / n)
    harm_mean = n / harm_total
    geo_mean = (geo_total) ** (1 / n)
    print(round(rms_average, 3))
    print(round(harm_mean, 3))
    print(round(geo_mean, 3))

if __name__ == '__main__':
    main()
