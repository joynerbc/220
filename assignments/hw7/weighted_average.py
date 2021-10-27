"""
Name: Brianna Joyner
weighted_average.py

Problem:
This program computes the weighted average.

Certification of Authenticity:
I certify that this assignment is entirely my own work,
with help from the CSL and Angela.
"""

def weighted_average(in_file_name, out_file_name):
    in_read_file = open(in_file_name, "r")
    out_write_file = open(out_file_name, "w")
    for every_line in in_read_file:
        split_line = every_line.split(":")
        weight_grade = split_line[1]
        weight_grade = weight_grade.split()
        total = 0
        q = 0
        for i in range(len(weight_grade)//2):
             q = q + int(weight_grade[2 * i])
             total = total + int(weight_grade[2 * i] * int(weight_grade[2 * i + 1]))
        avg = total / 100
        if q > 100:
            print(split_line[0] + "'s average: Error: The weights are more than 100.", file=out_write_file)
        elif q < 100:
            print(split_line[0] + "'s average: Error: The weights are less than 100.", file=out_write_file)
        else:
            print("{0}'s average: {1}".format(split_line[0], round(avg, 1)), file=out_write_file)

def main():
    weighted_average("grades.txt", "avg.txt")

if __name__ == '__main__':
    main()
