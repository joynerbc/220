"""
Name: Brianna Joyner
lab6.py
"""


def name_reverse():
    name = input("Enter your name in first-last order: ")
    name = name.split()
    print(name[1] + "," + name[0])

def company_name():
    company_name = input("Enter the company three-part internet domain: ")
    company_name = company_name.split(".")
    print(company_name[1])

def initials():
    names = eval(input("Enter the number of names: "))
    for i in range(names):
        first_name = input("Enter the first name of the student: ")
        last_name = input("Enter the last name of the student: ")
        print(first_name[0] + last_name[0])

def names():
    names = input("Enter a list of names separated by commas: ")
    names = names.split(",")
    for name in names:
        parts = name.split()
        print("The initials are: ",  parts[0][0] + parts[1][0])

def thirds():
    n = eval(input("Enter the number of sentences: "))
    for _ in range(n):
        sentence = input("Enter a sentence: ")
        print(sentence[2::3])

def word_average():
    sentence = input("Enter a sentence: ")
    acc = 0
    sentence = sentence.split()
    for word in sentence:
        acc = len(word) + acc
    print(acc / len(sentence))

def pig_latin():
    sentence = input("Enter a sentence: ")
    sentence = sentence.lower()
    sentence = sentence.split()
    for word in sentence:
        print(word[1:] + word[0] + "ay")

def main():
    name_reverse()
    company_name()
    initials()
    names()
    thirds()
    word_average()
    pig_latin()

main()
