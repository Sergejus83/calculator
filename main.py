import tkinter as tk

window = tk.Tk()
window.geometry("500x350")
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

window.mainloop()