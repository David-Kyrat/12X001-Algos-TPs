########################### Exercise 2 ###########################
from tp3 import solve_sudoku

def test_solve_sudoku():
    grid = [
        [None, None, 4, 6, None, 8, None, 1, 2],
        [6, None, 2, 1, None, None, 3, 4, None],
        [1, 9, 8, None, 4, None, 5, None, 7],
        [8, None, 9, 7, 6, None, 4, None, 3],
        [4, None, None, None, 5, 3, None, 9, 1],
        [None, 1, 3, None, None, 4, 8, None, None],
        [9, 6, 1, 5, None, 7, 2, None, 4],
        [2, None, 7, 4, 1, None, 6, 3, None],
        [None, 4, None, 2, 8, None, 1, 7, None],
    ]
    
    solution = [
        [5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7], 
        [8, 5, 9, 7, 6, 1, 4, 2, 3], 
        [4, 2, 6, 8, 5, 3, 7, 9, 1], 
        [7, 1, 3, 9, 2, 4, 8, 5, 6], 
        [9, 6, 1, 5, 3, 7, 2, 8, 4], 
        [2, 8, 7, 4, 1, 9, 6, 3, 5], 
        [3, 4, 5, 2, 8, 6, 1, 7, 9]
    ]
    
    assert solve_sudoku(grid) == solution
    
    
########################### Exercise 3 ###########################
from tp3 import solve_sum

def test_solve_sum():
    assert solve_sum([10], 1) == []
    assert solve_sum([10], 10) == [[1]]
    
    assert solve_sum([3, 4, 1, 2, 5, 6], 10) == [
        [0, 1, 0, 0, 0, 1],
        [0, 1, 1, 0, 1, 0],
        [1, 0, 0, 1, 1, 0],
        [1, 0, 1, 0, 0, 1],
        [1, 1, 1, 1, 0, 0]
    ]
