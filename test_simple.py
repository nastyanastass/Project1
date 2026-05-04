from Program import calculate_temperature

print("Запуск тестів assert...")

# Функції для pytest
def test_celsius_to_fahrenheit():
    assert calculate_temperature(0, "Цельсій", "Фаренгейт") == 32

def test_celsius_to_kelvin():
    assert calculate_temperature(100, "Цельсій", "Кельвін") == 373.15

def test_same_units():
    assert calculate_temperature(25, "Цельсій", "Цельсій") == 25

# Цей блок спрацює тільки якщо запускати файл як звичайний скрипт (python test_simple.py)
if __name__ == "__main__":
    test_celsius_to_fahrenheit()
    test_celsius_to_kelvin()
    test_same_units()
    print("Усі assert-тести успішно пройдені!")