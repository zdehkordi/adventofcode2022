import unittest

from main import *

sample_input = "./day3/inputs/sample-input"
input = "./day3/inputs/input"
     
class TestParseInput(unittest.TestCase):
    def test_parses_input(self):
        self.assertIn(
            "vJrwpWtwJgWrhcsFMMfFFhFp",
            parse_input(sample_input)
        )

class ItemPriority(unittest.TestCase):
    def test_is_capitalized(self):
        self.assertTrue(is_capitalized("A"))
        self.assertFalse(is_capitalized("a"))

    def test_get_priority(self):
        self.assertEqual(get_priority('a'), 1)
        self.assertEqual(get_priority('z'), 26)
        self.assertEqual(get_priority('A'), 27)
        self.assertEqual(get_priority('Z'), 52)
        

# class TestScore(unittest.TestCase):
#     def test_round(self):
#         self.assertEqual(score_action("A", "Y"), 8)
#         self.assertEqual(score_action("B", "X"), 1)
#         self.assertEqual(score_action("C", "Z"), 6)

# class TestSolutions(unittest.TestCase):
#     def test_sample(self):
#         self.assertEqual(score_game_with_action(sample_input), 15)

#     def test_input(self):
#         self.assertEqual(score_game_with_action(input), 13268)