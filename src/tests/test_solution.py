"""
Unit tests for the solution to the interview problem.
"""

import unittest
from solution.solution import Solution

class TestSolution(unittest.TestCase):
    """Tests for the can_transform() method of the Solution class."""
    @classmethod
    def setUpClass(cls):
        cls.solution = Solution()

    def test_different_number_of_L_and_R(self):
        self.assertFalse(self.solution.can_transform("_L__R_L_R", "_L__R_L__"))

    def test_different_order_of_L_and_R(self):
        self.assertFalse(self.solution.can_transform("_RL_", "L__R"))

    def test_correct_transformation(self):
        self.assertTrue(self.solution.can_transform("", ""))
        self.assertTrue(self.solution.can_transform("_", "_"))
        self.assertTrue(self.solution.can_transform("_L__R_L_R", "_L__R_L_R"))
        self.assertTrue(self.solution.can_transform("_L__R_L_R", "L____RL_R"))
        self.assertTrue(self.solution.can_transform("R__L_RL_L", "__RL_RLL_"))

    def test_impossible_transformation(self):
        self.assertFalse(self.solution.can_transform("_L__R_L_R", "_L_R__L_R"))
        self.assertFalse(self.solution.can_transform("_L_R_L", "L_R__L"))
        self.assertFalse(self.solution.can_transform("_L_R_L", "_L__LR"))

    @classmethod
    def tearDownClass(cls):
        del cls.solution


if __name__ == '__main__':
    unittest.main()