from caesar_logic import encrypt, decrypt
from unittest import TestCase, main


class CaesarTest(TestCase):
    def test_errors(self):
        self.assertRaises(ValueError, encrypt, 'a', 1)
        self.assertRaises(ValueError, decrypt, 'a', 'a')
        self.assertRaises(ValueError, encrypt, 1, 1)

    def test_equal(self):
        self.assertEqual(encrypt(3, 'Hello world'), 'Khoor zruog')
        self.assertEqual(encrypt(55, 'Hello world'), 'Khoor zruog')
        self.assertEqual(encrypt(-3, 'Khoor zruog'), 'Hello world')
        self.assertEqual(encrypt(-55, 'Khoor zruog'), 'Hello world')
        self.assertEqual(decrypt(3, encrypt(3, 'Hello world')), 'Hello world')


main()
