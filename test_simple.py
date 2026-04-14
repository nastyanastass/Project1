# Замість старого коду з importlib пишемо просто:
from Program import calculate_temperature

print("Запуск тестів assert...")

# Перевірка 1: 0 градусів Цельсія має бути 32 Фаренгейта
assert calculate_temperature(0, "Цельсій", "Фаренгейт") == 32

# Перевірка 2: 100 градусів Цельсія — це 373.15 Кельвінів
assert calculate_temperature(100, "Цельсій", "Кельвін") == 373.15

# Перевірка 3: Якщо одиниці однакові, число не змінюється
assert calculate_temperature(25, "Цельсій", "Цельсій") == 25

print("Усі assert-тести успішно пройдені!")