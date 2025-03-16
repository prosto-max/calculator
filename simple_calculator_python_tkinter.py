import tkinter as tk
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Калькулятор")
        self.result_var = tk.StringVar()
        self.result_var.set("0")
        self.create_widgets()

    def create_widgets(self):
        result_entry = tk.Entry(self.root, textvariable=self.result_var, font=("Arial", 20), bd=10, relief="sunken", justify="right")
        result_entry.grid(row=0, column=0, columnspan=4)
        buttons = [
            ('%', 1, 0), ('√', 1, 1), ('x²', 1, 2), ('1/x', 1, 3),
            ('CE', 2, 0), ('C', 2, 1), ('←', 2, 2), ('÷', 2, 3),
            ('7', 3, 0), ('8', 3, 1), ('9', 3, 2), ('×', 3, 3),
            ('4', 4, 0), ('5', 4, 1), ('6', 4, 2), ('-', 4, 3),
            ('1', 5, 0), ('2', 5, 1), ('3', 5, 2), ('+', 5, 3),
            ('±', 6, 0), ('0', 6, 1), (',', 6, 2), ('=', 6, 3)
        ]

        for (text, row, col) in buttons:
            button = tk.Button(self.root, text=text, font=("Arial", 18), height=2, width=5,
                               command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, padx=0, pady=0)

    def on_button_click(self, button):
        current_text = self.result_var.get()
        if button == "C" or button == "CE":
            self.result_var.set("0")
        elif button == "←" and current_text != "Ошибка":
            self.result_var.set(current_text[:-1] if len(current_text) > 1 else "0")
        elif button == "=" and current_text != "Ошибка":
            try:
                self.result_var.set(str(self.calculate_result(current_text)).replace(".", ","))
            except Exception:
                self.result_var.set("Ошибка")
        elif button == "√" and current_text != "Ошибка":
            self.result_var.set("√" + "(" + current_text + ")")
        elif button == "1/x" and current_text != "Ошибка":
            self.result_var.set("1÷" + "(" + current_text + ")")
        elif button == "x²" and current_text != "Ошибка":
            self.result_var.set("(" + current_text + ")" + "²")
        elif button == "±" and current_text != "Ошибка":
            self.result_var.set("-" + "(" + current_text + ")")
        elif button == "%" and current_text != "Ошибка":
            self.result_var.set(current_text + "%")
        elif button == "," and current_text != "Ошибка":
            self.result_var.set(current_text + ",")
        elif button == "÷" and current_text != "Ошибка":
            self.result_var.set(current_text + "÷")
        else:
            if current_text != "Ошибка":
                if current_text == "0":
                    self.result_var.set(button)
                else:
                    self.result_var.set(current_text + button)

    def calculate_result(self, expression):
        expression = expression.replace(',', '.').replace('×', '*').replace('÷', '/').replace("²", "**2").replace("√", "math.sqrt")
        answer = eval(expression)
        if answer != "Ошибка":
            if int(answer) == answer:
                answer = int(answer)
        return answer

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
