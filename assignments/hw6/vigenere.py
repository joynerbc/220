"""
Name: Brianna Joyner
vigenere.py

Problem:
This program will implement the vigenere cipher

Certification of Authenticity:
I certify that this assignment is entirely my own work. I talked with Angela and the CSL as well.
"""
from graphics import *

def user_button(win, button):
   user_button_click = win.getMouse()
   x_coordinate = user_button_click.getX()
   y_coordinate = user_button_click.getY()

def input_from_user(input, second_input):
    encrypted_message = " "
    code = input.getText()
    key = second_input.getText()
    for i in range(len(code)):
        encrypt = str(chr(ord(code[0] + ord(key[0]) % 26)))
        encrypted_message += encrypt

def main():
    win_width = 800
    win_height = 800
    win = GraphWin("Vigenere", win_width, win_height)
    win.setBackground("white")
    upper_message = Text(Point(160, 200), "Message to Encode: ")
    upper_message.draw(win)
    lower_message = Text(Point(160, 320), "Enter the Keyword: ")
    lower_message.draw(win)
    user_input = Entry(Point(440, 200), 40)
    user_input.draw(win)
    second_input = user_input.clone()
    second_input.move(0, 180)
    second_input.draw(win)
    encoder = Text(Point(400, 450), "Encode!")
    encoder_center = encoder.getAnchor()
    encoder.draw(win)
    x_c_cent = encoder_center.getX()
    y_c_cent = encoder_center.getY()
    first_rectangle = Rectangle(Point(x_c_cent - 30, y_c_cent + 20), Point(x_c_cent + 30, y_c_cent - 20))
    first_rectangle.draw(win)
    user_button(win, first_rectangle)
    function_output = input_from_user(user_input, second_input)
    first_rectangle.undraw(win)
    encoder.setText("Resulting Message" + function_output)
    close_message = Text(Point(250, 490), "Click Anywhere To Close Window")
    close_message.draw(win)
    win.getMouse()
    win.close()

if __name__ == '__main__':
    main()
