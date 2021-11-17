"""
Name: Brianna Joyner
Lab11.py
"""
# I was sick on Thursday so I was told that I could make this lab up during the Tuesday lab section.
from random import randint

def read_words(wordlist):
    in_file = open(wordlist, "r")
    word_list = in_file.readlines()
    in_file.close()
    return word_list

def random_word(wordlist):
    rand_word = randint(0,len(wordlist))
    return wordlist[rand_word]

def guessed_word(word, past_guess):
    acc = ""
    for letter in word:
        if letter in past_guess:
            acc = acc + letter
        else:
            acc = acc + "_"
    return acc

def secret_word(word, past_guess):
    for letter in word:
        if letter not in past_guess:
            return False
    return True

def main():
    words = read_words("wordlist.txt")
    r_word = random_word(words)
    list = ""
    guess = input("Enter a letter: ")
    while not secret_word(r_word, guess):
        print(guessed_word(r_word, guess))
        if guess not in secret_word:
            list = list + guess + " "
        print(list)
        guess = input("Enter a letter: ")

    pass

main()
