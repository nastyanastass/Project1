import unittest
from Program import calculate_temperature

class TestConverter(unittest.TestCase):
    def test_celsius_to_fahrenheit(self):
        self.assertEqual(calculate_temperature(0, "Цельсій", "Фаренгейт"), 32)

    def test_celsius_to_kelvin(self):
        self.assertEqual(calculate_temperature(0, "Цельсій", "Кельвін"), 273.15)

    def test_fahrenheit_to_celsius(self):
        self.assertAlmostEqual(calculate_temperature(32, "Фаренгейт", "Цельсій"), 0)

if __name__ == '__main__':
    unittest.main()