import my_mdl

from unittest import TestCase, main


class PerfectTest(TestCase):
    def test_perfect_true(self):
        self.assertTrue(my_mdl.is_perfect(33550336))
        self.assertTrue(my_mdl.is_perfect(8128))   # Это будет выполняться 5 секунд, но зато красиво: здорово, правда?
        self.assertTrue(my_mdl.is_perfect(496))

    def test_perfect_false(self):
        self.assertFalse(my_mdl.is_perfect(33550335))
        self.assertFalse(my_mdl.is_perfect(8127))
        self.assertFalse(my_mdl.is_perfect(495))

    def test_perfect_errors(self):
        with self.assertRaises(ValueError):
            my_mdl.is_perfect(1.5)
            my_mdl.is_perfect(-1)
            my_mdl.is_perfect('line')
            my_mdl.is_perfect(int)

main()


