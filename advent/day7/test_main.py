import unittest
import os

from .main import *

sample_input = os.path.join(os.path.dirname(os.path.realpath(__file__)), "inputs/sample-input")
input =  os.path.join(os.path.dirname(os.path.realpath(__file__)), "inputs/input")

class TestParseInput(unittest.TestCase):
    def test_parse_input(self):
        directories = parse.directories(sample_input)
        for d in ['a', 'e', 'd']: self.assertIn(d, directories) 

class TestFS(unittest.TestCase):
    def test_file(self):
        f = fs.parse("8033020 d.log")
        self.assertEqual(f.name, "d.log")
        self.assertEqual(f.size, 8033020)
        self.assertTrue(isinstance(f ,file))

    def test_dir(self):
        d = fs.parse("dir e")
        self.assertEqual(d.name, "e")
        self.assertTrue(isinstance(d, dir))

class TestLS(unittest.TestCase):
    def test_ls_one(self):
        self.assertEqual(
            ls(parse.input(sample_input), 'e'),
            ["584 i"]
        )

class TestSize(unittest.TestCase):
    def test_one_file(self):
        self.assertEqual(
            size(parse.input(sample_input), 'e'), 584
        )

    def test_many_file(self):
        self.assertEqual(
            size(parse.input(sample_input), 'd'), 24933642
        )

    def test_deep(self):
        self.assertEqual(
            size(parse.input(sample_input), 'a'), 94853
        )

class TestSolve(unittest.TestCase):
    def test_solve_sample(self):
        self.assertEqual(
            solve(sample_input), 95437
        )

    def test_solve(self):
        self.assertEqual(
            solve(input), 95437
        )