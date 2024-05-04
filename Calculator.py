import tkinter as i

cal = ""
def add_to_cal(sym):
    global cal
    cal += str(sym)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, cal)

def evaluate_cal():
    global cal
    print(cal)
    try:
        cal = str(eval(cal))
        text_result.delete(1.0, 'end')
        text_result.insert(1.0, cal)
    except ZeroDivisionError:
        clear_field()
        text_result.insert(1.0, 'Error')
def clear_field():
    global cal
    cal = ""
    text_result.delete(1.0, 'end')

def clear_field_last():
    global cal
    text_result.delete(1.0, 'end')

root = i.Tk()
root.geometry("300x381")

text_result = i.Text(root, height=2, width=16, font=('Arial', 24))
text_result.grid(columnspan=5)

btn1 = i.Button(root, text="1", command=lambda: add_to_cal(1), width=6, height=2, font=("Arial, 14"))
btn1.grid(row=2, column=1)
btn2 = i.Button(root, text="2", command=lambda: add_to_cal(2), width=6, height=2, font=("Arial, 14"))
btn2.grid(row=2, column=2)
btn3 = i.Button(root, text="3", command=lambda: add_to_cal(3), width=6, height=2, font=("Arial, 14"))
btn3.grid(row=2, column=3)
btn4 = i.Button(root, text="4", command=lambda: add_to_cal(4), width=6, height=2, font=("Arial, 14"))
btn4.grid(row=3, column=1)
btn5 = i.Button(root, text="5", command=lambda: add_to_cal(5), width=6, height=2, font=("Arial, 14"))
btn5.grid(row=3, column=2)
btn6 = i.Button(root, text="6", command=lambda: add_to_cal(6), width=6, height=2, font=("Arial, 14"))
btn6.grid(row=3, column=3)
btn7 = i.Button(root, text="7", command=lambda: add_to_cal(7), width=6, height=2, font=("Arial, 14"))
btn7.grid(row=4, column=1)
btn8 = i.Button(root, text="8", command=lambda: add_to_cal(8), width=6, height=2, font=("Arial, 14"))
btn8.grid(row=4, column=2)
btn9 = i.Button(root, text="9", command=lambda: add_to_cal(9), width=6, height=2, font=("Arial, 14"))
btn9.grid(row=4, column=3)
btn0 = i.Button(root, text="0", command=lambda: add_to_cal(0), width=6, height=2, font=("Arial, 14"))
btn0.grid(row=5, column=2)
btn_plus = i.Button(root, text="+", command=lambda: add_to_cal("+"), width=6, height=2, font=("Arial, 14"))
btn_plus.grid(row=2, column=4)
btn_minus = i.Button(root, text="-", command=lambda: add_to_cal("-"), width=6, height=2, font=("Arial, 14"))
btn_minus.grid(row=3, column=4)
btn_times = i.Button(root, text="*", command=lambda: add_to_cal("*"), width=6, height=2, font=("Arial, 14"))
btn_times.grid(row=4, column=4)
btn_plus = i.Button(root, text="/", command=lambda: add_to_cal("/"), width=6, height=2, font=("Arial, 14"))
btn_plus.grid(row=5, column=4)
btn_bracket_right = i.Button(root, text=")", command=lambda: add_to_cal(")"), width=6, height=2, font=("Arial, 14"))
btn_bracket_right.grid(row=5, column=3)
btn_bracket_left = i.Button(root, text="(", command=lambda: add_to_cal("("), width=6, height=2, font=("Arial, 14"))
btn_bracket_left.grid(row=5, column=1)
btn_clear = i.Button(root, text="C", command=clear_field, width=6, height=2, font=("Arial, 14"))
btn_clear.grid(row=6, column=4)
btn_equal = i.Button(root, text="=", command=evaluate_cal, width=13, height=2, font=("Arial, 14"))
btn_equal.grid(row=6, column=1, columnspan=15)
btn_dot = i.Button(root, text=".", command=lambda: add_to_cal("."), width=6, height=2, font=("Arial, 14"))
btn_dot.grid(row=6, column=1)
root.mainloop()