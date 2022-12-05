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

    def test_parses_input_group(self):
        self.assertIn(
            ["vJrwpWtwJgWrhcsFMMfFFhFp", "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL", "PmmdzqPrVvPwwTWBwg"],
            parse_input_group(sample_input)
        )
class TestItemPriority(unittest.TestCase):
    def test_is_capitalized(self):
        self.assertTrue(is_capitalized("A"))
        self.assertFalse(is_capitalized("a"))

    def test_get_priority(self):
        self.assertEqual(get_priority('a'), 1)
        self.assertEqual(get_priority('z'), 26)
        self.assertEqual(get_priority('A'), 27)
        self.assertEqual(get_priority('Z'), 52)

class TestCompartment(unittest.TestCase):
    def test_split_compartment(self):
        self.assertEqual(split_rucksack('AB'), ('A', 'B'))
        self.assertEqual(split_rucksack('XXXXYYYY'), ('XXXX', 'YYYY'))

    def test_common_type(self):
        self.assertEqual(common_type('AA'), 'A')
        self.assertEqual(common_type('ABCCDE'), 'C')

    def test_common_type_group(self):
        self.assertEqual(common_type_group(('Aab', 'cAd', 'efA')), 'A')

    def test_priority(self):
        self.assertEqual(find_comp_priority('ABCCDE'), 29)

class TestSolutions(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(sum_compartment_priority(sample_input), 157)

    def test_input(self):
        self.assertEqual(sum_compartment_priority(input), 8176)

class TestSolutions2(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(sum_compartment_priority_group(sample_input), 70)

    def test_input(self):
        self.assertEqual(sum_compartment_priority_group(input), 2689)