from balls_collide import balls_collide
from unittest import TestCase, main


class CollisionTest(TestCase):
    def test_errors(self):
        self.assertRaises(ValueError, balls_collide, (1, 2, -5), (1, 2, 3))

    def test_true(self):
        self.assertTrue(balls_collide((1, 2, 3), (1, 2, 3)))
        self.assertTrue(balls_collide((0, 0, 1.6), (-2.5, -3.5, 4.28)))
        self.assertTrue(balls_collide((0, 0, 1.333), (3, 4, 4.02)))

    def test_false(self):
        self.assertFalse(balls_collide((1, 1, 1), (2, 2, 0)))
        self.assertFalse(balls_collide((5, 5, 5), (-3, -2, 0)))

    def test_tricky(self):
        self.assertTrue(balls_collide((0, 0, 0), (0, 0, 0)))


main()
