# Program for a Basic Calculator with a GUI 
# 
# 
#################################################


### Importing necessary libraries

import tkinter as tk
from tkinter import ttk, Frame, Button, StringVar


### Calculator functions

# Pressing a button
def symbolpress(symbol):
    global text_line
    text_line += str(symbol)
    equation_variable.set(text_line) 

# Pressing the equals sign
def equalsign():
    global text_line
    try:
        calculation = str(eval(text_line))
    except ArithmeticError:
        equation_variable.set("Incorrect arithmetic usage")
        text_line = ""
    except SyntaxError:
        equation_variable.set("Incorrect syntax usage")
        text_line = ""
    else:
        equation_variable.set(calculation)
        text_line = calculation

# Clearing the current inputs
def clearbar():
    global text_line
    equation_variable.set("")
    text_line = ""


### Creating the window

window = tk.Tk()

# Size of window
window.geometry("450x500")

# Title of the window's app
window.title("Basic Calculator")

# Title of the GUI
title = tk.Label(window, text = "Calculator", width = 100, height = 1, font = ("Roboto", 15))
title.pack(pady = 10)

# Variables 
text_line = ""
equation_variable = StringVar()  # shows symbols on the textbox, while text_line holds the chars

# Textbox to enter the symbols in
text_box = tk.Label(window, font = ("Roboto", 20), textvariable = equation_variable, \
        bg = "White", width = 22, height = 2)
text_box.pack(pady = 1)


### Creating the buttons for the symbols

# Creating the frame to store the buttons
container = Frame(window)
container.pack()

# Buttons
bPlus = Button(container, text = "+", command = lambda: symbolpress("+"), \
        font = ("Roboto", 18), height = 2, width = 5, bg = "#9bddff")
bPlus.grid(row = 3, column = 2)

bMinus = Button(container, text = "-", command = lambda: symbolpress("-"), \
        font = ("Roboto", 18), height = 2, width = 5, bg = "#9bddff")
bMinus.grid(row = 3, column = 3)

bMultiply = Button(container, text = "*", command = lambda: symbolpress("*"), \
        font = ("Roboto", 18), height = 2, width = 5, bg = "#9bddff")
bMultiply.grid(row = 2, column = 3)

bDivide = Button(container, text = "/", command = lambda: symbolpress("/"), \
        font = ("Roboto", 18), height = 2, width = 5, bg = "#9bddff")
bDivide.grid(row = 1, column = 3)

bDecimal = Button(container, text = ".", command = lambda: symbolpress("."), \
        font = ("Roboto", 18), height = 2, width = 5)
bDecimal.grid(row = 3, column = 1)

bEqual = Button(container, text = "=", command = lambda: equalsign(), \
        font = ("Roboto", 18), height = 2, width = 5, bg = "#ff7f7f")
bEqual.grid(row = 4, column = 2)

bClear = Button(container, text = "C", command = lambda: clearbar(), \
        font = ("Roboto", 18, "italic"), height = 2, width = 5)
bClear.grid(row = 0, column = 3)

bLeftP = Button(container, text = "(", command = lambda: symbolpress("("), \
        font = ("Roboto", 18), height = 2, width = 5)
bLeftP.grid(row = 4, column = 0)

bRightP = Button(container, text = ")", command = lambda: symbolpress(")"), \
        font = ("Roboto", 18), height = 2, width = 5)
bRightP.grid(row = 4, column = 1)

b0 = Button(container, text = "0", command = lambda: symbolpress(0), \
        font = ("Roboto", 18), height = 2, width = 5)
b0.grid(row = 3, column = 0)

b1 = Button(container, text = "1", command = lambda: symbolpress(1), \
        font = ("Roboto", 18), height = 2, width = 5)
b1.grid(row = 2, column = 0)

b2 = Button(container, text = "2", command = lambda: symbolpress(2), \
        font = ("Roboto", 18), height = 2, width = 5)
b2.grid(row = 2, column = 1)

b3 = Button(container, text = "3", command = lambda: symbolpress(3), \
        font = ("Roboto", 18), height = 2, width = 5)
b3.grid(row = 2, column = 2)

b4 = Button(container, text = "4", command = lambda: symbolpress(4), \
        font = ("Roboto", 18), height = 2, width = 5)
b4.grid(row = 1, column = 0)

b5 = Button(container, text = "5", command = lambda: symbolpress(5), \
        font = ("Roboto", 18), height = 2, width = 5)
b5.grid(row = 1, column = 1)

b6 = Button(container, text = "6", command = lambda: symbolpress(6), \
        font = ("Roboto", 18), height = 2, width = 5)
b6.grid(row = 1, column = 2)

b7 = Button(container, text = "7", command = lambda: symbolpress(7), \
        font = ("Roboto", 18), height = 2, width = 5)
b7.grid(row = 0, column = 0)

b8 = Button(container, text = "8", command = lambda: symbolpress(8), \
        font = ("Roboto", 18), height = 2, width = 5)
b8.grid(row = 0, column = 1)

b9 = Button(container, text = "9", command = lambda: symbolpress(9), \
        font = ("Roboto", 18), height = 2, width = 5)
b9.grid(row = 0, column = 2)


### Running the window

window.mainloop()



### End of program