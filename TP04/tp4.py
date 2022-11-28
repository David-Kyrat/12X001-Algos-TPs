########################### Exercise 1 ###########################
def get_solution(M):
    """Returns a table T where each value T_ij tells the minimum cost to get from city i to city j based on the cost matrix M.
    Also returns the cost of travelling from city 0 to n-1 and the respective path as a list of indexes."""
    # TODO
    


########################### Exercise 2 ###########################
def compute_change(money, coin_set):
    """Returns the optimal change (lowest number of coins) for the given 'money' and 'coin set'."""
    A, C, n = money, coin_set, len(coin_set)

    def solve_sub(Ci) -> list[int]:
        """Returns the list res of coinset where res[k] is the amount of times we used coin Ci[k]. res[n] contains the amount of coins used overall for this subproblem"""
        res = [0]*(n+1)

        
        return res

    
    # matrix of solutions where the row i contains the solution for the subproblem with C = Ci = {c1, ..., ci}
    D = [[] for _ in range(n)]
        
    for i in range(n):
        D[i] = solve_sub(C[:i+1])

    # Now we just have to search the min in the last column of D i.e. D[n], (D[n][i] contains the amount of coins used for the i-th subproblem) 
    # Hence min { D[n][k] } for k in {0..n} is the optimal amount of coins, and row k contains the optimal solution.
    


########################### Exercise 3 ###########################
def longest_common_subsequence(A, B):
    """Returns the longest common subsequence (LCS) between lists A and B"""
    # TODO


def longest_common_substring(A, B):
    """Returns the longest common substring between lists A and B"""
    # TODO
