import unittest

from main import *

sample_input = "./day4/inputs/sample-input"
input = "./day4/inputs/input"
     
class TestParseInput(unittest.TestCase):
    def test_parses_input(self):
        self.assertIn(
            (range(2, 5), range(6, 9)),
            parse_input(sample_input)
        )

class TestRanges(unittest.TestCase):
    def test_fully_contains(self):
        self.assertTrue(fully_contains(range(1, 5), range(2, 3)))
        self.assertFalse(fully_contains(range(1,5), range(5,10)))


class TestSolutions(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(num_supersets(sample_input), 2)

    def test_input(self):
        self.assertEqual(num_supersets(input), 584)
