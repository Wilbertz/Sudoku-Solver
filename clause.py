"""This class encodes a clause."""


class Clause:
    def __init__(self):
        self.Variables = []
        self.NegatedVariables = []
        self.IsUnsat = False

    def substitute_as_true(self, index: int):
        if index in self.Variables:
            pass
        pass

    def substitute_as_false(self, index: int):
        pass


if __name__ == '__main__':
    pass
