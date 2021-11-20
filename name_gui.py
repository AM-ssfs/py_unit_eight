import tkinter as tk

root = tk.Tk()
root.title("Name")

def hi():
    return "Hello, " + name.get()

name = tk.StringVar()

user_input = tk.Entry(root, textvariable=name)
user_input.grid(row=1, column=1)

hello = tk.Label(root, text="hello " + name.get())
hello.grid(row=2, column=1)

say_hello = tk.Button(root, text="say hello", command=hi)
say_hello.grid(row=3, column=1)
tk.mainloop()