"""This class encodes a formula."""
from typing import List
from clause import Clause


class Formula:
    def __init__(self, clauses: List[Clause]):
        self.clauses = clauses

    @property
    def is_unsat(self) -> bool:
        return False


if __name__ == '__main__':
    pass
