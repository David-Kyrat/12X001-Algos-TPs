########################### Exercise 1 ###########################
def get_solution(M):
    """Returns a table T where each value T_ij tells the minimum cost to get from city i to city j based on the cost matrix M.
    Also returns the cost of travelling from city 0 to n-1 and the respective path as a list of indexes."""
    # TODO
    


########################### Exercise 2 ###########################
def compute_change(money, coin_set):
    """Returns the optimal change (lowest number of coins) for the given 'money' and 'coin set'."""
    C, n = coin_set, len(coin_set)

    def solve_sub(Ci, left, k, acc):
        """ Returns the list res of coinset where res[k] is the amount of times we used coin Ci[k].
            left := money left to partition into coins, k:= current coin index, acc:= accumulator containing the solution"""
        if k >= n or left <= 0: return acc
        if left - Ci[k] >= 0: return solve_sub(Ci, left - Ci[k], k, acc + [Ci[k]])
        return solve_sub(Ci, left, k + 1, acc)
    
    # matrix of solutions where the row i contains the solution for the subproblem with C = Ci = {c1, ..., ci}
    D = [] #[[] for _ in range(n)]
    for i in range(n):
        D.append(solve_sub(C[:i+1], money, 0, []))

    # Now we just have to search the min of the sum of each column
    # Hence min { sum(D[k]) } for k in {0..n} is the optimal amount of coins, and row k contains the optimal solution.
    
    #! NO
    # in the last column of D i.e. D[n], (D[i][n] contains the amount of coins used for the i-th subproblem) 
    
    opti_row = min(range(n), key= lambda i: sum(D[i]))
    print(f"optimal solutions: {opti_row[-1]} coins: {opti_row[:-1]} ")


########################### Exercise 3 ###########################
def longest_common_subsequence(A, B):
    """Returns the longest common subsequence (LCS) between lists A and B"""
    # TODO


def longest_common_substring(A, B):
    """Returns the longest common substring between lists A and B"""
    # TODO
