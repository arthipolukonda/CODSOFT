import tkinter as tk
from tkinter import messagebox


def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(screen.get()))
            screen.delete(0, tk.END)
            screen.insert(tk.END, result)
        except Exception as e:
            messagebox.showerror("Error", "Invalid Input")
            screen.delete(0, tk.END)
    elif text == "C":
        screen.delete(0, tk.END)
    else:
        screen.insert(tk.END, text)


root = tk.Tk()
root.title("Simple Calculator")


screen = tk.Entry(root, font="Helvetica 20 bold", bd=10, relief=tk.SUNKEN, justify='right')
screen.grid(row=0, column=0, columnspan=4, pady=10)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('C', 5, 0, 1, 4)
]


for (text, row, col, *span) in buttons:
    button = tk.Button(root, text=text, font="Helvetica 15", padx=10, pady=10)
    button.grid(row=row, column=col, columnspan=span[0] if span else 1, sticky='nsew')
    button.bind("<Button-1>", click)


for i in range(5):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)


root.mainloop()
