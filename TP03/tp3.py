

########################### Exercise 1 ###########################
# DEFINITIONS:
QUEEN = "👸"
WHITE = "⬜"
BLACK = "⬛"



#!
#!
#! As was allowed, The N-Queen problem was implemented like in the lecture notes.
#! Please execute the main function in queen.py with different values of n 
#! to see/test the implementation.
#! Nontheless A copy of the output was added at the end of file, you can verify that it is 
#! the same as the one generate when queen.py is run and also the same one as in your tests 
# For n=5, you can check the correctness of the solutions with the ones at https://www.researchgate.net/figure/The-ten-solutions-of-the-5-queens-problem_fig1_226219656
# For n=6 : https://www.researchgate.net/figure/Four-solutions-to-the-6-queens-problem_fig2_250697280#:~:text=Context%201-,...,as%20shown%20in%20Figure%201. 
#!
#!

#def B(x, k, n):
"""Tells, given the current partial solution x, current step k and final size n, 
    whether the current solution x is valid (True) or not (False)."""
#def T(x, k, n):
"""Returns, given the current partial solution x, step k and final size n, 
    a list of all possible elements that extend the solution x by keeping it valid."""
#def P(x, k, n):
"""Tells, given the final solution x, step k and final size n, 
    whether the given solution x is a final valid solution to the N-Queens problem."""
#def solve_bt(n):
"""Given the size of a square checkerboard, returns the list of all possible solution to the N-Queens problem.
    The order of found solution is trying to insert queens left-to-right, top-to-bottom."""


# TODO: Compare naive and backtracking runtimes
#! DONE IN 'tp3-nqueens.py'


########################### Exercise 2 ###########################
def solve_sudoku(array):
    """Given a square array with None values, fills the None values such that the result is a valid sudoku solution.
    Only the first solution encountered (going left-to-right, top-to-bottom, trying values 0-to-9) is returned."""
    # TODO
    ...


########################### Exercise 3 ###########################
def solve_sum(array, goal_sum):
    """Returns, given an array of positive numbers, a list of all possible selections that add up to variable 'goal_sum'.
    The order of the found solutions is by trying to not selecting (first) and selecting (then) elements from left-to-right."""
    # TODO
    ...
