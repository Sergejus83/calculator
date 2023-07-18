import tkinter as tk

window = tk.Tk()
window.geometry("505x445")
text_result = tk.Text(window, height=2, width=18, font=("Cascadia Code SemiLight", 35))
text_result.grid(columnspan=5)

calculation = ""

def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

def evaluate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clear_field()
        text_result.insert(1.0, "error")

def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")


button_1 = tk.Button(window, text="1", command=lambda: add_to_calculation(1), width=7, font=("Cascadia Code SemiLight", 20))
button_1.grid(row=2, column=0)
button_2 = tk.Button(window, text="2", command=lambda: add_to_calculation(2), width=7, font=("Cascadia Code SemiLight", 20))
button_2.grid(row=2, column=1)
button_3 = tk.Button(window, text="3", command=lambda: add_to_calculation(3), width=7, font=("Cascadia Code SemiLight", 20))
button_3.grid(row=2, column=2)
button_4 = tk.Button(window, text="4", command=lambda: add_to_calculation(4), width=7, font=("Cascadia Code SemiLight", 20))
button_4.grid(row=3, column=0)
button_5 = tk.Button(window, text="5", command=lambda: add_to_calculation(5), width=7, font=("Cascadia Code SemiLight", 20))
button_5.grid(row=3, column=1)
button_6 = tk.Button(window, text="6", command=lambda: add_to_calculation(6), width=7, font=("Cascadia Code SemiLight", 20))
button_6.grid(row=3, column=2)
button_7 = tk.Button(window, text="7", command=lambda: add_to_calculation(7), width=7, font=("Cascadia Code SemiLight", 20))
button_7.grid(row=4, column=0)
button_8 = tk.Button(window, text="8", command=lambda: add_to_calculation(8), width=7, font=("Cascadia Code SemiLight", 20))
button_8.grid(row=4, column=1)
button_9 = tk.Button(window, text="9", command=lambda: add_to_calculation(9), width=7, font=("Cascadia Code SemiLight", 20))
button_9.grid(row=4, column=2)
button_0 = tk.Button(window, text="0", command=lambda: add_to_calculation(0), width=7, font=("Cascadia Code SemiLight", 20))
button_0.grid(row=5, column=1)
button_plus = tk.Button(window, text="+", command=lambda: add_to_calculation("+"), width=7, font=("Cascadia Code SemiLight", 20))
button_plus.grid(row=2, column=3)
button_minus = tk.Button(window, text="-", command=lambda: add_to_calculation("-"), width=7, font=("Cascadia Code SemiLight", 20))
button_minus.grid(row=3, column=3)
button_multiply = tk.Button(window, text="*", command=lambda: add_to_calculation("*"), width=7, font=("Cascadia Code SemiLight", 20))
button_multiply.grid(row=4, column=3)
button_divide = tk.Button(window, text="/", command=lambda: add_to_calculation("/"), width=7, font=("Cascadia Code SemiLight", 20))
button_divide.grid(row=5, column=3)
button_open_bracket = tk.Button(window, text="(", command=lambda: add_to_calculation("("), width=7, font=("Cascadia Code SemiLight", 20))
button_open_bracket.grid(row=5, column=0)
button_close_bracket = tk.Button(window, text=")", command=lambda: add_to_calculation(")"), width=7, font=("Cascadia Code SemiLight", 20))
button_close_bracket.grid(row=5, column=2)
button_equals = tk.Button(window, text="=", command=evaluate_calculation, width=14, font=("Cascadia Code SemiLight", 22))
button_equals.grid(row=6, column=2, columnspan=2)
button_clear = tk.Button(window, text="C", command=clear_field, width=14, font=("Cascadia Code SemiLight", 22))
button_clear.grid(row=6, column=0, columnspan=2)

window.mainloop()