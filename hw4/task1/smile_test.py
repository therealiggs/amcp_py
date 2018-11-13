from unittest import TestCase, main
from smile_logic import smile


class SmileTest(TestCase):
    def test_true(self):
        self.assertTrue(smile('мыш (кродется)'))
        self.assertTrue(smile('внешний долг США over 9000'))
        self.assertTrue(smile('()[]{}'))
        self.assertTrue(smile('([{}])'))

    def test_false(self):
        self.assertFalse(smile('пРифФкИи [) >3"'))
        self.assertFalse(smile('({[)]'))
        self.assertFalse(smile('{а{ _ __ @{'))
        self.assertFalse(smile('([)]'))


main()
