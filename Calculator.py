import math
import re
from tkinter import*

root = Tk()
root.title("Калькулятор")
root.geometry("543x410")
icon = PhotoImage(file = "icon.png")
root.iconphoto(False, icon)

entry = Entry(root, font = "Arial 24", width = 30)
entry.grid(row = 0, column = 0, columnspan = 5, ipady=15)

def click(value):
    if value == "=":
        expr = entry.get()
        entry.delete(0, END)
        entry.insert(0, calculate(expr))
    elif value == "C":
        entry.delete(0, END)
    elif value == "⌫":
        entry.delete(len(entry.get()) - 1, END)
    else:
        entry.insert(END, value)


def calculate(expr):
    try:
        expr = expr.replace("sin(", "math.sin(")
        expr = expr.replace("cos(", "math.cos(")
        expr = expr.replace("tan(", "math.tan(")
        expr = expr.replace("√(", "math.sqrt(")
        expr = expr.replace("log(", "math.log10(")
        expr = expr.replace("ln(", "math.log(")
        expr = expr.replace("π", "math.pi")
        expr = expr.replace("e", "math.e")
        expr = expr.replace("^", "**")

        expr = re.sub(r"(\d+)!", r"math.factorial(\1)", expr)
        expr = re.sub(r"\(([^()]+)\)!", r"math.factorial(\1)", expr)

        answer = eval(expr)

        if isinstance(answer, float):
            if abs(answer) < 1e-12:
                answer = 0.0
            elif abs(answer - round(answer)) < 1e-12:
                answer = round(answer)
            else:
                answer = round(answer, 10)

        return str(answer)

    except:
        return "Ошибка!"


buttons = [("π", 1, 0, "#d9c5f0"), ("e", 1, 1, "#d9c5f0"), ("sin(", 1, 2, "#d9c5f0"), ("cos(", 1, 3, "#d9c5f0"), ("tan(", 1, 4, "#d9c5f0"),
           ("ln(", 2, 0, "#d9c5f0"), ("log(", 2, 1, "#d9c5f0"), ("√(", 2, 2, "#d9c5f0"), ("^", 2, 3, "#d9c5f0"), ("!", 2, 4, "#d9c5f0"),
           ("7", 3, 0, "#f0e5ff"), ("8", 3, 1, "#f0e5ff"), ("9", 3, 2, "#f0e5ff"), ("/", 3, 3, "#e7cbfb"), ("(", 3, 4, "#e8d9ff"),
           ("4", 4, 0, "#f0e5ff"), ("5", 4, 1, "#f0e5ff"), ("6", 4, 2, "#f0e5ff"), ("*", 4, 3, "#e7cbfb"), (")", 4, 4, "#e8d9ff"),
           ("1", 5, 0, "#f0e5ff"), ("2", 5, 1, "#f0e5ff"), ("3", 5, 2, "#f0e5ff"), ("-", 5, 3, "#e7cbfb"), ("C", 5, 4, "#ffe5e5"),
           ("0", 6, 0, "#f0e5ff"), (".", 6, 1, "#f0e5ff"), ("=", 6, 2, "#dfb3ff"), ("+", 6, 3, "#e7cbfb"), ("⌫", 6, 4, "#e7cbfb"),]

for i in buttons:
    btn = Button(root, text = i[0], font="Arial 20", width = 6, bg = i[3], command = lambda value = i[0]: click(value))
    btn.grid(row = i[1], column = i[2])


mainloop()