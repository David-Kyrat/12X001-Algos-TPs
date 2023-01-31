def getpath(i, j, P):
    """ return optimal path with the optimal intermediary steps in P"""
    intermed = sorted(P[i][j])
    opti_path = [i]
    for inter_step in intermed:
        opti_path += [inter_step]
    opti_path += [j]
    return opti_path

def get_solution(M):
    """Returns a table T where each value T_ij tells the minimum cost to get from city i to city j based on the cost matrix M.
    Also returns the cost of travelling from city 0 to n-1 and the respective path as a list of indexes."""
    # We start by setting T at M, like in Floyd algorithm, then
    # we will use those values to compute some intermediary values (optimal solutions for the subproblems)
    # and then by just continuing the algorithm and using our previous we will finaly get the optimal solution in Tij for all ij
    T, n = deepcopy(M), len(M) # M is a squared lower triangular matrix. 
    P = [[[] for _ in range(n)] for _ in range(n)]
    # matrix that will contain the optimal intermediary steps to take to minimize the cost. 
    # I.e. (when filled) P(i,j) is the path to take to pay the min. amount Tij (to go from j to i). 
    # (since T is lower triangular we must always have j <= i)
    for k in range(n):
        for i in range(k+1, n):
            for j in range(min(k+1, i-1)): # ignoring those where |i-j| = 1 since there are no interm step
                if j == i: continue        # T triangular => we then iterate only over for the necessary values of k,i,j 
                                           # that is j < k < i. 
                                           # We could add i=k and k=j but Tij = 0 for all i==j so we dont need to cover them 
                                           # since they'll be 0. 
                crt, candidate = T[i][j], T[i][k] + T[k][j]
                if candidate < crt : # if T_k-1(i, k)+ T_k-1(k, j) < T_k-1(i, j) we set T_k(i, j) to T_k-1(i, k)+ T_k-1(k, j) 
                                     # or else we dont change it
                    T[i][j] = candidate
                    P[i][j].append(k) # we add this step to the matrix of paths to keep a record of the optimal intermediary 
                                      # step to take
    # Tij now contains the contains min(C(i, j)) (for i,j in [|0, n-1|]) where C(i, j) would be defined 
    # as the function that returns all possible path to go from i-th town to j-th town.
    opti_path = getpath(n-1, 0, P)
    return T, T[n-1][0] , opti_path
