import unittest
from home_snacks_task import ListAssignments

class TestLength(unittest.TestCase):

    def test_countNumber(self):
        numbers = [12,7,33,5,28]

        countNumbers = ListAssignments()

        actual = countNumbers.get_length(numbers)
        expected = 5

        self.assertEqual(actual, expected)



    def test_sum_up_even_positions(self):
        numbers = [12,7,33,5,28]

        sum_numbers = ListAssignments()

        actual = sum_numbers.get_even_numbers(numbers)

        expected = 12

        self.assertEqual(actual,expected)



    def test_smallest(self):

        numbers = [12,7,33,5,28]

        smallest_numbers = ListAssignments()

        actual = smallest_numbers.get_length(numbers)

        expected = 5

        self.assertEqual(actual,expected)
        
