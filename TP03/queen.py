
########################### Exercise 1 ###########################

QUEEN = "👸"
WHITE = "⬜"
BLACK = "⬛"

# redifing abs because name is shorter than the 'fabs' function from math (and because it should only take ints here)
def abs(x:int)->int: return x if (x >= 0) else -x


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


def solve_bt(n) -> list[list[int]]:
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
    if n < 4: return None
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

def printSol(x): print(pretty_str_sol(x))


########################### MAIN / TEST OF N-QUEEN PROBLEM ###########################

if __name__ == '__main__':
    n = 5

    print("________________________________________________________\n")
    print("  --- All Solutions to N-Queens problem for n =", n, "---")
    print("________________________________________________________\n")
    sols = solve_bt(n)
    
    for sol, i in zip(sols, range(1, len(sols)+1)):
        
        print(f"Solution n°{i} :")
        printSol(sol)
        print("")

    print("--- END N-Queen ---")

#
# For example for n=5, you can check the correctness with the one at https://www.researchgate.net/figure/The-ten-solutions-of-the-5-queens-problem_fig1_226219656
# For n=6 : https://www.researchgate.net/figure/Four-solutions-to-the-6-queens-problem_fig2_250697280#:~:text=Context%201-,...,as%20shown%20in%20Figure%201. 
#