########################### Exercise 1 ###########################
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


def approx_vertex_cover(matrix: list[list[int]]) -> list[int]:
    """Returns an approximation for the vertex-cover problem.
    The approximation is at most 2-times worse than the optimal solution"""
    C: list[tuple[int, int]] = []
    E: list[tuple[int, int]] = edges(matrix)
    n: int = len(matrix) # matrix is squared
    #? We're keeping track of the removed edges because we cannot afford to check if an element belongs to a list 
    #? and we are forced to use a list to keep the order required by the exercise & tests
    removed: set[tuple[int, int]] = set()
    for _ in range(n):
        e = E[0]
        C.append(e)
        rm_incident_edges(matrix, E, e, removed)
        if E == []: break

    return flatten_solution(C)
