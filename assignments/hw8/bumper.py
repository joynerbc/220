"""
Name: Brianna Joyner
bumper.py

Problem:
This program creates a random generation of ball movements across a window.

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
    dy = get_random(40)
    dx = get_random(40)
    get_random(40)
    for i in range():
        circle_two.move(dx, dy)
        time.sleep(.5)
    randint(-40, 40)
    did_collide(circle_one, circle_two)
    if hit_vertical(Circle, win):
        dy = dy * -1
        return dy
    elif did_collide(circle_one, circle_two):
        dx = dx * -1
        return dx
    elif did_collide(circle_one, circle_two):
        dy = dy * -1
        return dy
    elif hit_horizontal(Circle, win):
        dx = dx * -1
        return dx
    acc = 0
    while not hit_vertical(circle_one, win) or hit_horizontal(circle_two, win):
        get_random_color()
        acc = acc + circle_one.move(20, 200)
        return acc
    win.getMouse()
    win.close()

if __name__ == '__main__':
    main()
