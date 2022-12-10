########################### Exercise 1 ###########################
from fifteen_puzzle import c_hat, solve_taquin
from fifteen_puzzle import UP, RIGHT, DOWN, LEFT

board = [[1, 2, 3, 4], 
         [5, 6, 16, 8], 
         [9, 10, 7, 11],
         [13, 14, 15, 12]]


def test_c_hat():
    assert c_hat(board) == 3


def test_solve_taquin():
    assert solve_taquin(board) == [DOWN, RIGHT, DOWN]


########################### Exercise 2 ###########################
from tp5 import solve_tasks


def test_solve_tasks():
    cost_matrix = [
        [11, 14, 11, 17],
        [12, 15, 17, 14],
        [18, 13, 19, 20],
        [40, 22, 23, 28],
    ]

    assert solve_tasks(cost_matrix) == [0, 3, 1, 2]


########################### Exercise 3 ###########################
from tp5 import solve_shortest_path


def test_solve_shortest_path():
    domain = [
        # We want to get here
        # |
        # v
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 0, 0],
        [0, 0, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        # ^
        # |
        # We start from here
    ]
    a, b = (7, 6), (0, 7)
    solution = [a, (7, 7), (6, 7), (5, 7), (4, 7), (3, 7), (2, 7), (1, 7), b]

    assert solve_shortest_path(domain, a, b) == solution
