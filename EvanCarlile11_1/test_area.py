import unittest
import area as a


class TestCase(unittest.TestCase):
    def test_square(self):
        self.assertEqual(a.square(2), 4)
        self.assertAlmostEqual(a.square(33.33), 1110.8889, 5)
        self.assertRaises(ValueError, a.square, "foo")
        self.assertRaises(TypeError, a.square, -3)
        self.assertRaises(TypeError, a.square, 0)
        self.assertRaises(TypeError, a.circle, -6.33)

    def test_circle(self):
        self.assertAlmostEqual(a.circle(2), 12.56637, 5)
        self.assertAlmostEqual(a.circle(33.33), 3489.96041, 5)
        self.assertAlmostEqual(a.circle(1), 3.14159, 5)
        self.assertRaises(ValueError, a.circle, "foo")
        self.assertRaises(TypeError, a.circle, -11)
        self.assertRaises(TypeError, a.circle, 0)

    def test_rectangle(self):
        self.assertEqual(a.rectangle(2, 2), 4)
        self.assertAlmostEqual(a.rectangle(33, 16.66), 549.78, 2)
        self.assertAlmostEqual(a.rectangle(16.66, 2), 33.32, 2)
        self.assertAlmostEqual(a.rectangle(33.33, 16.66), 555.2778, 4)
        self.assertRaises(ValueError, a.rectangle, "foo", 0)
        self.assertRaises(ValueError, a.rectangle, 1, "foo")
        self.assertRaises(ValueError, a.rectangle, "bar", "foo")
        self.assertRaises(TypeError, a.rectangle, -2, -3)
        self.assertRaises(TypeError, a.rectangle, 2, -3)
        self.assertRaises(TypeError, a.rectangle, -2, 3)
        self.assertRaises(TypeError, a.rectangle, 0, 1)
        self.assertRaises(TypeError, a.rectangle, 1, 0)
        self.assertRaises(TypeError, a.rectangle, 0, 0)

    def test_triangle(self):
        self.assertEqual(a.triangle(2, 2), 2)
        self.assertAlmostEqual(a.triangle(33.33, 16.66), 277.6389, 4)
        self.assertAlmostEqual(a.triangle(33, 2.22), 36.63, 2)
        self.assertAlmostEqual(a.triangle(5.55, 100), 277.5, 1)
        self.assertRaises(ValueError, a.triangle, "foo", 0)
        self.assertRaises(ValueError, a.triangle, 1, "foo")
        self.assertRaises(ValueError, a.triangle, "bar", "foo")
        self.assertRaises(TypeError, a.triangle, -2, -3)
        self.assertRaises(TypeError, a.triangle, 1, -3)
        self.assertRaises(TypeError, a.triangle, -1, 1)
        self.assertRaises(TypeError, a.triangle, 0, 1)
        self.assertRaises(TypeError, a.triangle, 1, 0)
        self.assertRaises(TypeError, a.triangle, 0, 0)


def main():
    unittest.main()


if __name__ == "__main__":
    main()
