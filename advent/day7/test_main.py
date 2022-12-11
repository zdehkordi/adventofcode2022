import unittest
import os
from .main import *

sample_input = os.path.join(os.path.dirname(os.path.realpath(__file__)), "inputs/sample-input")
input =  os.path.join(os.path.dirname(os.path.realpath(__file__)), "inputs/input")

class TestBuildingDirectories(unittest.TestCase):
    def test_moves_to_root(self):
        self.assertEqual([["/"], {}], exec_command([], {}, "$ cd /"))

    def test_moves_down_dir(self):
        self.assertEqual([["/", "d"], {}], exec_command(["/"], {}, "$ cd d"))

    def test_moves_up_dir(self):
        self.assertEqual([["/"], {}], exec_command(["/", "d"], {}, "$ cd .."))

    def test_adds_dir(self):
        self.assertEqual([["/"], {"/": {}, "/a": {}}], exec_command(["/"], {"/": {}}, "dir a"))

    def test_adds_file(self):
        self.assertEqual([["/"], {"/": {"f": 99}}], exec_command(["/"], {"/": {}}, "99 f"))

    def test_ignore_ls(self):
        self.assertEqual([["/"], {}], exec_command(["/"], {}, "$ ls"))

    def test_builds_test_directory(self):
        self.assertEqual(
            {"/": {"b.txt": 14848514, "c.dat": 8504156} , "/a": {"f": 29116, "g": 2557, "h.lst": 62596}, "/a/e": {"i": 584}, "/d": {"j": 4060174, "d.log": 8033020, "d.ext": 5626152, "k": 7214296}},
            exec_command_file(sample_input)
        )

    def test_total_size(self):
        self.assertEqual(
            584,
            size(sample_input, "/a/e")
        )

        self.assertEqual(
            94853,
            size(sample_input, "/a")
        )

        self.assertEqual(
            24933642,
            size(sample_input, "/d")
        )

        self.assertEqual(
            48381165,
            size(sample_input, "/")
        )

class TestSolve(unittest.TestCase):
    def test_solve_sample(self):
        self.assertEqual(
            95437,
            solve(sample_input)
        )

    def test_solve_input(self):
        self.assertEqual(
            919137,
            solve(input)
        )