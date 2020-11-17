# The main startup code.
import logging
from dpll_algorithm import DpllAlgorithm


def main():
    logging.debug("Hallo")
    print("Python main function started.")
    solver = DpllAlgorithm()


def report_solution(solution):
    pass


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    main()
