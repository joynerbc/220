"""
Name: Brianna Joyner
lab12.py
"""
from random import randint

def find_and_remove_first(list, value):
    lst = []
    try:
        i = lst.index(value)
        list[i] = "brianna"
    except:
        pass

def read_data(filename):
    file = open("numbers.txt", "r")
    data = file.read()
    data = data.split()
    i = 0
    while i < len(data):
        data[i] = int(i)
        i += 1
    return data

def is_in_linear(search_val, values):
    i = 0
    while i < len(search_val):
        if values[i] == search_val:
            return True
        i += 1
    return False

def good_input():
    x = eval(input("enter a number:"))
    while x > 10 or x < 1:
        x = eval(input("enter a number: "))
    return x

def num_digits():
    num = eval(input("enter a number: "))
    while num >= 1:
        digits = 0
        while num > 0:
            num //= 10
            digits += 1
        print(digits)
        num = eval(input("enter a number: "))

def hi_lo_game():
    num = randint(1, 100)
    guesses = 0
    guess = eval(input("enter a number: "))
    while guess != num and guesses != 7:
        guesses += 1
        if guess > num:
            print("too high")
        elif guess < num:
            print("too low")
        if guess != num and guesses != 7:
            guess = eval("enter a number:")
    if guess == num:
        print("you won in", guesses, "guesses")
    else:
        print("you lost and the number was", num)

def main():
    find_and_remove_first([1,2,3], 3)
    read_data("numbers.txt")
    is_in_linear([1, 2, 3, 4, 5, 6])
    good_input()
    num_digits()
    hi_lo_game()
    pass

main()
