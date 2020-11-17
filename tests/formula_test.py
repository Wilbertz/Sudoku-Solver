"""Unit tests for formula class."""
import logging
import unittest
from formula import Formula


class TestFormula(unittest.TestCase):

    def test_dummy(self):
        self.assertTrue(True)

    def test_formula_constructor(self):
        formula = Formula([])
        self.assertTrue(formula is not None)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    unittest.main()
