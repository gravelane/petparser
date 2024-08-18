import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")

        self.expression = ""
        self.input_text = tk.StringVar()

        # Создание поля ввода
        input_frame = tk.Frame(self.root, bd=10, relief=tk.RIDGE)
        input_frame.pack(side=tk.TOP)

        input_field = tk.Entry(input_frame, font=('arial', 18, 'bold'), textvariable=self.input_text, width=50, bd=10, insertwidth=4, bg="powder blue", justify='right')
        input_field.grid(row=0, column=0)
        input_field.pack(ipady=10)

        # Создание кнопок
        buttons_frame = tk.Frame(self.root, bd=10, relief=tk.RIDGE)
        buttons_frame.pack()

        # Первая строка кнопок
        button_clear = tk.Button(buttons_frame, text="C", fg="black", width=32, height=3, bd=0, bg="#eee", cursor="hand2", command=self.clear_input)
        button_clear.grid(row=0, column=0, columnspan=3)
        button_divide = tk.Button(buttons_frame, text="/", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: self.button_click("/"))
        button_divide.grid(row=0, column=3)

        # Вторая строка кнопок
        button_7 = tk.Button(buttons_frame, text="7", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: self.button_click("7"))
        button_7.grid(row=1, column=0)
        button_8 = tk.Button(buttons_frame, text="8", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: self.button_click("8"))
        button_8.grid(row=1, column=1)
        button_9 = tk.Button(buttons_frame, text="9", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: self.button_click("9"))
        button_9.grid(row=1, column=2)
        button_multiply = tk.Button(buttons_frame, text="*", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: self.button_click("*"))
        button_multiply.grid(row=1, column=3)

        # Третья строка кнопок
        button_4 = tk.Button(buttons_frame, text="4", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: self.button_click("4"))
        button_4.grid(row=2, column=0)
        button_5 = tk.Button(buttons_frame, text="5", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: self.button_click("5"))
        button_5.grid(row=2, column=1)
        button_6 = tk.Button(buttons_frame, text="6", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: self.button_click("6"))
        button_6.grid(row=2, column=2)
        button_subtract = tk.Button(buttons_frame, text="-", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: self.button_click("-"))
        button_subtract.grid(row=2, column=3)

        # Четвертая строка кнопок
        button_1 = tk.Button(buttons_frame, text="1", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: self.button_click("1"))
        button_1.grid(row=3, column=0)
        button_2 = tk.Button(buttons_frame, text="2", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: self.button_click("2"))
        button_2.grid(row=3, column=1)
        button_3 = tk.Button(buttons_frame, text="3", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: self.button_click("3"))
        button_3.grid(row=3, column=2)
        button_add = tk.Button(buttons_frame, text="+", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: self.button_click("+"))
        button_add.grid(row=3, column=3)

        # Пятая строка кнопок
        button_0 = tk.Button(buttons_frame, text="0", fg="black", width=21, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: self.button_click("0"))
        button_0.grid(row=4, column=0, columnspan=2)
        button_dot = tk.Button(buttons_frame, text=".", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: self.button_click("."))
        button_dot.grid(row=4, column=2)
        button_equals = tk.Button(buttons_frame, text="=", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=self.evaluate_expression)
        button_equals.grid(row=4, column=3)

    def button_click(self, item):
        self.expression += str(item)
        self.input_text.set(self.expression)

    def clear_input(self):
        self.expression = ""
        self.input_text.set("")

    def evaluate_expression(self):
        try:
            result = str(eval(self.expression))
            self.input_text.set(result)
            self.expression = ""
        except Exception as e:
            self.input_text.set("Ошибка")
            self.expression = ""
            messagebox.showerror("Ошибка", f"Неправильное выражение\n{e}")

if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
