import tkinter as tk  # وارد کردن کتابخانه ساخت رابط گرافیکی

# ایجاد پنجره اصلی
window = tk.Tk()
window.title("Simple Calculator")
window.geometry("300x400")

# ایجاد کادر ورودی
entry = tk.Entry(window, font=("Arial", 24), justify="right")
entry.pack(pady=10)

# Frame برای دکمه‌ها
button_frame = tk.Frame(window)
button_frame.pack()

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
    button = tk.Button(button_frame, text=button_text, width=5, height=2, font=("Arial", 14))
    button.grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1

window.mainloop()