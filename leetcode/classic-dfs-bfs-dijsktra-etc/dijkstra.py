from math import inf, isfinite
from pprint import PrettyPrinter
from prettytable import PrettyTable
pprint = PrettyPrinter(indent=4).pprint


def mprint(matrix: list[list]):
    p = PrettyTable()
    for row in matrix: p.add_row(row)
    print("_________________")
    print(p.get_string(header=False, border=False))
    print("-----------------")
    print(" ")


def dijkstra(V: list[int], M: list[list[int | float]], start: int, goal: int):
    """start, goal: indices of start and goal vertex in V"""
    N = len(V)
    C, visited = [inf] * N, set()
    C[start] = 0
    path: list[int] = []
    pq: list[tuple[int, int]] = [(start, 0)] # node, cost

    def add_priority(node: int, cost: int):
        pq.append((node, cost))
        for i in range(len(pq) - 1, 0, -1):
            crt, next = pq[i], pq[i - 1]
            if crt[1] > next[1]: pq[i], pq[i - 1] = next, crt
            else: break

    def get_adjacent(node: int) -> list[int]:
        return [i for i in range(N) if i != node and isfinite(M[node][i])]

    enode = None
    while len(pq) > 0:
        enode = pq.pop()[0]
        if enode in visited: continue
        visited.add(enode)
        if enode == goal: return C, path
        for node in get_adjacent(enode):
            if node in visited: continue
            cost = M[enode][node] + C[enode]
            if cost < C[node]:
                C[node] = cost
                add_priority(node, cost) # type: ignore
    return C, path


def main1():
    N = 6
    """ M = [
        [0, 1, inf, inf, 2, inf],
        [inf, 0, 6, 3, inf, inf],
        [inf, 5, 0, inf, inf, inf],
        [7, inf, inf, 0, inf, 2],
        [inf, inf, inf, inf, 0, 1],
        [inf, inf, inf, inf, inf, 0],
    ] """
    M = [
        [0, 7, 9, inf, inf, 14],
        [7, 0, 10, 15, inf, inf],
        [9, 10, 0, 11, inf, 2],
        [inf, 15, 11, 0, 6, inf],
        [inf, inf, inf, 6, 0, 9],
        [14, inf, 2, inf, 9, 0]
        ]
    V = list(range(1, N + 1))

    # dp_all_pair_sp(V, M)
    res, path = dijkstra(V, M, 0, 5)
    print(path)
    for idx, val in enumerate(V): print(f"{val}: {res[idx]}")

if __name__ == "__main__":
    main1()
