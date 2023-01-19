# redifing abs because name is shorter than the 'fabs' function from math (and because it should only take ints here)
def abs(x:int)->int: return x if (x >= 0) else -x


def diff(arr1, arr2):
    '''Return `arr1` \ `arr2` (mathematical difference)'''
    set2 = set(arr2)  # "is in" check should be O(1)
    return [a1 for a1 in arr1 if a1 not in set2]


def isSameDiag(i1, j1, i2, j2):
    '''`isSameDiag` returns `True` if the two points are on the same diagonal, and `False` otherwise.
    Returns: Whether the two coordinates are on the same diagonal (or anti-diagonal).'''
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
    Returns: The set of all possible positions for the `k+1`-th queen. '''
        
    return diff(range(n), x[:k])


def B(x, k, n):
    '''If the last queen is not on the same diagonal as any of the previous queens, then return True
    Parameters
    ----------
    @ `x` - (Partial solution) i.e. Current state of the board. A list of the queens column indices (i.e. x0 x1 ... xk)
    @ `k` - Index of current row/step we are working on  
    @ `n` - the size of the board
    Returns: Whether the current solution is valid. i.e. If the last queen is not on the same diagonal as any of the previous queens'''
        
    if k == 0: return True
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
    # checks each element shares a diagons runs (n-1)*n/2 times
    
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
    No two queen are on the same column, same row or same diagonal.
    Returns: A list of all possible solution to the N-Queens problem. i.e. list of lists of the columns indices of the queens. '''
        
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
