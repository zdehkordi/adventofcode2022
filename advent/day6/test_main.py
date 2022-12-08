import unittest
import os

from .main import *

input =  os.path.join(os.path.dirname(os.path.realpath(__file__))
, "inputs/input")
     
class TestParseInput(unittest.TestCase):

    def test_parse_input(self):
        self.assertIn(
            'tnmmpfmfzmmnsmsjmjjbvvhnhzzfmmgpmgpgbgnnwff', 
            parse.input(input)
        )

class TestSearch(unittest.TestCase):
    def test_markers(self):
        self.assertEqual(find_marker('bvwbjplbgvbhsrlpgdmjqwftvncz'), 5)
        self.assertEqual(find_marker('nppdvjthqldpwncqszvftbrmjlhg'), 6)
        self.assertEqual(find_marker('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg'), 10)
        self.assertEqual(find_marker('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'), 11)

    def test_message_markers(self):
        self.assertEqual(find_message_marker('mjqjpqmgbljsphdztnvjfqwrcgsmlb'), 19)
        self.assertEqual(find_message_marker('bvwbjplbgvbhsrlpgdmjqwftvncz'), 23)
        self.assertEqual(find_message_marker('nppdvjthqldpwncqszvftbrmjlhg'), 23)
        self.assertEqual(find_message_marker('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg'), 29)
        self.assertEqual(find_message_marker('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'), 26)

class TestSolutions(unittest.TestCase):
    def test_input(self):
        self.assertEqual(solve(input), 1134)

class TestSolutions2(unittest.TestCase):
    def test_input(self):
        self.assertEqual(solve2(input), 2263)
