"""
Name: Brianna Joyner
button.py

Problem: This program creates a button class

Certification of Authenticity:
I certify that this assignment is entirely my own work, with help from the CSL.
"""
from graphics import *

class Button:
    def __init__(self, rectangle_shape, string_label):
        self.rectangle_shape = rectangle_shape
        self.text = Text(rectangle_shape.getCenter(), string_label)

    def get_label(self):
        return self.text.getText()

    def draw(self, win):
        self.rectangle_shape.draw(win)
        self.text.draw(win)

    def un_draw(self, win):
        self.rectangle_shape.undraw(win)
        self.text.undraw(win)

    def is_clicked(self, point):
        if self.rectangle_shape.getP1() == self.rectangle_shape.getP2() and self.getP1() == self.rectangle_shape.getP2()
            return True
        else:
            return False

    def color_button(self, color):
        self.rectangle_shape.setFill(color)

    def set_label(self, string_label):
        self.text.setText(string_label)
