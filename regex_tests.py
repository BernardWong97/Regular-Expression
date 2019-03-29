import unittest
from shunting_yard import convert
from thompsons import run_thompson


class ThompsonsTest(unittest.TestCase):
    def test_shunting(self):
        postfix = convert("(a.b)|(c*.d)")
        print(postfix)
        self.assertEqual(postfix, "ab.c*d.|")

    def test_thompson(self):
        print(run_thompson("ab.cd.|"))


if __name__ == '__main__':
    unittest.main()
