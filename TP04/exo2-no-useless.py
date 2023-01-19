def compute_change(money, coin_set:list) -> list:
    """Computes the optimal change (lowest number of coins) for the given 'money' and 'coin set'.
    Parameters
    ----------
    @ `money` - amount to change
    @ `coin_set` - values of the coins to used when returning the money (sorted in decreasing order)
    Returns: (list) Solution ``l`` s.t. ``l[i]`` is the amount of times ``coin_set[i]`` was used."""    
        
    if coin_set is None or coin_set == [] or money <= 0: return []
    C, n = coin_set, len(coin_set)        
    # matrix of solutions where the row i contains the solution for the subproblem with C = Ci = {cn, ..., ci}. (we start with the lowest coin values)
    # say in rapport maybe that e.g. for C = {10,5,1} we start with C={1} then C={1,2}
    D = [] 
    # Let S be the optimal answer
    # Either there exists a coin of value exactly 'money' (i.e. S = <that coin>)
    for i in range(n):
        coin = C[i]
        if money == coin:
            sol = [0]*n
            sol[i] = 1
            return sol
    # if not then there exists at least 2 subsets S1, S2 such that S1, S2 also minimize the amount of coin used (if S is optimal)
    # (S1, S2) are the solutions to the subproblems, so we can compute the subsolutions step by step by memorizing the answers to the previous steps in D
    def solve_sub(Ci, step_idx):
        """ Returns the list res of coinset where res[k] is the amount of times we used coin Ci[k]."""
        left, sol = money, [0]*n
        
        for k, coin in enumerate(Ci):
            # if largest current coin is too big, then the solution is exactly the one we memorized before
            if (k == 0 and step_idx > 0 and coin > left): return D[step_idx-1]
            crt_amnt, left = (left // coin), (left % coin)
            sol[n-step_idx-1 + k] = crt_amnt # stores crt_amnt in sol but in reversed order since we iterate first on the lowest coins
            if left <= 0: return sol
        return []
        
    for i in range(n-1, -1, -1):
        tmp = solve_sub(C[i:], n-1-i) # padding with the necessary amount of 0s
        D.append(tmp)
    # Now we just have to search the min of the sum of each column
    # Hence min { sum(D[i]) } for i in {0..n} is the optimal amount of coins, and row i contains the optimal solution.
    opti_row = min(range(n), key= lambda i: sum(D[i]))
    out = D[opti_row]
    return out
