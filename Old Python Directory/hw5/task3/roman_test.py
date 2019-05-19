from roman import Roman
from unittest import TestCase, main

with open('roman.txt') as file:
    text = [line[:-1] for line in file]  # Подгружаем файлик со столбцом всех
    # римских чисел до 1999 (он создан с помощью roman_generator.py из
    # таблички соответствия из интернета)


class RomanTest(TestCase):

    def test_equal(self):
        for i in range(1, 2000):
            self.assertEqual(str(Roman(i)), text[i])  # Здесь, по сути,
            #  проверяем соответствие любого int i из области определения
            #  его римскому написанию по файлику roman.txt

    def test_true(self):
        self.assertTrue(Roman(5) == Roman(5))

    def test_false(self):
        self.assertFalse(Roman(5) == Roman(6))

    def test_errors(self):
        self.assertRaises(ValueError, Roman, -1)
        with self.assertRaises(ValueError):
            a = Roman(1000) + Roman(1000)


main()
