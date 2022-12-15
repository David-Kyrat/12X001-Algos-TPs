########################### Exercise 1 ###########################
def edges(matrix: list[list[int]]) -> set[tuple[int, int]]:
    """ Returns the list of edges of the graph represented by the given adjacency matrix."""
    return {(i, j) for i in range(len(matrix)) for j in range(len(matrix[i])) if matrix[i][j] == 1}


def flatten_solution(c: set[tuple[int, int]]) -> list[int]:
    """ Flatten the list of coordinates we obtain at the end of the algorithm into a list of vertices."""
    out = []
    for pair in c: out += [*pair]
    return out
        

def get_incident_edges(matrix: list[list[int]], edge:tuple[int, int]):
    u, v = edge
    edgesl = edges(matrix)
    return [e for e in edgesl if u not in e and v not in e]


def arbitrary_edge(edges: set[tuple[int, int]]):
    """ Returns an arbitrary edge from the given set of edges."""
    return next(iter(edges))


def discard_multiple(s: set, *els):
    """ Applies `s.discard(e)` to each element of `els`. """
    for e in els: s.discard(e)
 
def rm_incident_edges(edges: set[tuple[int, int]], edge:tuple[int, int]):
    """Removes all edges incident to the given edge from ``edges``."""
    u, v = edge[0], edge[1]
    for j in range(len(edges)):
        discard_multiple(edges, (u, j), (j, u), (j, v), (v, j))


def approx_vertex_cover(matrix: list[list[int]]) -> list[int]:
    """Returns an approximation for the vertex-cover problem.
    The approximation is at most 2-times worse than the optimal solution"""
    C: set[tuple[int, int]] = set()
    E: set[tuple[int, int]] = edges(matrix)
    n: int = len(matrix) # matrix is squared
    
    for _ in range(n):
        e = arbitrary_edge(E)
        C.add(e)
        rm_incident_edges(E, e)
        if not E: break

    return sorted(flatten_solution(C))

if __name__ == '__main__':
    n = 10
    matrix = [[1 if i != j else 0 for j in range(n)] for i in range(n)]
    print(approx_vertex_cover(matrix))
    