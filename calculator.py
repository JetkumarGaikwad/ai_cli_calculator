import tkinter as tk
from math import sin, cos, tan, asin, acos, atan, log10, log, sqrt, factorial, e, pi, pow

class ScientificCalculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Advanced Scientific Calculator")
        self.geometry("480x600")
        self.resizable(False, False)
        self.config(bg="lightgray")

        self.shift = False  # shift toggle for secondary functions
        self.memory = 0
        self.expression = ""

        self.create_widgets()

    def create_widgets(self):
        self.entry = tk.Entry(self, font=("Arial", 20), bd=5, relief=tk.RIDGE, justify="right")
        self.entry.grid(row=0, column=0, columnspan=6, ipady=15, pady=10, padx=10, sticky="we")

        btn_text = [
            ["Shift", "(", ")", "MC", "MR", "M+"],
            ["sin", "cos", "tan", "ln", "log", "√"],
            ["sin⁻¹", "cos⁻¹", "tan⁻¹", "e^x", "10^x", "x²"],
            ["7", "8", "9", "÷", "xʸ", "x³"],
            ["4", "5", "6", "×", "y√x", "n!"],
            ["1", "2", "3", "-", "π", "e"],
            ["0", ".", "+/-", "+", "%", "1/x"],
            ["C", "CE", "←", "Ans", "=", ""]
        ]

        self.buttons = {}

        for r, row in enumerate(btn_text, start=1):
            for c, text in enumerate(row):
                if text == "":
                    continue
                action = lambda x=text: self.on_button_click(x)
                btn = tk.Button(self, text=text, width=6, height=2, font=("Arial", 14),
                                command=action, bg="white", fg="black")
                btn.grid(row=r, column=c, padx=2, pady=2)
                self.buttons[text] = btn

    def on_button_click(self, char):
        if char == "Shift":
            self.shift = not self.shift
            self.update_shift_state()
        elif char == "C":
            self.expression = ""
            self.update_entry()
        elif char == "CE":
            self.expression = ""
            self.update_entry()
        elif char == "←":
            self.expression = self.expression[:-1]
            self.update_entry()
        elif char == "=":
            self.calculate_result()
        elif char == "+/-":
            self.toggle_sign()
        elif char == "Ans":
            self.expression += str(self.last_answer)
            self.update_entry()
        elif char == "MC":
            self.memory = 0
        elif char == "MR":
            self.expression += str(self.memory)
            self.update_entry()
        elif char == "M+":
            try:
                val = eval(self.expression.replace("÷", "/").replace("×", "*"))
                self.memory += val
            except:
                pass
        else:
            self.expression += char
            self.update_entry()

    def update_shift_state(self):
        if self.shift:
            # Update buttons to show shift functions
            self.buttons["sin"].config(text="sin⁻¹")
            self.buttons["cos"].config(text="cos⁻¹")
            self.buttons["tan"].config(text="tan⁻¹")
            self.buttons["ln"].config(text="e^x")
            self.buttons["log"].config(text="10^x")
            self.buttons["√"].config(text="x³")
            self.buttons["x²"].config(text="x³")
            # more shift mappings can be added here
        else:
            # revert to normal
            self.buttons["sin"].config(text="sin")
            self.buttons["cos"].config(text="cos")
            self.buttons["tan"].config(text="tan")
            self.buttons["ln"].config(text="ln")
            self.buttons["log"].config(text="log")
            self.buttons["√"].config(text="√")
            self.buttons["x²"].config(text="x²")

    def toggle_sign(self):
        try:
            if self.expression.startswith("-"):
                self.expression = self.expression[1:]
            else:
                self.expression = "-" + self.expression
            self.update_entry()
        except:
            pass

    def update_entry(self):
        self.entry.delete(0, tk.END)
        self.entry.insert(0, self.expression)

    def calculate_result(self):
        try:
            expr = self.expression
            expr = expr.replace("÷", "/").replace("×", "*").replace("^", "**").replace("π", str(pi)).replace("e", str(e))

            # Replace functions for eval
            expr = expr.replace("sin⁻¹", "asin").replace("cos⁻¹", "acos").replace("tan⁻¹", "atan")
            expr = expr.replace("sin", "sin").replace("cos", "cos").replace("tan", "tan")
            expr = expr.replace("ln", "log").replace("log", "log10")
            expr = expr.replace("√", "sqrt")
            expr = expr.replace("n!", "factorial")

            # Custom parse for factorial (since factorial is not recognized by eval)
            if "!" in expr:
                expr = self.handle_factorial(expr)

            result = eval(expr, {"sin": sin, "cos": cos, "tan": tan,
                                 "asin": asin, "acos": acos, "atan": atan,
                                 "log": log, "log10": log10, "sqrt": sqrt,
                                 "factorial": factorial, "pi": pi, "e": e,
                                 "pow": pow})
            self.last_answer = result
            self.expression = str(result)
            self.update_entry()
        except Exception as e:
            self.expression = ""
            self.update_entry()
            self.entry.insert(0, "Error")

    def handle_factorial(self, expr):
        import re
        # Replace n! with factorial(n)
        def repl(match):
            num = match.group(1)
            return f"factorial({num})"
        expr = re.sub(r'(\d+)!', repl, expr)
        return expr


if __name__ == "__main__":
    app = ScientificCalculator()
    app.last_answer = 0
    app.mainloop()
