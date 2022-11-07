from copy import deepcopy


def abs(x): return x if (x >= 0) else -x


def diff(arr1, arr2):  # return arr1 \ arr2
    #if (not arr2 or len(arr2) == 0): return arr1
    set2 = set(arr2)  # "is in" check should be O(1)
    return [a1 for a1 in arr1 if a1 not in set2]


def isSameDiag(i1, j1, i2, j2):
    '''`isSameDiag` returns `True` if the two points are on the same diagonal, and `False` otherwise.
    
    Parameters
    ----------
    @ i1 - row of first queen
    @ j1 - column of the first queen
    @ i2 - row of the second queen
    @ j2 - column of the second queen
    
    Returns
    -------
        Whether the two coordinates are on the same diagonal.'''
    disti, distj = abs(i1-i2), abs(j1-j2)
    return disti == distj


def T(x, k, n):
    '''`T(x,k,n)` returns the set of all possible positions for the `(k+1)`-th queen, given the positions
    of the first `k` queens
    
    Parameters
    ----------
    @ `x` - Current state of the board
    @ `k` - the number of queens placed so far
    @ `n` -  the number of queens
    
    Returns
    -------
        The set of all possible positions for the `k+1`-th queen. '''
    #x => [x_i]_1≤k where x_i = column of i-th queen
    return diff(range(n), x[:k])


def B(x, k, n):
    '''If the last queen is not on the same diagonal as any of the previous queens, then return True
    
    Parameters
    ----------
    @ x - the list of queens  
    @ k - the current row we are working on  
    @ n - the size of the board
    
    Returns
    -------
        If the last queen is not on the same diagonal as any of the previous queens'''
    if k == 0: return True
    last = x[k]
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

def nQueen(n):
    '''`nQueen` takes a number `n` and returns a list of `n` columns indices, each of which is
    such that the i-th queen is located at index `(i, nQueen[i])` of the `n`x`n` chess board.
    No two queen are on the same column, same row or same diagonal
    
    Parameters
    ----------
    @ n - Number of queen and dimensions of chess board
    
    Returns
    -------
        A list of the columns indices of the queens. '''
    if n < 4: return None
    values_list = [[None]]*(n+1)
    stop = [False]
    def bt_rec(x, k, n):        
        for y in T(x, k, n):
            x[k] = y
            if B(x, k, n): 
                stop[0] = P(x, k, n)
                if stop[0]: 
                    printSol(x)
                    return x
                bt_rec(x, k+1, n)
                if stop[0]: return x

    out = bt_rec([None]*n, 0, n)
    return out

def nQueenAll(n):
    '''`nQueen` takes a number `n` and returns a list of `n` columns indices, each of which is
    such that the i-th queen is located at index `(i, nQueen[i])` of the `n`x`n` chess board.
    No two queen are on the same column, same row or same diagonal
    
    Parameters
    ----------
    @ n - Number of queen and dimensions of chess board
    
    Returns
    -------
        A list of the columns indices of the queens. '''
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


def str_sol(x):
    n = len(x)
    M = [['  ' for _ in range(n)] for _ in range(n)]
    for i in range(len(x)):
        if x[i]!= None: M[i][x[i]] = '👑'
    s = ""
    for row in M:
        s += "["
        l = len(row)
        for i in range(l):
            s += f"{row[i]}"
            if (i < l-1): s += ", "
        s += "]\n"
    return s
def printSol(x): print(str_sol(x))

if __name__ == '__main__':
    n = 4    
    #sol1 = nQueen(n)
    #print(f"\nSol1:\n{str_sol(sol1)}")

    print("Other Sols:")
    sols = nQueenAll(n)
    print("sols:", sols, "\n")
    for sol in sols:
        print("sol =", sol)
        printSol(sol)
