import tkinter as tk

def on_text_changed(*args):
    print("Updated value:", my_var.get())

root = tk.Tk()
root.title("Control Variables Example")

my_var = tk.StringVar()

entry = tk.Entry(root, textvariable=my_var)
entry.pack()

my_var.trace("w", on_text_changed)  # Triggers on_text_changed when the variable changes

root.mainloop()
