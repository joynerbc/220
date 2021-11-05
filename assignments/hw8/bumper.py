"""
Name: Brianna Joyner
bumper.py

Problem:
This program creates a random generation of ball movements.

Certification of Authenticity:
I certify that this assignment is entirely my own work, with help from Angela and the CSL.
"""
from graphics import *
from random import randint
from time import sleep

def did_collide():
    circle_one_x = Circle.getCenter().getX()
    circle_one_y = Circle.getCenter().getY()
    radius_one = Circle.getRadius()
    circle_two_x = Circle.getCenter().getX()
    circle_two_y = Circle.getCenter().getY()
    radius_two = Circle.getRadius()
    x_value = (circle_one_x - circle_two_x) ** 2
    y_value = (circle_one_y - circle_two_y) **2
    dist = (x_value + y_value) ** (1/2)
    if dist <= (radius_one + radius_two):
        return True
    else:
        return False

def hit_vertical(ball, win):
    y_edge = ball.getCenter().getY() + ball.getRadius()
    if y_edge >= win.getHeight() or y_edge <= 0:
        return True
    else:
        return False

def hit_horizontal():
    x_edge = Circle.getCenter().getX() + Circle.getRadius()
    if x_edge >= win.getWidth() or x_edge <= 0:
        return True
    else:
        return False

def get_random():
    movement = randint(-move_amount, +move_amount)
    return movement

def get_random_color():
    return color_rgb()

def main():
    win_width = 500
    win_height = 500
    win = GraphWin("bumper", win_width, win_height)
    circle_one = Circle(Point(150, 150), 50)
    circle_one.draw(win)
    circle_two = Circle(Point(150, 200), 50)
    circle_two.draw(win)
    dy = 10
    dx = 10
    while win.getMouse() == None:
        while
            circle_one.move(dy, dx)
            circle_two.move(dy, dx)
            time.sleep(.1)
            get_random()
    win.getMouse()
    win.close()

if __name__ == '__main__':
    main()
