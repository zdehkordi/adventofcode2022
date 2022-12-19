import unittest
import os
from pathlib import Path

from advent.day02 import *

day = "02"

sample_input = f"inputs/day{day}/sample-input"
input = f"inputs/day{day}/input"
     
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
        self.assertEqual(score_action("A", "Y"), 8)
        self.assertEqual(score_action("B", "X"), 1)
        self.assertEqual(score_action("C", "Z"), 6)

class TestSolutions(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(score_game_with_action(sample_input), 15)

    def test_input(self):
        self.assertEqual(score_game_with_action(input), 13268)

class TestSolutions2(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(score_game_with_outcome(sample_input), 12)

    def test_input(self):
        self.assertEqual(score_game_with_outcome(input), 15508)