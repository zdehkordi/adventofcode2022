import unittest
import os

from .main import *

sample_input = os.path.join(os.path.dirname(os.path.realpath(__file__))
, "inputs/sample-input")
input =  os.path.join(os.path.dirname(os.path.realpath(__file__))
, "inputs/input")
     
class TestParseInput(unittest.TestCase):

    def test_num_stacks(self):
        self.assertEqual(3, parse.num_stacks(' 1   2   3 '))

    def test_parses_stacks(self):
        stacks = parse.stacks(sample_input)
        self.assertIn(
            ['D', 'C', 'M'],
            stacks
        )
        self.assertIn(
            ['P'],
            stacks
        )

    def test_parse_instructions(self):
        instructions = parse.instructions(sample_input)
        self.assertIn(
            'move 2 from 2 to 1',
            instructions
        )

class TestCrateOperations(unittest.TestCase):
    def test_top(self):
        self.assertEqual(top(['Z', 'N', 'D']), 'Z')

    def test_remove(self):
        self.assertEqual(remove(['A', 'B']), ['B'])

    def test_add(self):
        self.assertEqual(add(['B'], 'A'), ['A', 'B'])

    def test_move(self):
        self.assertEqual(
            move([['A'], ['B'], ['C']], 3, 2), [['A'], ['C', 'B'], []]
        )

class TestSolutions(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(solve(sample_input), 'CMZ')

    def test_input(self):
        self.assertEqual(solve(input), 'ZWHVFWQWW')

class TestSolutions2(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(solve2(sample_input), 'MCD')

    def test_input(self):
        self.assertEqual(solve2(input), 933)
