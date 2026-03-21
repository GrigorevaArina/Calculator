import math
import re
from tkinter import*
"""
Калькулятор с графическим интерфейсом.

Модуль реализует инженерный калькулятор с поддержкой:
- арифметических операций (+, -, *, /)
- тригонометрических функций (sin, cos, tan)
- логарифмов (log, ln)
- факториала (!)
- констант π и e
- степени (^)
- скобок

Запуск:
    python Calculator.py
"""

root = Tk()
root.title("Калькулятор")
root.geometry("530x410")
icon = PhotoImage(file="icon.png")
root.iconphoto(False, icon)

entry = Entry(root, font="Arial 20", width=35)
entry.grid(row=0, column=0, columnspan=5, sticky="nsew", ipady=20)

def click(value):
    """
    Обрабатывает нажатие кнопки калькулятора.
    Аргументы: value (str): Текст нажатой кнопки
    Действия:
        "=" - вычисляет выражение и выводит резульат
        "C" - очищает поле ввода
        "⌫" - удаляет последний символ
        иначе - добавляет символ в поле ввода
    """
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
    """
    Вычисляет математическое выражение.
    Аргументы: expr (str): Строка с выражением
    Возвращает: str: Результат вычисления или сообщение об ошибке
    """
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
            if abs(answer) > 1e15:
                return "Ошибка: слишком большое значение"
            if abs(answer) < 1e-12:
                answer = 0.0
            elif abs(answer - round(answer)) < 1e-12:
                answer = round(answer)
            else:
                answer = round(answer, 10)

        return str(answer)

    except:
        return "Ошибка!"


buttons = [("π", "#d9c5f0"), ("e", "#d9c5f0"), ("sin(", "#d9c5f0"), ("cos(", "#d9c5f0"), ("tan(", "#d9c5f0"),
           ("ln(", "#d9c5f0"), ("log(", "#d9c5f0"), ("√(", "#d9c5f0"), ("^", "#d9c5f0"), ("!", "#d9c5f0"),
           ("7", "#f0e5ff"), ("8", "#f0e5ff"), ("9", "#f0e5ff"), ("/", "#e7cbfb"), ("(", "#e8d9ff"),
           ("4", "#f0e5ff"), ("5", "#f0e5ff"), ("6", "#f0e5ff"), ("*", "#e7cbfb"), (")", "#e8d9ff"),
           ("1", "#f0e5ff"), ("2", "#f0e5ff"), ("3", "#f0e5ff"), ("-", "#e7cbfb"), ("C", "#ffe5e5"),
           ("0", "#f0e5ff"), (".", "#f0e5ff"), ("=", "#dfb3ff"), ("+", "#e7cbfb"), ("⌫", "#e7cbfb"),]

for i in range(len(buttons)):
    btn = Button(root, text=buttons[i][0], font="Arial 20", width=6, bg=buttons[i][1], command=lambda value=buttons[i][0]: click(value))
    btn.grid(row=i // 5 + 1, column=i % 5)


mainloop()
