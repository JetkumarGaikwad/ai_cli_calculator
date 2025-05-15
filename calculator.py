import tkinter as tk
import math

class ScientificCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Scientific Calculator")
        self.root.geometry("420x600")
        self.expression = ""

        self.input_text = tk.StringVar()

        self.create_display()
        self.create_buttons()

    def create_display(self):
        input_frame = tk.Frame(self.root, bd=0, relief=tk.RIDGE)
        input_frame.pack(side=tk.TOP)

        input_field = tk.Entry(
            input_frame, font=('arial', 20, 'bold'),
            textvariable=self.input_text, width=30, bg="#eee", bd=10, justify=tk.RIGHT
        )
        input_field.grid(row=0, column=0)
        input_field.pack(ipady=10)

    def create_buttons(self):
        btns_frame = tk.Frame(self.root)
        btns_frame.pack()

        buttons = [
            ['C', 'DEL', 'π', 'e'],
            ['sin', 'cos', 'tan', '√'],
            ['x²', 'xʸ', '1/x', 'log'],
            ['7', '8', '9', '÷'],
            ['4', '5', '6', '×'],
            ['1', '2', '3', '-'],
            ['0', '.', '=', '+']
        ]

        for row in buttons:
            row_frame = tk.Frame(btns_frame)
            row_frame.pack(expand=True, fill='both')
            for btn_text in row:
                button = tk.Button(
                    row_frame, text=btn_text, font=('arial', 18),
                    fg="black", height=2, width=9,
                    command=lambda b=btn_text: self.on_button_click(b)
                )
                button.pack(side=tk.LEFT, expand=True, fill='both')

    def on_button_click(self, char):
        if char == 'C':
            self.expression = ""
        elif char == 'DEL':
            self.expression = self.expression[:-1]
        elif char == '=':
            try:
                self.expression = str(self.safe_eval(self.expression))
            except Exception:
                self.expression = "Error"
        elif char == 'π':
            self.expression += str(math.pi)
        elif char == 'e':
            self.expression += str(math.e)
        elif char == 'sin':
            self.expression += "math.sin("
        elif char == 'cos':
            self.expression += "math.cos("
        elif char == 'tan':
            self.expression += "math.tan("
        elif char == 'log':
            self.expression += "math.log10("
        elif char == '√':
            self.expression += "math.sqrt("
        elif char == 'x²':
            self.expression += "**2"
        elif char == 'xʸ':
            self.expression += "**"
        elif char == '1/x':
            self.expression = f"1/({self.expression})"
        elif char == '÷':
            self.expression += "/"
        elif char == '×':
            self.expression += "*"
        else:
            self.expression += str(char)

        self.input_text.set(self.expression)

    def safe_eval(self, expr):
        allowed_names = {k: v for k, v in math.__dict__.items() if not k.startswith("__")}
        return eval(expr, {"__builtins__": {}}, allowed_names)

if __name__ == "__main__":
    root = tk.Tk()
    calc = ScientificCalculator(root)
    root.mainloop()
