import tkinter as tk


#  ВИДІЛЯЄМО ЛОГІКУ (Цю частину ми будемо тестувати)
def calculate_temperature(temp, from_unit, to_unit):
    # Якщо одиниці однакові, повертаємо те саме число
    if from_unit == to_unit:
        return temp

    if from_unit == "Цельсій":
        if to_unit == "Фаренгейт":
            return (temp * 9 / 5) + 32
        elif to_unit == "Кельвін":
            return temp + 273.15

    elif from_unit == "Фаренгейт":
        if to_unit == "Цельсій":
            return (temp - 32) * 5 / 9

    elif from_unit == "Кельвін":
        if to_unit == "Цельсій":
            return temp - 273.15

    return temp


# ОНОВЛЮЄМО ФУНКЦІЮ ДЛЯ КНОПКИ
def convert_temperature():
    try:
        # Отримуємо дані з полів вводу
        temp = float(entry.get())
        from_unit = from_var.get()
        to_unit = to_var.get()

        # Викликаємо нашу "чисту" функцію для розрахунку
        result = calculate_temperature(temp, from_unit, to_unit)

        # Виводимо результат
        result_label.config(text="Результат: " + str(round(result, 2)))
    except ValueError:
        result_label.config(text="Помилка: введіть число!")
window = tk.Tk()
window.title("Конвертер температури")

# Велике вікно
window.geometry("400x300")

title = tk.Label(window, text="Конвертер температури", font=("Arial", 16))
title.pack(pady=10)

tk.Label(window, text="Введіть температуру:", font=("Arial", 12)).pack()
entry = tk.Entry(window, font=("Arial", 12), width=20) #помилка
entry.pack(pady=5)

from_var = tk.StringVar()
from_var.set("Цельсій")
to_var = tk.StringVar()
to_var.set("Фаренгейт")

tk.Label(window, text="З якої одиниці:", font=("Arial", 12)).pack()
tk.OptionMenu(window, from_var, "Цельсій", "Фаренгейт", "Кельвін").pack(pady=5)

tk.Label(window, text="У яку одиницю:", font=("Arial", 12)).pack()
tk.OptionMenu(window, to_var, "Цельсій", "Фаренгейт", "Кельвін").pack(pady=5)

tk.Button(window, text="Конвертувати", command=convert_temperature, font=("Arial", 12)).pack(pady=10) #помилка

result_label = tk.Label(window, text="", font=("Arial", 12)) #помилка
result_label.pack()

window.mainloop()