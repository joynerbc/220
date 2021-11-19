"""
Name: Brianna Joyner
three_door_game.py

Problem: This program creates a three door game

Certification of Authenticity:
I certify that this assignment is entirely my own work, with help from the CSL.
"""

from button import Button
from random import randint
from graphics import *

def main():
    win = GraphWin("Three Button Game", 500, 500)
    rectangle_one = Rectangle(Point(100, 290), Point(140, 310))
    rectangle_two = Rectangle(Point(150, 290), Point(190, 310))
    rectangle_three = Rectangle(Point(200, 290), Point(240, 310))
    button_one = Button(rectangle_one, "Door One")
    button_two = Button(rectangle_two, "Door Two")
    button_three = Button(rectangle_three, "Door Three")
    button_one.draw(win)
    button_two.draw(win)
    button_three.draw(win)
    message = Text(Point(220, 30), "I have a secret door")
    message.draw(win)
    message_two = Text(Point(220, 320), "Click to choose my door")
    message_two.draw(win)
    list_buttons = [button_one, button_two, button_three]
    answer = list_buttons[randint(0, 2)]
    click = win.getMouse()
    for button in list_buttons:
        if button.is_clicked(click):
            if answer == button:
                message.setText("you win!")
                button.color_button("green")
                message_two.setText("click to close")
            else:
                message.setText("you lost!")
                button.color_button("red")
                message_two.setText(answer.get_label() + "is my secret door")

    win.getMouse()
    win.close()

if __name__ == '__main__':
    main()