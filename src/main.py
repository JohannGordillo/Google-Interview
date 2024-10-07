"""
======================================================================
Google Mexico - Software Engineering III Interview (Round 1)
======================================================================
>> Candidate:       Johann Gordillo
>> Interview Date:  10/03/2024
======================================================================
"""

import unittest
from tests.test_solution import TestSolution


def main() -> None:
    print("Running the unit tests...\n")
    runner = unittest.TextTestRunner(verbosity=0)
    suite = unittest.TestSuite([unittest.TestLoader().loadTestsFromTestCase(TestSolution)])
    runner.run(suite)


if __name__ == '__main__':
    main()