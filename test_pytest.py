import pytest
from Program import calculate_temperature

@pytest.fixture
def input_value():
    return 100

# Тест №1 (Модифікований з фікстурою)
def test_celsius_to_kelvin_with_fixture(input_value):
    assert calculate_temperature(input_value, "Цельсій", "Кельвін") == 373.15

# Тест №2 (Новий параметризований - створить одразу 4 перевірки)
@pytest.mark.parametrize("temp, from_u, to_u, expected", [
    (0, "Цельсій", "Фаренгейт", 32),
    (32, "Фаренгейт", "Цельсій", 0),
    (0, "Цельсій", "Кельвін", 273.15),
    (273.15, "Кельвін", "Цельсій", 0)
])
def test_all_conversions(temp, from_u, to_u, expected):
    assert calculate_temperature(temp, from_u, to_u) == expected

# Тест №3. (Новий тест, який очікуватиме помилку (with pytest.raises))
def test_value_error_on_string():
    # Ми використовуємо конструкцію 'with pytest.raises',
    # щоб сказати: "ми знаємо, що зараз буде помилка TypeError, і це нормально"
    with pytest.raises(TypeError):
        # Передаємо рядок "25" замість числа 25.
        # Оскільки в коді йде множення (temp * 9 / 5), Python видасть TypeError
        calculate_temperature("25", "Цельсій", "Фаренгейт")

# Тест №4. (Новий тест з використанням @pytest.mark.skip)pytest test_pytest.pyv
@pytest.mark.skip(reason="Функція розрахунку для Фаренгейт -> Кельвін ще в розробці")
def test_skipped_conversion():
    # Цей код не буде виконуватися, тому тут можна написати будь-що
    assert calculate_temperature(100, "Фаренгейт", "Кельвін") == 310.928

# Тест №5. (Новий тест з використанням @pytest.mark.xfail)
@pytest.mark.xfail(reason="Відома проблема: функція поки не обробляє від'ємні температури нижче абсолютного нуля")
def test_absolute_zero_fail():
    # Наприклад, ми очікуємо, що -500 Цельсія має видати помилку,
    # але програма поки що просто рахує це за формулою. Тест "впаде".
    assert calculate_temperature(-500, "Цельсій", "Фаренгейт") == "Error"

# Тест №6. Спеціально помилкові тести для демонстрації Failed status
def test_failed_calculation_logic():
    # Ми кажемо, що 0 Цельсія - це 100 Фаренгейта (хоча це 32)
    # Тест впаде, бо математика не зійдеться
    assert calculate_temperature(0, "Цельсій", "Фаренгейт") == 100

def test_wrong_unit_name():
    # Спробуємо передати неіснуючу одиницю виміру
    # Якщо функція не обробляє це помилкою, а тест очікує успіху - він впаде
    assert calculate_temperature(20, "Цельсій", "Кельвін") == 293.15