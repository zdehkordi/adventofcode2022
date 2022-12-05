import unittest
import os

from .main import *

sample_input = os.path.join(os.path.dirname(os.path.realpath(__file__))
, "inputs/sample-input")
input =  os.path.join(os.path.dirname(os.path.realpath(__file__))
, "inputs/input")
     
class TestParseInput(unittest.TestCase):
    def test_parses_input(self):
        self.assertIn(
            (range(2, 5), range(6, 9)),
            parse_input(sample_input)
        )

class TestRanges(unittest.TestCase):
    def test_fully_contains(self):
        self.assertTrue(fully_contains(range(1, 5), range(2, 3)))
        self.assertFalse(fully_contains(range(1, 5), range(2, 6)))

    def test_overlap(self):
        self.assertTrue(overlap(range(1, 5), range(2, 6)))
        self.assertTrue(overlap(range(1, 5), range(2, 6)))
        self.assertFalse(overlap(range(1, 5), range(6, 10)))

class TestSolutions(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(num_supersets(sample_input), 2)

    def test_input(self):
        self.assertEqual(num_supersets(input), 584)

class TestSolutions2(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(num_intersections(sample_input), 4)

    def test_input(self):
        self.assertEqual(num_intersections(input), 933)
