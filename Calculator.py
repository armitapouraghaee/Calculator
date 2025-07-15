import tkinter as tk  # وارد کردن کتابخانه ساخت رابط گرافیکی

# ایجاد پنجره اصلی
window = tk.Tk()
window.title("Simple Calculator")
window.geometry("300x400")

# ایجاد کادر ورودی
display = tk.Entry(window, font=("Arial", 18), justify="right")
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


# Frame برای دکمه‌ها
button_frame = tk.Frame(window)
button_frame.grid()

# لیست دکمه‌ها
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", "C", "=", "+"
]

# ساخت دکمه‌ها با حلقه
row = 0
col = 0
for button_text in buttons:
    button = tk.Button(button_frame, text=button_text, width=5, height=2, font=("Arial", 14), command=lambda x=button_text: on_button_click(x))
    button.grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1

def on_button_click(value):
    if value == "=":
        try:
            result = str(eval(display.get()))
            display.delete(0, tk.END)
            display.insert(0, result)
        except:
            display.delete(0, tk.END)
            display.insert(0, "Error")
    elif value == "C":
        display.delete(0, tk.END)
    else:
        display.insert(tk.END, value)




window.mainloop()