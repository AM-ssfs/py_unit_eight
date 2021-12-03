import tkinter as tk

root=tk.Tk()
root.title("calculator")

"""
vars
"""

equation = tk.StringVar

"""
functions
"""

def press_number():
    t=equation.get
    t+="7"
    text_field.set(t)

"""
entry
"""

text_field = tk.Entry(root, textVariable=equation)
text_field.grid(row=1, column=1)


"""
numbers 0-9
"""

frame1 = tk.Frame(root)
frame1.grid(row=2, column=1, columnspan=2, pady=10)

button1 = tk.Button(frame1, text="1")
button1.grid(row=2, column=1)
button2 = tk.Button(frame1, text="2")
button2.grid(row=2, column=2)
button3 = tk.Button(frame1, text="3")
button3.grid(row=2, column=3)

frame2 = tk.Frame(root)
frame2.grid(row=3, column=1, columnspan=2, pady=10)

button4 = tk.Button(frame2, text="4")
button4.grid(row=3, column=1)
button5 = tk.Button(frame2, text="5")
button5.grid(row=3, column=2)
button6 = tk.Button(frame2, text="6")
button6.grid(row=3, column=3)

frame3 = tk.Frame(root)
frame3.grid(row=4, column=1, columnspan=2, pady=10)

button7= tk.Button(frame3, text="7")
button7.grid(row=4, column=1)
button8= tk.Button(frame3, text="8")
button8.grid(row=4, column=2)
button9= tk.Button(frame3, text="9")
button9.grid(row=4, column=3)

frame4 = tk.Frame(root)
frame4.grid(row=5, column=1, columnspan=2, pady=10)

button0 = tk.Button(frame4, text="0")
button0.grid(row=5, column=2)

"""
functions
"""

clear = tk.Button(root, text="Clear")
clear.grid(row=1, column=2)

add = tk.Button(root, text="+")
add.grid(row=1, column=3)
subtract = tk.Button(root, text="-")
subtract.grid(row=2, column=4)
multiply = tk.Button(root, text="x")
multiply.grid(row=3, column=4)
divide = tk.Button(root, text="/")
divide.grid(row=4, column=4)

exponent = tk.Button(frame4, text="^")
exponent.grid(row=5, column=1)
sqrt = tk.Button(frame4, text="√")
sqrt.grid(row=5, column=3)

solve = tk.Button(root, text="=")
solve.grid(row=5, column=4)






tk.mainloop()


#   entry clear   +
#   1   2   3     -
#   4   5   6     x
#   7   8   9     /
#   ^   0  sqrt   =



