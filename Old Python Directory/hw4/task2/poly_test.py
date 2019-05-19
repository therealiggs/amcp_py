from poly_logic import proizv
from unittest import TestCase, main


class PolyTest(TestCase):
    def test_equal(self):
        self.assertEqual(proizv('3x^7 + 10x^5 - 4x^2 + 3'),
                         '21x^6 + 50x^4 - 8x')
        self.assertEqual(proizv('2x^5'), '10x^4')
        self.assertEqual(proizv('0x^7+0x^2'), '0')
        self.assertEqual(proizv('5x^2+3x^1'), '10x + 3')


main()
