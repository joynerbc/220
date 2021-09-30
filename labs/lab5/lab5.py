"""
Name: Brianna Joyner
lab5.py
"""

from graphics import *
import math

def triangle():
    win_width = 500
    win_height = 500
    win = GraphWin("Draw a Triangle", win_width, win_height)
    p1 = win.getMouse()
    p2 = win.getMouse()
    p3 = win.getMouse()
    triangle = Polygon(p1, p2, p3)
    triangle.draw(win)
    a = math.sqrt((p1.getX() - p2.getX()) ** 2 + (p1.getY() - p2.getY()) ** 2)
    b = math.sqrt((p2.getX() - p3.getX()) ** 2 + (p2.getY() - p3.getY()) ** 2)
    c = math.sqrt((p1.getX() - p3.getX()) ** 2 + (p1.getY() - p3.getY()) ** 2)
    s = (a + b + c) / 2
    area = math.sqrt(a * (s - a) * (s - b) * (s - c))
    perimeter = a + b + c
    area_text = Text(Point(200, 20), "The area is " + str(area))
    area_text.draw(win)
    per_text = Text(Point(200, 40), "The perimeter is " + str(perimeter))
    per_text.draw(win)
    win.getMouse()
    win.close()

def color_shape():
    '''Create code to allow a user to color a shape by entering rgb amounts'''
    # create window
    win_width = 400
    win_height = 400
    win = GraphWin("Color Shape", win_width, win_height)
    win.setBackground("white")
    # create text instructions
    msg = "Enter color values between 0 - 255\nClick window to color shape"
    inst = Text(Point(win_width / 2, win_height - 20), msg)
    inst.draw(win)
    # create circle in window's center
    shape = Circle(Point(win_width / 2, win_height / 2 - 30), 50)
    shape.draw(win)
    # redTexPt is 50 pixels to the left and forty pixels down from center
    red_text_pt = Point(win_width / 2 - 50, win_height / 2 + 40)
    red_text = Text(red_text_pt, "Red: ")
    red_text.setTextColor("red")
    # green_text_pt is 30 pixels down from red
    green_text_pt = red_text_pt.clone()
    green_text_pt.move(0, 30)
    green_text = Text(green_text_pt, "Green: ")
    green_text.setTextColor("green")
    # blue_text_pt is 60 pixels down from red
    blue_text_pt = red_text_pt.clone()
    blue_text_pt.move(0, 60)
    blue_text = Text(blue_text_pt, "Blue: ")
    blue_text.setTextColor("blue")
    # display rgb text
    red_text.draw(win)
    green_text.draw(win)
    blue_text.draw(win)
    red_box = Entry(Point(win_width / 2, win_height / 2 + 40), 5)
    green_box = Entry(Point(win_width / 2, win_height / 2 + 70), 5)
    blue_box = Entry(Point(win_width / 2, win_height / 2 + 100), 5)
    red_box.draw(win)
    green_box.draw(win)
    blue_box.draw(win)
    for _ in range(5):
        win.getMouse()
        red = int(red_box.getText())
        green = int(green_box.getText())
        blue = int(blue_box.getText())
        color = color_rgb(red, green, blue)
        shape.setFill(color)
    win.getMouse()
    win.close()

def process_string():
    string = input("enter a string: ")
    print(string[0])
    print(string[-1])
    print(string[2:6])
    print(string[0] + string[-1])
    print(string[0:3] * 10)
    for i in range(len(string)):
        print(string[i])
    print(len(string))

def process_list():
    pt = Point(5, 10)
    values = [5, "hi", 2.5, "there", pt, "7.2"]
    x = values[1] + values[3]
    print(x)
    x = values[0] + float(values[5])
    print(x)
    x = values[1] * 5
    print(x)
    x = [values[2], values[3], values[4]]
    print(x)
    x = [values[2], values[3], values[0]]
    print(x)
    x = [values[2], values[0], float(values[5])]
    print(x)
    x = values[0] + values[2] + float(values[5])
    print(x)
    x = len(values)
    print(x)

def another_series():
    acc = 0
    n = eval(input("Enter the number of terms in the series: "))
    for i in range(n):
        y = 2 + 2 * (i % 3)
        print(y, end=" ")
        acc = acc + y
    print(acc)

def target():
    win_width = 500
    win_height = 500
    win = GraphWin("Archery Target", win_width, win_height)
    z = win_width = win_height
    r = z / 10
    white_circle = Circle(Point(z / 2, z / 2), r * 5)
    white_circle.setFill("White")
    white_circle.draw(win)
    black_circle = Circle(Point(z / 2, z / 2), r * 4)
    black_circle.setFill("Black")
    black_circle.draw(win)
    blue_circle = Circle(Point(z / 2, z / 2), r * 3)
    blue_circle.setFill("Blue")
    blue_circle.draw(win)
    red_circle = Circle(Point(z / 2, z / 2), r * 2)
    red_circle.setFill("Red")
    red_circle.draw(win)
    yellow_circle = Circle(Point(z / 2, z / 2), r)
    yellow_circle.setFill("Yellow")
    yellow_circle.draw(win)
    win.getMouse()
    win.close()

triangle()
color_shape()
process_string()
process_list()
another_series()
target()
