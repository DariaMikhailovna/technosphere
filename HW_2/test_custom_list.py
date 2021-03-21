import unittest
from HW_2.custom_list import CustomList


class MetaTestCase(unittest.TestCase):
    def setUp(self):
        self.my_list1 = CustomList([5, 1, 3, 7])
        self.my_list2 = CustomList([1, 2, 7])
        self.my_list3 = CustomList([1, 2, 4, 1])
        self.my_list4 = CustomList([3, 5])

    def test_add(self):
        self.assertEqual(self.my_list1 + self.my_list2, [6, 3, 10, 7])
        self.assertEqual(self.my_list2 + self.my_list3, [2, 4, 11, 1])
        self.assertEqual(self.my_list2 + self.my_list4, [4, 7, 7])
        self.assertEqual(self.my_list4 + [1, 0], [4, 5])
        self.assertEqual([0, 1, 2] + self.my_list4, [3, 6, 2])
        self.assertEqual(self.my_list4 + [], [3, 5])

    def test_add_type(self):
        self.assertEqual(type(self.my_list1 + self.my_list2), CustomList)
        self.assertEqual(type(self.my_list1 + [1, 2]), CustomList)
        self.assertEqual(type([3] + self.my_list2), CustomList)

    def test_sub(self):
        self.assertEqual(self.my_list1 - self.my_list2, [4, -1, -4, 7])
        self.assertEqual(self.my_list2 - self.my_list3, [0, 0, 3, -1])
        self.assertEqual(self.my_list2 - self.my_list4, [-2, -3, 7])
        self.assertEqual(self.my_list4 - [1, 0], [2, 5])
        self.assertEqual([0, 5, 2] - self.my_list4, [-3, 0, 2])
        self.assertEqual([] - self.my_list4, [-3, -5])
        self.assertEqual(self.my_list4 - [], [3, 5])

    def test_sub_type(self):
        self.assertEqual(type((self.my_list1 - self.my_list2)), CustomList)
        self.assertEqual(type(self.my_list1 - [1, 2]), CustomList)
        self.assertEqual(type([] - self.my_list2), CustomList)
