import unittest
from ad2 import first_total_method_inputs
from ad2 import write_to_file
from ad3 import my_total_metod

class MyTestCase1(unittest.TestCase):
    def test_something(self):
        a =first_total_method_inputs()
        self.assertEqual('1 2 3', a)

class MyTestCase2(unittest.TestCase):
    def test_something(self):
        a =write_to_file('1 2 3','trojkoty_test.txt')
        self.assertEqual(0, a)

class MyTestCase3(unittest.TestCase):
    def test_something(self):
        a = my_total_metod('/home/michu/PycharmProjects/pierwsze_programy/trojkoty_test.txt','test_obwody.txt')
        self.assertEqual(0, a)

class MyTestCase4(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

if __name__ == '__main__':
    unittest.main()
