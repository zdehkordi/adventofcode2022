from os.path import join, dirname, realpath
from .main import *

sample_inp = join(dirname(realpath(__file__)), "inputs/sample-input")
inp =  join(dirname(realpath(__file__)), "inputs/input")

def test_is_visible():
    assert is_visible(5, Neighbors(0,2,5,5)) is True
    assert is_visible(1, Neighbors(7,5,2,9)) is False

def test_is_edge():
    assert is_edge(np.eye(3, 3), Coordinate(0, 0)) is True
    assert is_edge(np.eye(3, 3), Coordinate(0, 2)) is True
    assert is_edge(np.eye(3, 3), Coordinate(2, 0)) is True
    assert is_edge(np.eye(3, 3), Coordinate(2, 2)) is True
    assert is_edge(np.eye(3, 3), Coordinate(0, 1)) is True

    assert is_edge(np.eye(3, 3), Coordinate(1, 1)) is False

def test_neighbors():
    m = np.array([[1,2,3],
                  [4,5,6],
                  [7,8,9]])

    assert get_neighbors(m, Coordinate(1, 1)) == Neighbors(2,8,4,6)

def test_neighbors_big():
    m = np.array([[1,2,3,3],
                  [4,5,6,6],
                  [7,8,9,9]])

    assert get_neighbors(m, Coordinate(2, 1)) == Neighbors(3,9,5,6)

def test_solve_sample():
    assert solve(sample_inp) == 21

def test_solve():
    assert solve(inp) == 1812
