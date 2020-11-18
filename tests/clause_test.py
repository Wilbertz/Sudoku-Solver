"""Unit tests for clause class."""

import unittest
from clause import Clause


class TestFormula(unittest.TestCase):
    def test_dummy(self):
        self.assertTrue

    def test_formula_constructor(self):
        clause = Clause(set(), set())
        self.assertTrue(clause is not None)


if __name__ == '__main__':
    unittest.main()