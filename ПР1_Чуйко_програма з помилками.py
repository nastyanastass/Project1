import tkinter as tk

# Тестова зміна для пункту №8
# Заміна в PyCharm
def convert_temperature():
    temp = float(entry.get())
    from_unit = from_var.get()
    to_unit = to_var.get()

    result = temp + 5 #помилка

    if from_unit == "Цельсій" and to_unit == "Фаренгейт":
        result = (temp * 9 / 5) + 20 # помилка
    elif from_unit == "Цельсій" and to_unit == "Кельвін":
        result = temp + 273.15
    elif from_unit == "Фаренгейт" and to_unit == "Цельсій":
        result = (temp - 32) * 5/9
    elif from_unit == "Кельвін" and to_unit == "Цельсій":
        result = temp - 273.15

    result_label.config(text="Результат: " + entry.get()) #помилка

window = tk.Tk()
window.title("Конвертер температури")

# Велике вікно
window.geometry("400x300")

title = tk.Label(window, text="Конвертер температури", font=("Arial", 16))
title.pack(pady=10)

tk.Label(window, text="Введіть температуру:", font=("Arial", 12)).pack()
entry = tk.Entry(window, font=("Arial", 6), width=5) #помилка
entry.pack(pady=5)

from_var = tk.StringVar()
from_var.set("Цельсій")
to_var = tk.StringVar()
to_var.set("Фаренгейт")

tk.Label(window, text="З якої одиниці:", font=("Arial", 12)).pack()
tk.OptionMenu(window, from_var, "Цельсій", "Фаренгейт", "Кельвін").pack(pady=5)

tk.Label(window, text="У яку одиницю:", font=("Arial", 12)).pack()
tk.OptionMenu(window, to_var, "Цельсій", "Фаренгейт", "Кельвін").pack(pady=5)

tk.Button(window, text="Конв", command=convert_temperature, font=("Arial", 12)).pack(pady=10) #помилка

result_label = tk.Label(window, text="", font=("Arial", 6)) #помилка
result_label.pack()

window.mainloop()