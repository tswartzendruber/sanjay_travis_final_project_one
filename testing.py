import unittest
from module import *


class MyTestCase(unittest.TestCase):
    def test_one(self):
        self.assertEqual(one(1), 1)
        self.assertEqual(one(2), 3)
        self.assertEqual(one(3), 6)
        self.assertNotEqual(one(4), 11)

        with self.assertRaises(TypeError):
            one('BANANA')
            one(-5.7)
            one(9.4)

        with self.assertRaises(ValueError):
            one(-5)
            one(0)

    def test_two(self):
        self.assertEqual(two(2, 1), 2)
        self.assertEqual(two(2, 2), 4)
        self.assertEqual(two(2, 3), 8)
        self.assertNotEqual(two(3, 4), 80)

        with self.assertRaises(TypeError):
            two('CAT', 'DOG')
            two('CAT', 9)
            two(10, 'DOG')
            two('CAT', -9)
            two(-10, 'DOG')

            two('CAT', 9.1)
            two(10.2, 'DOG')
            two('CAT', -9.1)
            two(-10.2, 'DOG')

            two(-5.7, -6.8)
            two(9.4, 10.5)
            two(5.7, -6.8)
            two(-9.4, 10.5)

        with self.assertRaises(ValueError):
            two(0, 0)
            two(0, 1)
            two(1, 0)
            two(0, 4)
            two(5, 0)

            two(-2, 5)
            two(2, -5)
            two(-2, -5)

    def test_three(self):
        self.assertEqual(three(1), '1')
        self.assertEqual(three(5), '5 4 3 2 1')
        self.assertEqual(three(10), '10 9 8 7 6 5 4 3 2 1')
        self.assertNotEqual(three(7), '4 3 2 1')

        with self.assertRaises(TypeError):
            one('CUCUMBER')
            one(-4.2)
            one(18.7)

        with self.assertRaises(ValueError):
            one(-8)
            one(0)


if __name__ == '__main__':
    unittest.main()
