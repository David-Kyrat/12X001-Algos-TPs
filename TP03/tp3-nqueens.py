

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

########################### Exercise 1 ###########################
import numpy as np
import numba
from numba import jit


QUEEN = "👸"
WHITE = "⬜"
BLACK = "⬛"


def pretty_to_useful(s: str):
        return 1 if s == QUEEN else 0
    
def useful_to_pretty(cell_val:int, row:int, col:int): 
        return QUEEN if cell_val == 1 else (WHITE if (row+col)%2 == 0 else BLACK)

def translate(board) -> list[list]:
    """based on board[0][0], infers whether need to translate WHITE/BLACK/QUEEN to 0/1 or the opposite """
    if board[0][0] in {0, 1}:
        return [[useful_to_pretty(board[i][j], i, j) for j in range(len(board[i]))] for i in range(len(board))]
    else:
        return list(map(lambda row: [pretty_to_useful(cell) for cell in row] , board))

@jit
def P_naive(x:list[list[list[str]]], k, n):
    """ Special implementation of P_naive to work with naive version below"""

    # for each chessboard in x
    for crt in x:
        M = np.zeros((n,n))
        #[[] for _ in range(n)]
        queens:list[tuple(int, int)] = [(0, 0)] #array of queen column indices. (doing this to match with implementation of isSameDiag used in B(x, k, n) below)
        queens.pop()
        for i in range(n):
            for j in range(n):
                el = 0
                if (crt[i][j] == QUEEN):
                    el = 1
                    queens.append((i,j))
                    M[i, j] = el
                #M[i].append(el)

        # checks for diagonals
        for qidx in range(len(queens)-1):
            crtq = queens[qidx]

            for q2idx in range(qidx+1, len(queens)):
                crt2q = queens[q2idx]
                if isSameDiag(crtq[0], crtq[1], crt2q[0], crt2q[1]): return False
    
        # checks for rows
        for row_idx in range(n):
            sum = 0
            for j in range(n):
                sum += M[row_idx][j]
            if sum > 1: return False
        
        # checks for columns
        for col_idx in range(n):
            #def col_i(idcrt): return M[i][idcrt]
            sum = 0
            for j in range(n):
                sum += M[j][col_idx]
            if sum > 1: return False
    return True

@jit
def solve_naive(n, remaining=None, curr_sol=None, i=0, j=0):
    """Naive solution for the N-Queens problem. Do not modify this function."""
    
    # If we are starting, initialize current solution
    if remaining is None:
        remaining = n
        curr_sol = [[WHITE if (r+c)%2 == 0 else BLACK for r in range(n)] for c in range(n)]
    
    # If we placed all queens, check whether the found solution is plausible and return it
    if remaining == 0:
        if P_naive([curr_sol for _ in range(n)], n-1, n):
            out = [[[""]]]
            out[0] = curr_sol
            return out #[curr_sol]

        #out = [[[""]]]; out[0][0].pop()
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
            """ if (sols == [[[""]]]):
                tmp = [""]; tmp.pop()
                all_sols.extend(tmp)
            else: 
                all_sols.extend(sols) """
            
    return all_sols

# redifing abs because name is shorter than the 'fabs' function from math (and because it should only take ints here)
@jit
def abs(x:int)->int: return x if (x >= 0) else -x

@jit
def diff(arr1, arr2):
    '''Return `arr1` \ `arr2` (mathematical difference)
    
    Parameters
    ----------
    @ `arr1` - First array
    @ `arr2` - Array to be removed from arr1
    
    Returns
    -------
        `arr1` without `arr2`.'''
    set2 = set(arr2)  # "is in" check should be O(1)
    return [a1 for a1 in arr1 if a1 not in set2]

@jit
def isSameDiag(i1, j1, i2, j2):
    '''`isSameDiag` returns `True` if the two points are on the same diagonal, and `False` otherwise.
    
    Parameters
    ----------
    @ `i1` - row of first queen
    @ `j1` - column of the first queen
    @ `i2` - row of the second queen
    @ `j2` - column of the second queen
    
    Returns
    -------
        Whether the two coordinates are on the same diagonal (or anti-diagonal).'''
    disti, distj = abs(i1-i2), abs(j1-j2)
    return disti == distj

@jit
def T(x, k, n):
    '''`T(x,k,n)` returns the set of all possible positions for the `(k+1)`-th queen, given the positions
    of the first `k` queens
    
    Parameters
    ----------
    @ `x` - (Partial solution) i.e. Current state of the board. List of column indices (i.e. [x_i]_{1<=i<=k} where x_i = column of i-th queen)
    @ `k` - the number of queens placed so far
    @ `n` - the number of queens
    
    Returns
    -------
        The set of all possible positions for the `k+1`-th queen. '''
    return diff(range(n), x[:k])

@jit
def B(x, k, n):
    '''If the last queen is not on the same diagonal as any of the previous queens, then return True
    
    Parameters
    ----------
    @ `x` - (Partial solution) i.e. Current state of the board. A list of the queens column indices (i.e. x0 x1 ... xk)
    @ `k` - Index of current row/step we are working on  
    @ `n` - the size of the board

    Returns
    -------
        Whether the current solution is valid. i.e. If the last queen is not on the same diagonal as any of the previous queens'''
    if k == 0: return True
    if (k >= n): k -= 1 # handling case where a k greater or equal to n might be passed (should not happen)
    for i in range(k):
        if isSameDiag(k, x[k], i, x[i]): return False
    return True

@jit
def P(x, k, n):
    if None in x: return False
    for i in range(n-1):
        crt = x[i]
        for j in range(i+1, n):
            if isSameDiag(i, crt, j, x[j]): 
                return False
    # checks each element shares a diagonal
    # runs (n-1)*n/2 times
    
    # Checking if 2 columns are the same
    count = [0]*n
    for el in x: # x are columns indices
        count[el] += 1
        if count[el] > 1: return False
        
    return True


def solve_bt(n) -> None | list[list[int]]:
    '''`solve_bt` returns all the solutions for the N-Queens problem for a chess board of size n.
    
    Takes a number `n` and returns a (list of) lists of `n` columns indices, each of which is
    such that the i-th queen is located at index `(i, solve_bt[k][i])` (for the k-th solution) of the `n`x`n` chess board.
    No two queen are on the same column, same row or same diagonal
    
    Parameters
    ----------
    @ `n` - Number of queen i.e. dimensions of chess board
    
    Returns
    -------
        A list of all possible solution to the N-Queens problem. i.e. list of lists of the columns indices of the queens. '''
    if n < 4: return []
    sols:set = set()
    def bt_rec(x, k, n):        
        for y in T(x, k, n):
            x[k] = y
            if B(x, k, n): 
                if P(x, k, n): sols.add(tuple(x)) # using a set to avoid duplicates
                bt_rec(x, k+1, n)

    bt_rec([None]*n, 0, n)    
    return [list(sol_tuple) for sol_tuple in sols] # converting set of tuple back to list of list


########################### PRINTING/TEST FUNCTIONS ###########################
@jit
def fill_emptyboard(n):
    ''' Generate an empty chess board of size `n` with `WHITE` and `BLACK` in each cell

    Parameters
    ----------
    @ `n` - the size of the board
    
    Returns
    -------
        An `n x n` matrix '''
    def fill(i, j):
        return WHITE if (i+j) % 2 == 0 else BLACK
    return [[fill(i, j) for i in range(n)] for j in range(n)]

def pretty_str_sol(x):
    ''' Takes a partial solution (list of column indices) and returns a string representation of the board (with the black and white cell and the queen emoji...)
    
    Parameters
    ----------
    @ `x` - List of int, where `x[i]` is the column index of the queen in row `i`.
    
    Returns
    -------
        A pretty graphic/formatted representation of the chessboard'''
    if x == None or x == []: return []
    n = len(x)
    
    M = fill_emptyboard(n)
    for i in range(n):
        if x[i]!= None: M[i][x[i]] = QUEEN
    s = ""
    for row in M:
        s += "["
        l = len(row)
        for i in range(l):
            s += f"{row[i]}"
            if (i < l-1): s += ", "
        s += "]\n"
    return s


def pretty_str_sols(solution_list):
    """ Returns
        -------
        result of calling `pretty_str_sol(solution)` for each `solution` in `solution_list`"""
    return [pretty_str_sol(solution) for solution in solution_list]
    

def printSol(x): print(pretty_str_sol(x))

################ COMPARISION NAIVE / BACKTRACKING FOR N-QUEEN PROBLEM ################

# TODO: Compare naive and backtracking runtimes
from util import *


def compare_naive_and_backtracking():
    """Compares the running times for the naive and backtracking algorithms for n = [1, ..., 6]"""
    max_n = 4
    plot_n = [n for n in range(1, max_n+2)]
    plot_f1 = runtime_arr(solve_naive, plot_n, unpack=False)
    plot_f2 = runtime_arr(solve_bt, plot_n, unpack=False)
    xlabel = "Chessboard Dimension"
    ylabel = "Runtime (s)"
    title = "Runtime of Naive VS Backtracking solution"
    f1label = "Naive implementation"
    f2label = "Backtracking implementation"
    plotVS(plot_n, plot_f1, plot_f2, title, xlabel, ylabel, f1label, f2label)




########################### MAIN / TEST OF N-QUEEN PROBLEM ###########################


def test_naive(n):
    s = solve_naive(n)
    print(type(s))
    print(s)
    for x in s:
        for subx in x:
            print(subx)
        print("------\n")

def test_backtrack(n):
    print("________________________________________________________\n")
    print("  --- All Solutions to N-Queens problem for n =", n, "---")
    print("________________________________________________________\n")
    sols = solve_bt(n)
    
    for sol, i in zip(sols, range(1, len(sols)+1)):
        
        print(f"Solution n°{i} :")
        printSol(sol)
        print("")

    print("--- END N-Queen ---")


if __name__ == '__main__':
    n = 4
    test_naive(n)
    # test_backtrack(n)
    #compare_naive_and_backtracking()
   
  

# Output for n=4: you can see that is exactly the same one as in your tests
""" 
________________________________________________________

  --- All Solutions to N-Queens problem for n = 4 ---
________________________________________________________

Solution n°1 :
[⬜, ⬛, 👸, ⬛]
[👸, ⬜, ⬛, ⬜]
[⬜, ⬛, ⬜, 👸]
[⬛, 👸, ⬛, ⬜]


Solution n°2 :
[⬜, 👸, ⬜, ⬛]
[⬛, ⬜, ⬛, 👸]
[👸, ⬛, ⬜, ⬛]
[⬛, ⬜, 👸, ⬜]


--- END N-Queen --- """

#
# For n=5, you can check the correctness with the one at https://www.researchgate.net/figure/The-ten-solutions-of-the-5-queens-problem_fig1_226219656
# For n=6 : https://www.researchgate.net/figure/Four-solutions-to-the-6-queens-problem_fig2_250697280#:~:text=Context%201-,...,as%20shown%20in%20Figure%201. 
#
