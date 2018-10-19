import my_mdl

from unittest import TestCase, main


class PascalTest(TestCase):
    def test_pascal_true(self):
        self.assertEqual(my_mdl.pascal_tri(0), [])
        self.assertEqual(my_mdl.pascal_tri(1), [[1]])
        self.assertEqual(my_mdl.pascal_tri(2), [[1], [1, 1]])
        self.assertEqual(my_mdl.pascal_tri(3), [[1], [1, 1], [1, 2, 1]])
        self.assertEqual(my_mdl.pascal_tri(4), [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]])

    def test_pascal_errors(self):
        with self.assertRaises(ValueError):
            my_mdl.pascal_tri(1.5)
            my_mdl.pascal_tri(-1)
            my_mdl.pascal_tri('line')
            my_mdl.pascal_tri(int)

main()
