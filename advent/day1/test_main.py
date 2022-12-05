import unittest

from pathlib import Path
import os
from .main import *

sample_input = os.path.join(os.path.dirname(os.path.realpath(__file__))
, "inputs/sample-input")
input =  os.path.join(os.path.dirname(os.path.realpath(__file__))
, "inputs/input")
     
class TestFindElf(unittest.TestCase):
    def test_sum_calories(self):
        self.assertEqual(
            [6000,4000,11000,24000,10000],
            sum_calories([[1000,2000,3000],[4000],[5000,6000],[7000,8000,9000],[10000]])
        )


    def test_max_calories(self):
        self.assertEqual(
            24000,
            max([1000,24000,19000])
        )

class TestReadInput(unittest.TestCase):
    def test_reads_file(self):
        self.assertEqual(
            "1000\n2000\n3000\n\n4000\n\n5000\n6000\n\n7000\n8000\n9000\n\n10000", 
            Path(sample_input).read_text()
        )

    def test_breaks_input_into_lines(self):
        self.assertEqual(
            ["this", "that", "", "the other"], 
            "this\nthat\n\nthe other".splitlines()
        )

    def test_parses_input(self):
        self.assertEqual(
            [[1000,2000,3000],[4000],[5000,6000],[7000,8000,9000],[10000]],
            parse_input(sample_input)
        )

class TestSolutions(unittest.TestCase):
    def test_part_1(self):
        self.assertEqual(
            67633, find_max_calories(input)
        )

    def test_part_2(self):
        self.assertEqual(
            199628, find_calories_in_top_three_elves(input)
        )