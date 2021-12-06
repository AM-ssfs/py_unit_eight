import tkinter
import tkinter as tk
import math

root = tk.Tk()
root.title("calculator")

"""
vars
"""

equation = tkinter.StringVar()
equation.set("")

"""
functions
"""


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

def press_clear():
    equation.set("")

def press_solve():
    n = equation.get()

    if "^" in n:
        n = n.replace("^", "**")

    if "√" in n:
        n = n.replace("√", "math.sqrt(") + ")"
        # print(n)
        n = compile(n, "<string>", "eval")

    print(n)
    n = eval(n)
    equation.set(n)


"""
entry
"""

text_field = tk.Entry(root, textvariable=equation)
text_field.grid(row=1, column=1)


"""
numbers 0-9
"""

frame1 = tk.Frame(root)
frame1.grid(row=2, column=1, columnspan=2, pady=10)

button1 = tk.Button(frame1, text="1", command=press_1)
button1.grid(row=2, column=1)
button2 = tk.Button(frame1, text="2", command=press_2)
button2.grid(row=2, column=2)
button3 = tk.Button(frame1, text="3", command=press_3)
button3.grid(row=2, column=3)

frame2 = tk.Frame(root)
frame2.grid(row=3, column=1, columnspan=2, pady=10)

button4 = tk.Button(frame2, text="4", command=press_4)
button4.grid(row=3, column=1)
button5 = tk.Button(frame2, text="5", command=press_5)
button5.grid(row=3, column=2)
button6 = tk.Button(frame2, text="6", command=press_6)
button6.grid(row=3, column=3)

frame3 = tk.Frame(root)
frame3.grid(row=4, column=1, columnspan=2, pady=10)

button7= tk.Button(frame3, text="7", command=press_7)
button7.grid(row=4, column=1)
button8= tk.Button(frame3, text="8", command=press_8)
button8.grid(row=4, column=2)
button9= tk.Button(frame3, text="9", command=press_9)
button9.grid(row=4, column=3)

frame4 = tk.Frame(root)
frame4.grid(row=5, column=1, columnspan=2, pady=10)

button0 = tk.Button(frame4, text="0", command=press_0)
button0.grid(row=5, column=2)

"""
operators
"""

clear = tk.Button(root, text="Clear", command=press_clear)
clear.grid(row=1, column=2)

add = tk.Button(root, text="+", command=press_add)
add.grid(row=1, column=3)
subtract = tk.Button(root, text="-", command=press_subtract)
subtract.grid(row=2, column=4)
multiply = tk.Button(root, text="x", command=press_multiply)
multiply.grid(row=3, column=4)
divide = tk.Button(root, text="/", command=press_divide)
divide.grid(row=4, column=4)

exponent = tk.Button(frame4, text="^", command=press_exponent)
exponent.grid(row=5, column=1)

sqrt = tk.Button(frame4, text="√", command=press_sqrt)
sqrt.grid(row=5, column=3)

solve = tk.Button(root, text="=", command=press_solve)
solve.grid(row=5, column=4)






tk.mainloop()


#   entry clear   +
#   1   2   3     -
#   4   5   6     x
#   7   8   9     /
#   ^   0   !     =



