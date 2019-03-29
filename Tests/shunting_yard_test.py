import unittest
from shunting_yard import convert


class ShuntingYardTest(unittest.TestCase):
    def test(self):
        self.assertEqual(convert("(a.b)|(c*.d)"), "ab.c*d.|")


if __name__ == '__main__':
    unittest.main()
