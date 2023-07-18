import tkinter as tk

window = tk.Tk()
window.geometry("500x350")
text_result = tk.Text(window, height=2, width=18, font=("Cascadia Code SemiLight", 35))
text_result.grid(columnspan=5)

calculation = ""

def add_to_calculation(symbol):
    pass

def evaluate_calculation():
    pass

def clear_field():
    pass

window.mainloop()