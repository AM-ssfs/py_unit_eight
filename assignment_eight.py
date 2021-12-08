# Aden Menschik
# last edit Dec. 8 2021
# basic calculator

import tkinter as tk
import math

root = tk.Tk()
root.title("Calculator")

equation = tk.StringVar()
equation.set("")

"""
functions
"""

# adds number to the end of the equation

def press_1():
    n = equation.get()
    n += "1"
    equation.set(n)
def press_2():
    n = equation.get()
    n += "2"
    equation.set(n)
def press_3():
    n = equation.get()
    n += "3"
    equation.set(n)
def press_4():
    n = equation.get()
    n += "4"
    equation.set(n)
def press_5():
    n = equation.get()
    n += "5"
    equation.set(n)
def press_6():
    n = equation.get()
    n += "6"
    equation.set(n)
def press_7():
    n = equation.get()
    n += "7"
    equation.set(n)
def press_8():
    n = equation.get()
    n += "8"
    equation.set(n)
def press_9():
    n = equation.get()
    n += "9"
    equation.set(n)
def press_0():
    n = equation.get()
    n += "0"
    equation.set(n)

# adds symbol to the end of the equation

def press_deci():
    n = equation.get()
    n += "."
    equation.set(n)
def press_add():
    n = equation.get()
    n += "+"
    equation.set(n)
def press_subtract():
    n = equation.get()
    n += "-"
    equation.set(n)
def press_multiply():
    n = equation.get()
    n += "*"
    equation.set(n)
def press_divide():
    n = equation.get()
    n += "/"
    equation.set(n)
def press_exponent():
    n = equation.get()
    n += "^"
    equation.set(n)
def press_sqrt():
    n = equation.get()
    n += "√"
    equation.set(n)

# deletes entire equation
# deletes last character

def press_clear():
    equation.set("")
def press_del():
    n = equation.get()
    n = n[:-1]
    equation.set(n)

# keeps the equation pretty when the user is entering the equation, run this when they click solve so they don't see

def press_solve():
    n = equation.get()

    if "^" in n:
        n = n.replace("^", "**")

    if "√" in n:
        n = n.replace("√", " math.sqrt(") + ")"

    print(n)

    if eval(n) == SyntaxError:  # or ZeroDivisionError or OverflowError or ValueError: # doesnt work :(
        equation.set("error")
    else:
        n = eval(n)
        equation.set(n)


def press_off():
    root.destroy()


"""
entry
"""

text_field = tk.Entry(root, textvariable=equation, width=40, borderwidth=3, font=("Arial", "40"))
text_field.grid(row=1, column=1)


"""
numbers 0-9
"""

frame1 = tk.Frame(root)

frame1.grid(row=2, column=1, columnspan=2)

button1 = tk.Button(frame1, text="1", command=press_1, width=10, font=("Arial", "40"))
button1.grid(row=2, column=1)
button2 = tk.Button(frame1, text="2", command=press_2, width=10, font=("Arial", "40"))
button2.grid(row=2, column=2)
button3 = tk.Button(frame1, text="3", command=press_3, width=10, font=("Arial", "40"))
button3.grid(row=2, column=3)

frame2 = tk.Frame(root)
frame2.grid(row=3, column=1, columnspan=2)

button4 = tk.Button(frame2, text="4", command=press_4, width=10, font=("Arial", "40"))
button4.grid(row=3, column=1)
button5 = tk.Button(frame2, text="5", command=press_5, width=10, font=("Arial", "40"))
button5.grid(row=3, column=2)
button6 = tk.Button(frame2, text="6", command=press_6, width=10, font=("Arial", "40"))
button6.grid(row=3, column=3)

frame3 = tk.Frame(root)
frame3.grid(row=4, column=1, columnspan=2)

button7= tk.Button(frame3, text="7", command=press_7, width=10, font=("Arial", "40"))
button7.grid(row=4, column=1)
button8= tk.Button(frame3, text="8", command=press_8, width=10, font=("Arial", "40"))
button8.grid(row=4, column=2)
button9= tk.Button(frame3, text="9", command=press_9, width=10, font=("Arial", "40"))
button9.grid(row=4, column=3)

frame4 = tk.Frame(root)
frame4.grid(row=5, column=1, columnspan=2)

button0 = tk.Button(frame4, text="0", command=press_0, width=10, font=("Arial", "40"))
button0.grid(row=5, column=1)

"""
operators
"""

deci = tk.Button(frame4, text=".", command=press_deci, width=10, font=("Arial", "40"))
deci.grid(row=5, column=2)
solve = tk.Button(frame4, text="=", command=press_solve, width=10, font=("Arial", "40"))
solve.grid(row=5, column=3)


add = tk.Button(frame1, text="+", command=press_add, width=10, font=("Arial", "40"))
add.grid(row=2, column=4)
subtract = tk.Button(frame2, text="-", command=press_subtract, width=10, font=("Arial", "40"))
subtract.grid(row=3, column=4)
multiply = tk.Button(frame3, text="x", command=press_multiply, width=10, font=("Arial", "40"))
multiply.grid(row=4, column=4)
divide = tk.Button(frame4, text="/", command=press_divide, width=10, font=("Arial", "40"))
divide.grid(row=5, column=4)


sqrt = tk.Button(root, text="√", command=press_sqrt, width=10, font=("Arial", "40"))
sqrt.grid(row=2, column=3)
exp = tk.Button(root, text="^", command=press_exponent, width=10, font=("Arial", "40"))
exp.grid(row=3, column=3)
delete = tk.Button(root, text="Del", command=press_del, width=10, font=("Arial", "40"))
delete.grid(row=4, column=3)
clear = tk.Button(root, text="Clear", command=press_clear, width=10, font=("Arial", "40"))
clear.grid(row=5, column=3)


off = tk.Button(root, text="Off", command=press_off, width=3, font=("Arial", "30"))
off.grid(row=1, column=3)


tk.mainloop()


#   entryyyyyyyyyyyy  off
#   1   2   3     +   sqrt
#   4   5   6     -   ^
#   7   8   9     x   del
#   0   .   =     /   clear



