import unittest
import area as a

class TestCase(unittest.TestCase):
    def test_square(self):
        self.assertEqual(a.square(2),4)
        self.assertEqual(a.square(33.33),1110.8889)
        self.assertEqual(a.square(0),0)
        self.assertRaises(ValueError, a.square, "foo")
        self.assertRaises(TypeError, a.square, -3)
    def test_circle(self):
        self.assertAlmostEqual(a.circle(2),12.56637, 5)
        self.assertAlmostEqual(a.circle(33.33), 3489.96041, 5)
        self.assertEqual(a.circle(0), 0)
        self.assertAlmostEqual(a.circle(1), 3.14159, 5)
        self.assertRaises(ValueError, a.circle, "foo")
        self.assertRaises(TypeError, a.circle, -11)
    def test_rectangle(self):
        self.assertEqual(a.rectangle(2,2),4)
        self.assertEqual(a.rectangle(33.33,16.66),555.2778)
        self.assertEqual(a.rectangle(0, 0),0)
        self.assertEqual(a.rectangle(1, 0),0)
        self.assertEqual(a.rectangle(0, 9999999),0)
        self.assertRaises(ValueError, a.rectangle, "foo", 0)
        self.assertRaises(ValueError, a.rectangle, 1, "foo")
        self.assertRaises(ValueError, a.rectangle, "bar", "foo")
        self.assertRaises(TypeError, a.rectangle, -2, -3)

    def test_triangle(self):
        self.assertEqual(a.triangle(2, 2), 2)
        self.assertEqual(a.triangle(33.33, 16.66), 277.6389)
        self.assertEqual(a.triangle(0, 0), 0)
        self.assertEqual(a.triangle(1, 0),0)
        self.assertEqual(a.triangle(0, 9999999), 0)
        self.assertRaises(ValueError, a.triangle, "foo", 0)
        self.assertRaises(ValueError, a.triangle, 1, "foo")
        self.assertRaises(ValueError, a.triangle, "bar", "foo")
        self.assertRaises(TypeError, a.triangle, -2, -3)
        self.assertRaises(TypeError, a.triangle, 1, -3)