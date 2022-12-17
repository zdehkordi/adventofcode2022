from unittest import TestCase

from pathlib import Path

from advent.day01 import *

day = "01"

sample_input = f"inputs/day{day}/sample-input"
input = f"inputs/day{day}/input"
     
class TestFindElf(TestCase):
    def test_sum_calories(self):
        calories = [[1000,2000,3000],[4000],[5000,6000],[7000,8000,9000],[10000]]
        assert [6000,4000,11000,24000,10000] == sum_calories(calories)

    def test_max_calories(self):
        assert 24000 == max([1000,24000,19000])

class TestReadInput(TestCase):
    def test_reads_file(self):
        assert "1000\n2000\n3000\n\n4000\n\n5000\n6000\n\n7000\n8000\n9000\n\n10000" == Path(sample_input).read_text()

    def test_breaks_input_into_lines(self):
        assert ["this", "that", "", "the other"] == "this\nthat\n\nthe other".splitlines()

    def test_parses_input(self):
        assert [[1000,2000,3000],[4000],[5000,6000],[7000,8000,9000],[10000]] == parse_input(sample_input)

class TestSolutions(TestCase):
    def test_part_1(self):
        assert 67633 == find_max_calories(input)

    def test_part_2(self):
        assert 199628 == find_calories_in_top_three_elves(input)