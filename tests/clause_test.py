"""Unit tests for clause class."""
import logging
import unittest
from clause import Clause


class TestClause(unittest.TestCase):

    def test_clause_constructor_should_accept_empty_argument_sets(self):
        clause = Clause(set(), set())
        self.assertTrue(clause is not None)

    def test_clause_constructor_should_accept_non_empty_argument_sets(self):
        clause = clause = Clause({1}, {2})
        self.assertTrue(clause is not None)

    def test_clause_constructor_should_detect_inconsistent_arguments(self):
        with self.assertRaises(Exception) as context:
            clause = Clause({1}, {1})
        self.assertTrue('Variables and NegatedVariables cannot contain a common element' in str(context.exception))


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    unittest.main()
