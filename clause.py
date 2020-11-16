"""This class encodes a clause."""
from typing import Set


class Clause:
    def __init__(self, variables: Set[int], negated_variables: Set[int]):
        self.check_constructor_arguments(variables, negated_variables)
        self.Variables = variables
        self.NegatedVariables = negated_variables
        self.IsUnsat = False

    def substitute_as_true(self, index: int):
        if index in self.Variables:
            pass
        pass

    def substitute_as_false(self, index: int):
        pass

    @staticmethod
    def check_constructor_arguments(variables: Set[int], negated_variables: Set[int]):
        if variables.intersection(negated_variables):
            raise Exception("Variables and NegatedVariables cannot contain a common element")


if __name__ == '__main__':
    pass
