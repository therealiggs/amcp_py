import my_mdl
import time
from unittest import TestCase, main


class FactorialTest(TestCase):
    def test_non_rec_true(self):
        self.assertEqual(my_mdl.factor(15), 1307674368000)
        self.assertEqual(my_mdl.factor(2), 2)
        self.assertEqual(my_mdl.factor(3), 6)
        self.assertEqual(my_mdl.factor(4), 24)

    def test_rec_true(self):
        self.assertEqual(my_mdl.factor_rec(15), 1307674368000)
        self.assertEqual(my_mdl.factor_rec(2), 2)
        self.assertEqual(my_mdl.factor_rec(3), 6)
        self.assertEqual(my_mdl.factor_rec(4), 24)

    def test_tricky(self):
        self.assertEqual(my_mdl.factor(0), 1)
        self.assertEqual(my_mdl.factor(1), 1)
        self.assertEqual(my_mdl.factor_rec(0), 1)
        self.assertEqual(my_mdl.factor_rec(1), 1)

    def test_non_rec_errors(self):
        with self.assertRaises(ValueError):
            my_mdl.factor(1.5)
            my_mdl.factor(-1)
            my_mdl.factor('line')
            my_mdl.factor(int)

            my_mdl.factor_rec(1.5)
            my_mdl.factor_rec(-1)
            my_mdl.factor_rec('line')
            my_mdl.factor_rec(int)


main()

