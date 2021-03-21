import unittest
from HW_2.custom_meta import CustomClass


class MetaTestCase(unittest.TestCase):
    def setUp(self):
        self.inst = CustomClass()

    def test_custom_x(self):
        self.assertEqual(self.inst.custom_x, 50)

    def test_custom_line(self):
        self.assertEqual(self.inst.custom_line(), 100)

    def test_x(self):
        with self.assertRaises(AttributeError):
            self.inst.x

    def test_line(self):
        with self.assertRaises(AttributeError):
            self.inst.line()
