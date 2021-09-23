"""
Name: Brianna Joyner
lab4.py
"""

from graphics import *
import math

def squares():
    """  <---  You can use tripled quotes to write a multi-line comment....

    Modify the following function to:

    Draw squares (20 X 20) instead of circles. Make sure that the center of the square
    is at the point where the user clicks. Make the window 400 by 400.

    Have each successive click draw an additional square on the screen (rather
    than just moving the existing one).

    Display a message on the window "Click again to quit" after the loop, and
    wait for a final click before closing the window.
    """
    # Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("Lab 4", width, height)

    # number of times user can move circle
    num_clicks = 5

    # create a space to instruct user
    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to move square")
    instructions.draw(win)

    # builds a circle
    shape = Rectangle(Point(50, 50), Point(70, 70))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    # allows the user to click multiple times to move the circle
    for i in range(num_clicks):
        p = win.getMouse()
        shape = Rectangle(Point(p.getX() - 10, p.getY() - 10), Point(p.getX() + 10, p.getY() + 10))
        shape.setOutline("red")
        shape.setFill("red")
        shape.draw(win)

    instructions.undraw()
    instructions.setText("Click to close")
    instructions.draw(win)

    win.getMouse()
    win.close()

def rectangle():
    """
    This program displays information about a rectangle drawn by the user.
    Input: Two mouse clicks for the opposite corners of a rectangle.
    Output: Draw the rectangle.
         Print the perimeter and area of the rectangle.
    Formulas: area = (length)(width)   and    perimeter = 2(length+width)
    """
    win = GraphWin("WiRectanglewsndow", 700, 500)
    p1 = win.getMouse()
    p2 = win.getMouse()
    rec = Rectangle(p1, p2)
    rec.draw(win)
    length = abs(p2.getX() - p1.getX())
    width = abs(p2.getY() - p1.getY())
    area = length * width
    perimeter = 2 * (length + width)
    area_text = Text(Point(200, 20), "The area is " + str(area))
    area_text.draw(win)
    per_text = Text(Point(200, 40), "The perimeter is " + str(perimeter))
    per_text.draw(win)

    win.getMouse()
    win.close()



def circle():
    win = GraphWin("Circle", 700, 500)
    p1 = win.getMouse()
    p2 = win.getMouse()
    x1 = p1.getX()
    x2 = p2.getX()
    y1 = p1.getY()
    y2 = p2.getY()
    r = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    r_text = Text(Point(200, 20), "The radius is " + str(r))
    r_text.draw(win)
    circle = Circle(p1, r)
    circle.draw(win)
    win.getMouse()
    win.close()

def pi2():
    n = eval(input("enter the number of terms to sum: "))
    acc = 0
    for i in range(n):
        num = 4 * ((-1) ** i)
        denom = 1 + (2 * i)
        frac = num / denom
        acc = acc + frac
    print(math.pi - acc)

squares()
rectangle()
circle()
pi2()