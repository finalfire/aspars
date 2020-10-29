import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from aspars import aspars

class TestSum(unittest.TestCase):

    def test_single_parse_1(self):
        t = '{a, b, f(x), b("ciao")}'
        r = [{"name": "a"}, {"name": "b"}, {"pred": "f", "ext": ["x"], "arity": 1}, {"pred": "b", "ext": ["\"ciao\""], "arity": 1}]
        self.assertEqual(aspars.ASPars().parse(t), r, "Should be {}".format(r))

    def test_multiple_parse(self):
        t = '{a, b, f(x), b("foo")}\n{f(-1,0,1), x, g("42",42)}'.split('\n')
        r = [
            [{"name": "a"}, {"name": "b"}, {"pred": "f", "ext": ["x"], "arity": 1}, {"pred": "b", "ext": ["\"foo\""], "arity": 1}],
            [{"pred": "f", "ext": [-1, 0, 1], "arity": 3}, {"name": "x"}, {"pred": "g", "ext": ["\"42\"", 42], "arity": 2}]
        ]
        self.assertEqual(list(aspars.ASPars().parse(t)), r, "Should be {}".format(r))

if __name__ == '__main__':
    unittest.main()