import convert
import unittest

class TestCases(unittest.TestCase):
    pass

    def test_str_to_float_1(self):
        input = "1.23"
        result = convert.str_to_float(input)
        expected = 1.23
        self.assertEqual(expected,result)
    def test_str_to_float_2(self):
        input = "hello"
        result = convert.str_to_float(input)
        expected = None
        self.assertEqual(expected, result)
