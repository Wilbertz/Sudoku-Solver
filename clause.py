"""This class encodes a clause."""
from typing import List


class Clause:
    def __init__(self, variables: List[int], negated_variables: List[int]):
        self.Variables = variables
        self.NegatedVariables = negated_variables
        self.IsUnsat = False

    def substitute_as_true(self, index: int):
        if index in self.Variables:
            pass
        pass

    def substitute_as_false(self, index: int):
        pass


if __name__ == '__main__':
    pass
