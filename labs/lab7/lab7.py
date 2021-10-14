"""
Name: Brianna Joyner
Partner: <your partner's name goes here – first and last>
lab7.py
"""
import math

def cash_conversion():
    x = eval(input("enter an integer: "))
    print("{:2f}".format(x))

def encode():
    s = input("enter a message: ")
    k = eval(input("enter an integer key value: "))
    acc = " "
    for c in s:
        i = ord(c)
        c = k + i
        c = chr(c)
        acc = acc + c
    print(acc)

def sphere_area(radius):
    area = 4 * math.pi * (radius ** 2)
    return area

def sphere_volume(radius):
    volume = (4 / 3) * math.pi * (radius ** 3)
    return volume

def sum_n(n):
    acc = 0
    for i in range(n):
        acc += 1
    return acc

def sum_n_cubes(n):
    acc = 0
    for i in range(n):
        acc += i ** 3
    return acc

def encode_better():
    string = input("Enter a sentence: ")
    k = (input("Enter a key: "))
    acc = " "
    for i in range(len(string)):
        c = string[i]
        key = k[i % len(k)]
        c = ord(c)
        key = ord(key) - 97
        key = (key + c)
        c = chr(key)
        acc = acc + c
    print(acc)

def main():
    cash_conversion()
    encode()
    print(sphere_area(3))
    print(sphere_volume(5))
    print(sum_n(7))
    print(sum_n_cubes(10))
    encode_better()
    pass
