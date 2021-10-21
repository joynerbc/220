"""
Name: Brianna Joyner
lab8.py
"""
import math
from encryption import encode, encode_better

def number_words(in_file_name, out_file_name):
    in_file = open(in_file_name, "r")
    output = open(out_file_name, "w+")
    i = 1
    for line in in_file:
        words = line.split()
        for word in words:
            output.write(str(i) + word + "\n")
            i += 1

def hourly_wages(in_file_name, out_file_name):
    in_file = open(in_file_name, "r")
    output = open(out_file_name, "w+")
    for line in in_file:
        parts = line.split()
        wage = float(parts[2])
        wage = wage + 1.65
        wage = wage * int(parts[3])
        output.write(parts[0] + parts[1] + str(wage) + "\n")

def calc_check_sum(isbn):
    acc = 0
    for i in range(10):
        position = 10 - i
        acc = acc + (position * int(isbn[i]))
    return acc

def send_message(file, friend):
    infile = open(file, "r")
    outfile = open(friend + ".txt", "w+")
    for line in infile:
        outfile.write(line)

def send_safe_message(file, friend, key):
    infile = open(file, "r")
    outfile = open(friend + ".txt", "w+")
    for line in infile:
        outfile.write(encode(line, key))

def send_uncrackable_message(file, friend, pad):
    infile = open(file, "r")
    pad_file = open(pad, "r")
    outfile = open(friend + ".txt", "w+")
    key = pad_file.read()
    for line in infile:
        outfile.write(encode_better(line, key))

def main():
   number_words("Walrus.txt", "wout.txt")
   hourly_wages("hourly_wages.txt", "newwages.txt")
   calc_check_sum("0012345678")
   send_message("message.txt", "bob")
   send_safe_message("secret_message.txt", "hunter", 3)
   send_uncrackable_message("safest_message.txt", "safest", "pad.txt")

main()
