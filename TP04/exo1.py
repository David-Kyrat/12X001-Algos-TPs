

########################### Exercise 1 ###########################
def get_solution(M):
    """Returns a table T where each value T_ij tells the minimum cost to get from city i to city j based on the cost matrix M.
    Also returns the cost of travelling from city 0 to n-1 and the respective path as a list of indexes."""
    # We start by setting T at M, like in Floyd algorithm, then
    # we will use those values to compute some intermediary values (optimal solutions for the subproblems)
    # and then by just continuing the algorithm and using our previous we will finaly get the optimal solution in Tij for all ij

    T, n = M, len(M) # M is a squared lower triangular matrix. 
    P = [[] * n] # matrix that will contain the optimal intermediary steps to take to minimize the cost. 
               # I.e. (when filled) P(i,j) is the path to take to pay the min. amount Tij (to go from j to i). (since T is lower triangular we must always have j <= i)

    #! remove this when done testing
    if M is None or n <= 0: return [], [] #[[]], 0, []

    """for k in range(n): 
        for i in range(k): # we could add i=k and k=j but Tij = 0 for all i==j so we dont need to cover them since they'll be 0.
            for j in range(k+1, n):  #! maybe n+1 idk
                crt, candidate = T[i][j], T[i][k] + T[k][j]
                if candidate < crt : # if T_k-1(i, k)+ T_k-1(k, j) < T_k-1(i, j) we set T_k(i, j) to T_k-1(i, k)+ T_k-1(k, j) or else we dont change it
                    T[i][j] = candidate
                    P[i][j].append(k) # we add this step to the matrix of paths to keep a record of the optimal intermediary step to take"""
    def p(i,j): return (T[i][j] if T[i][j] is not None else "_")
    for k in range(n):
        for i in range(k+1, n):
            #print(k, i)
            for j in range(min(k, i-1)): # ignoring those where |i-j| = 1 since there are no interm step
                #if k <= i: continue # T triangular => we then iterate only over for the necessary values of k,i,j that is j < k < i
                                    # We could add i=k and k=j but Tij = 0 for all i==j so we dont need to cover them since they'll be 0. 
                if j in (k, i): continue
                #if j > k: break
                print(f"T[{i}, {j}] = min[ T[{i}, {j}], T[{k}, {j}] + T[{i}, {k}] ]")
            print()

    # Tij now contains the contains min(C(i, j)) (for i,j in [|0, n-1|]) where C(i, j) would be defined 
    # as the function that returns all possible path to go from i-th town to j-th town.

    #minCost_startTolast = T[0][n-1]
    
    return T, P


if __name__ == "__main__":
    M = [
        [0,None,None,None,None,None,None,None],
        [4.9,0,None,None,None,None,None,None],
        [6,3,0,None,None,None,None,None],
        [7.6,4.5,2.8,0,None,None,None,None],
        [11.4,9.3,8.3,6.5,0,None,None,None],
        [14,11.4,11.1,9.3,3.7,0,None,None],
        [16.5,14,13.9,12.9,7.4,5.6,0,None],
        [21,19,13.9,13.9,13.9,12,7.4,0]
    ]

    T, P = get_solution(M)
    print(M)

#!
#! NOPE#ORDER OF MATRIX IN TEST IS REVERSED => TRANPOSE IT !
#!
#!