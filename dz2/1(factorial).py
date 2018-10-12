import my_mdl
import time
from unittest import TestCase, main


class FactorialTest(TestCase):
    def test_non_rec(self):
        self.assertEqual(my_mdl.factor(15), 1307674368000)

    def test_rec(self):
        self.assertEqual(my_mdl.factor_rec(15), 1307674368000)


main()

