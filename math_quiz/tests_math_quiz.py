import unittest
from math_quiz import random_integer, random_operator, math_operation


class TestMathGame(unittest.TestCase):

    def test_random_integer(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_random_operator(self):
        # Test if the returned operator is one of the expected operators
        operators = ['+', '-', '*']
        for _ in range(1000):  # Test a large number of random values
            rand_op = random_operator()
            self.assertIn(rand_op, operators)

    def test_math_operation(self):
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (8, 3, '-', '8 - 3', 5),
            (4, 6, '*', '4 * 6', 24),
            # Add more test cases as needed
        ]

        for num_1, num_2, operator, expected_problem, expected_answer in test_cases:
            problem, answer = math_operation(num_1, num_2, operator)

            # Check if the problem statement matches the expected value
            self.assertEqual(problem, expected_problem)

            # Check if the calculated answer matches the expected value
            self.assertEqual(answer, expected_answer)


if __name__ == "__main__":
    unittest.main()
