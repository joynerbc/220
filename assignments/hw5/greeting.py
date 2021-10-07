"""
Name: Brianna Joyner
greeting.py

Problem: This code makes a greeting card with a heart and an arrow.

Certification of Authenticity:
I certify that this assignment is entirely my own work, with help from the CSL.
"""
import time
from graphics import GraphWin, Point, Circle, Polygon, Text, Line

def main():
    win_width = 700
    win_height = 700
    win = GraphWin("Greeting Card", win_width, win_height)
    heart_circle_one = Circle(Point(165, 200), 100)
    heart_circle_one.setFill("Red")
    heart_circle_one.setOutline("Red")
    heart_circle_one.draw(win)
    circle_one_radius = heart_circle_one.getRadius()
    heart_circle_two = Circle(Point(heart_circle_one.getCenter().getX() + circle_one_radius * 2, 200), 100)
    heart_circle_two.setFill("Red")
    heart_circle_two.setOutline("Red")
    heart_circle_two.draw(win)
    p1 = Point(heart_circle_one.getCenter().getX() - circle_one_radius, 210)
    p2 = Point(heart_circle_two.getCenter().getX() + circle_one_radius, 210)
    p3 = Point(heart_circle_one.getCenter().getX() + circle_one_radius, 500)
    heart_triangle = Polygon(p1, p2, p3)
    heart_triangle.setFill("Red")
    heart_triangle.setOutline("Red")
    heart_triangle.draw(win)
    open_message = Text(Point(350, 650), "Happy Valentine's Day!")
    open_message.draw(win)
    line = Line(Point(0, 700), Point(50, 600))
    line.setArrow('last')
    line.draw(win)
    for _ in range(50):
        line.move(10, -10)
        time.sleep(.1)
    open_message.undraw()
    close_message = Text(Point(350, 660), "Click anywhere to close")
    close_message.draw(win)
    win.getMouse()
    win.close()

if __name__ == '__main__':
    main()
