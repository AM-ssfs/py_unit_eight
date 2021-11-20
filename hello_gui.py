import tkinter as tk
root = tk.Tk()
root.title("Hello")
text = tk.Label(root, text="Hello, World")
text.grid(row=1, column=1)
tk.mainloop()