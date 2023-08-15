# 1584. Min Cost to Connect All Points
from typing import List


class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        return 0

def pp(e: tuple[int, int]):
    e1, e2 = e
    c1, c2 = chr(e1 + 97), chr(e2 + 97) # a = 97
    return c1, c2

def pp2(e1:int, e2:int):
    c1, c2 = chr(e1 + 97), chr(e2 + 97) # a = 97
    return c1.upper(), c2.upper()

def ps(s: set[tuple[int, int]]):
    return [pp(e) for e in s]


def in_tree(v: int, tree: set[tuple[int, int]]) -> bool:
    # sourcery skip: use-any
    for edge in tree:
        if v in edge:
            return True
    return False

def find_tree(v: int, trees: list[set[tuple[int, int]]]) -> int: #set[tuple[int, int]]:
    for i, t in enumerate(trees):
        if in_tree(v, t):
            return i
    s = f"{v} should be in trees since it contains all edges"
    raise ValueError(s)

def merge_tree(t1_idx: int, t2_idx: int, trees: list[set[tuple[int, int]]]):
        t1, t2 = trees[t1_idx], trees[t2_idx]
        trees.remove(t1)
        print(f"Merging {ps(t1)} and {ps(t2)}")
        trees[t2_idx] = t1.union(t2)
        #print(trees)


def kruskal(A: list[list[int]]) -> set[tuple[int, int]]:  # sourcery skip: identity-comprehension
    """A: adjacency matrix, Return: MST"""
    N = len(A)
    if not A or not A[0]: return set()
    if N == 1: return {(0, 0)}

    trees, S = [], []  # S: sorted list of edges (w.r.t. weight)
    trees: list[set[tuple[int, int]]] = []
    for i in range(N):
        # list of trees at start : list of trees of length 1 i.e. each edge in a singleton
        for j in range(N):
            if A[i][j] == 0: continue  # (no edge)
            trees.append({(i, j)})
            S.append([(i, j), A[i][j]])

    S.sort(key=lambda kv: kv[1], reverse=True)  # min should be last
    F: set[tuple[int, int]] = set()  # forest which will hold/be the MST
    while S and len(F) < N:
        e, cost = S.pop()
        print(f"e = {pp(e)} ({cost})")
        v1, v2 = e
        t1_idx, t2_idx = find_tree(v1, trees), find_tree(v2, trees)
        if trees[t1_idx] != trees[t2_idx]:
            F.add(e)
            merge_tree(t1_idx, t2_idx, trees)
            print("")
    return F


if __name__ == "__main__":
    A = [#a b  c  d  e  f  g
        [0, 7, 0, 5, 0, 0, 0],
        [7, 0, 8, 9, 7, 0, 0],
        [0, 8, 0, 0, 5, 0, 0],
        [5, 9, 0, 0, 15, 6, 0],
        [0, 7, 5, 15, 0, 8, 9],
        [0, 0, 0, 6, 8, 0, 11],
        [0, 0, 0, 0, 9, 11, 0],
    ]
    F = kruskal(A)
    print(ps(F))
