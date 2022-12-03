import unittest

from main import *

sample_input = "./day2/inputs/sample-input"
input = "./day2/inputs/input"
     
class TestParseInput(unittest.TestCase):
    def test_reads_file(self):
        self.assertEqual(
            "A Y\nB X\nC Z", 
            Path(sample_input).read_text()
        )

    def test_parses_input(self):
        self.assertEqual(
            [["A", "Y"], ["B", "X"], ["C", "Z"]],
            parse_input(sample_input)
        )

class TestScore(unittest.TestCase):
    def test_round(self):
        self.assertEqual(score_round("A", "Y"), 8)
        self.assertEqual(score_round("B", "X"), 1)
        self.assertEqual(score_round("C", "Z"), 6)

class TestSolutions(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(score_game(sample_input), 15)

    def test_input(self):
        self.assertEqual(score_game(input), 13268)