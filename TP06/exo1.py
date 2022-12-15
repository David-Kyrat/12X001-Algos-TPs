########################### Exercise 1 ###########################
from copy import deepcopy


def edges(matrix: list[list[int]]) -> list[tuple[int, int]]:
    """ Returns the list of edges of the graph represented by the given adjacency matrix."""
    return [(i, j) for i in range(len(matrix)) for j in range(len(matrix[i])) if matrix[i][j] == 1]


def flatten_solution(c: list[tuple[int, int]]) -> list[int]:
    """ Flatten the list of coordinates we obtain at the end of the algorithm into a list of vertices."""
    out = []
    for pair in c: out += [*pair]
    return out
        

def get_incident_edges(matrix: list[list[int]], edge:tuple[int, int]):
    u, v = edge
    edgesl = edges(matrix)
    return [e for e in edgesl if u not in e and v not in e]

#def rm_incident_edges(edges: list[tuple[int, int]], edge:tuple[int, int]) -> list[tuple[int, int]]:
    """Removes all edges incident to the given edge from ``edges``."""
    #u, v = edge[0], edge[1]
    """ for j, el in enumerate(matrix[u]):
        if el == 1:  
            edges.remove((u, j))
            s.add((u, j))
    for i, row in enumerate(matrix):
        if row[v] == 1 and (i, v) not in s: 
            edges.remove((i, v)) """
    #return [e for e in edges if u not in e and v not in e]
            
def rm_incident_edges(matrix:list[list[int]], edges: list[tuple[int, int]], edge:tuple[int, int], rmd: set[tuple[int, int]]):
    """Removes all edges incident to the given edge from ``edges``."""
    u, v = edge[0], edge[1]
    n = len(matrix)
    for j in range(n):
        if matrix[u][j] == 1 and (u, j) not in rmd:   
            edges.remove((u, j))
            rmd.add((u, j))
        if matrix[j][u] == 1 and (j, u) not in rmd:
            edges.remove((j, u))
            rmd.add((j, u))
        if matrix[j][v] == 1 and (j, v) not in rmd:   
            edges.remove((j, v))
            rmd.add((j, v))
        if matrix[v][j] == 1 and (v, j) not in rmd:
            edges.remove((v, j))
            rmd.add((v, j))
                
    """ for i in range(n):
        if matrix[i][v] == 1 and (i, v) not in rmd:   
            edges.remove((i, v))
            rmd.add((i, v))
        if matrix[v][i] == 1 and (v, i) not in rmd:
            edges.remove((v, i))
            rmd.add((v, i)) """    

def approx_vertex_cover(matrix: list[list[int]]) -> list[int]:
    """Returns an approximation for the vertex-cover problem.
    The approximation is at most 2-times worse than the optimal solution"""
    C: list[tuple[int, int]] = []
    E: list[tuple[int, int]] = edges(matrix)
    n: int = len(matrix) # matrix is squared
    # We're keeping track of the removed edges because we cannot afford to check if an element belongs to a list 
    # and we are forced to use a list to keep the order required by the exercise & tests
    removed: set[tuple[int, int]] = set()
    for _ in range(n):
        e = E[0]
        C.append(e)
        rm_incident_edges(matrix, E, e, removed)
        if E == []: break

    return flatten_solution(C)

if __name__ == "__main__":
    matrix2 = [
        [0, 1, 0, 0, 0, 0, 0],
        [1, 0, 1, 0, 0, 0, 0],
        [0, 1, 0, 1, 1, 0, 0],
        [0, 0, 1, 0, 1, 1, 1],
        [0, 0, 1, 1, 0, 1, 0],
        [0, 0, 0, 1, 1, 0, 0],
        [0, 0, 0, 1, 0, 0, 0],
    ]
    n = 10
    matrix1 = [[1 if i != j else 0 for j in range(n)] for i in range(n)]
    for row in matrix1: print(row)
    res1 = approx_vertex_cover(matrix1)
    print("res1:", res1)

""" while E != []:
        e: tuple[int, int] = arb_edge(E)
        C.append(e)
        rm_incident_edges(E, e) """
