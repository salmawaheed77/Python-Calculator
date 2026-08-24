import tkinter as tk

window = tk.Tk()
window.title("Calculator")

window_width = 420
window_height = 500

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

window.geometry(f"{window_width}x{window_height}+{x}+{y}")
window.resizable(False, False)

f = ("Arial", 14)

def calculate():
    try:
        expression = entry.get()
        result = eval(expression)

        output.config(text=f"Result = {result}")

        history.insert(tk.END,f"{expression} = {result}")

    except:
        output.config(text="Invalid Input")

def clear():
    entry.delete(0, tk.END)
    output.config(text="")

def square():
    try:
        num = float(entry.get())
        result = num ** 2
        output.config(text=f"Result = {result}")
        history.insert(tk.END,f"{num}² = {result}")
    except:
        output.config(text="Invalid Input")

title = tk.Label(window,text="Calculator",font=("Arial", 18, "bold"))
title.pack(pady=(15, 10))

entry = tk.Entry(window, font=f)
entry.pack(pady=10)

frame = tk.Frame(window)
frame.pack()
btn_plus = tk.Button(frame,text="+",font=f,width=10,command=lambda: entry.insert(tk.END,"+"))
btn_plus.grid(row=0, column=0, padx=5, pady=5)

btn_minus = tk.Button(frame,text="-",font=f,width=10,command=lambda: entry.insert(tk.END,"-"))
btn_minus.grid(row=0, column=1, padx=5, pady=5)

btn_mul = tk.Button(frame,text="*",font=f,width=10,command=lambda: entry.insert(tk.END,"*"))
btn_mul.grid(row=0, column=2, padx=5, pady=5)

btn_div = tk.Button(frame,text="/",font=f,width=10,command=lambda: entry.insert(tk.END,"/"))
btn_div.grid(row=1, column=0, padx=5, pady=5)

btn1 = tk.Button(frame, text="x²", font=f, width=10, command=square)
btn1.grid(row=1, column=1, padx=5, pady=5)

btn2 = tk.Button(frame, text="=", font=f, width=10, command=calculate)
btn2.grid(row=1, column=2, padx=5, pady=5)

btn3 = tk.Button(frame, text="Clear", font=f, width=10, command=clear)
btn3.grid(row=2, column=0, padx=5, pady=5)

output = tk.Label(window, font=f, fg="red")
output.pack(pady=10)

history_label = tk.Label(window,text="History",font=("Arial", 14, "bold"))
history_label.pack()

history = tk.Listbox(window, width=40, height=10)
history.pack(pady=10)

window.bind("<Return>", lambda event: calculate())

window.mainloop()
