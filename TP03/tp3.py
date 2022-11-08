########################### Exercise 1 ###########################
# DEFINITIONS:
QUEEN = "👸"
WHITE = "⬜"
BLACK = "⬛"

def solve_naive(n, remaining=None, curr_sol=None, i=0, j=0):
    """Naive solution for the N-Queens problem. Do not modify this function."""
    
    # If we are starting, initialize current solution
    if remaining is None:
        remaining = n
        curr_sol = [[WHITE if (r+c)%2 == 0 else BLACK for r in range(n)] for c in range(n)]
    
    # If we placed all queens, check whether the found solution is plausible and return it
    if remaining == 0:
        if P([curr_sol for _ in range(n)], n-1, n):
            return [curr_sol]
        return []
    
    # If we still have queens to place, place one in the next non-explored square and find all solutions
    all_sols = []
    for r in range(n):
        for c in range(n):
            
            # Skipping visited squares
            if r < i or (r == i and c < j):
                continue
            
            # Placing a queen in the next available square (left-to-right, top-to-bottom)
            copy_sol = [[curr_sol[i][j] for j in range(n)] for i in range(n)]
            copy_sol[r][c] = QUEEN
            
            # Finding all solutions with the newly placed queen
            sols = solve_naive(n, remaining-1, copy_sol, r, c+1)
            all_sols.extend(sols)
            
    return all_sols

def B(x, k, n):
    """Tells, given the current partial solution x, current step k and final size n, 
    whether the current solution x is valid (True) or not (False)."""
    # TODO
    ...
    

def T(x, k, n):
    """Returns, given the current partial solution x, step k and final size n, 
    a list of all possible elements that extend the solution x by keeping it valid."""
    # TODO
    ...
    

def P(x, k, n):
    """Tells, given the final solution x, step k and final size n, 
    whether the given solution x is a final valid solution to the N-Queens problem."""
    # TODO
    ...

def solve_bt(n):
    """Given the size of a square checkerboard, returns the list of all possible solution to the N-Queens problem.
    The order of found solution is trying to insert queens left-to-right, top-to-bottom."""
    # TODO
    ...
    

def compare_naive_and_backtracking():
    """Compares the running times for the naive and backtracking algorithms for n = [1, ..., 6]"""
    from time import time
    import matplotlib.pyplot as plt
    # TODO
    ...

# TODO: Compare naive and backtracking runtimes
# compare_naive_and_backtracking()



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
