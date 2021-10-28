"""
Name: Brianna Joyner
lab9.py
"""
import math
from graphics import *

def addTen(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] + 10

def squareEach(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] ** 2

def sumList(nums):
    acc = 0
    for i in range(len(nums)):
        acc = acc + nums[i]
    return acc

def toNumbers(strList):
    for i in range(len(strList)):
        strList[i] = float(strList[i])

def writesumofSquares():
    input_file_name = input("input the filename: ")
    infile = open(input_file_name, "r")
    outfile = open("wss.txt", "w+")
    for line in infile:
        line = line.split()
        toNumbers(line)
        squareEach(line)
        sum = sumList(line)
        outfile.write("Sum = " + str(sum))

def starter():
    weight = eval(input("enter the weight: "))
    wins = eval(input("enter the numbers of wins: "))
    if weight >= 150 and weight < 160 and wins >= 5:
        print("is starter")
    elif weight > 199 or wins > 20:
        print("is starter")
    else:
        print("not starter")

def leapYear(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def circleOverlap():
    win = GraphWin("Circle Overlap", 400, 400)
    p1 = win.getMouse()
    p2 = win.getMouse()
    r1 = math.sqrt((p2.getX() - p1.getX()) ** 2 + (p2.getY() - p1.getY()) ** 2)
    circle_one = Circle(p1, r1)
    circle_one.draw(win)
    p3 = win.getMouse()
    p4 = win.getMouse()
    r2 = math.sqrt((p4.getX() - p3.getX()) ** 2 + (p4.getY() - p3.getY()) ** 2)
    circle_two = Circle(p3, r2)
    circle_two.draw(win)
    distance = math.sqrt((p1.getX() - p3.getX()) ** 2 + (p1.getY() - p3.getY()) ** 2)
    if distance <= r1 + r2:
        overlap_text = Text(Point(200, 390), "the circles overlap")
        overlap_text.draw(win)
    else:
        no_overlap_text = Text(Point(200, 390), "the circles do not overlap")
        no_overlap_text.draw(win)
    win.getMouse()
    win.close()

def main():
    x = [5, 2, -3]
    addTen(x)
    print(x)
    starter()
    leapYear()
    circleOverlap()
    pass

main()
