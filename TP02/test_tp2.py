########################### Exercise 1 ###########################
from tp2 import knapsack_a, knapsack_b, knapsack_c

def test_knapsack_a():
    w, v = [10, 3, 7, 12, 1], [5, 2, 4, 9, 2]
    assert knapsack_a(w, v, 0) == ([], [])
    assert knapsack_a(w, v, 10) == ([10], [5])
    assert knapsack_a(w, v, 12) == ([12], [9])
    assert knapsack_a(w, v, 22) == ([12, 10], [9, 5])
    assert knapsack_a(w, v, 29) == ([12, 10, 7], [9, 5, 4])
    
def test_knapsack_b():
    w, v = [10, 3, 7, 12, 1], [5, 2, 4, 9, 2]
    assert knapsack_b(w, v, 0) == ([], [])
    assert knapsack_b(w, v, 10) == ([1, 3], [2, 2])
    assert knapsack_b(w, v, 12) == ([1, 3, 7], [2, 2, 4])
    assert knapsack_b(w, v, 22) == ([1, 3, 7, 10], [2, 2, 4, 5])
    assert knapsack_b(w, v, 29) == ([1, 3, 7, 10], [2, 2, 4, 5])
    
def test_knapsack_c():
    w, v = [10, 3, 7, 12, 1], [5, 2, 4, 9, 2]
    assert knapsack_c(w, v, 0) == ([], [])
    assert knapsack_c(w, v, 10) == ([1, 3], [2, 2])
    assert knapsack_c(w, v, 12) == ([1, 3, 7], [2, 2, 4])
    assert knapsack_c(w, v, 22) == ([1, 12, 3], [2, 9, 2])
    assert knapsack_c(w, v, 29) == ([1, 12, 3, 7], [2, 9, 2, 4])



########################### Exercise 2 ###########################
from tp2 import compute_change

def test_compute_change():
    coin_set = [30, 24, 12, 6, 3, 1]
    assert compute_change(0, coin_set) == []
    assert compute_change(2, coin_set) == [1, 1]
    assert compute_change(4, coin_set) == [3, 1]
    assert compute_change(10, coin_set) == [6, 3, 1]
    assert compute_change(33, coin_set) == [30, 3]
    assert compute_change(100, coin_set) == [30, 30, 30, 6, 3, 1]


########################### Exercise 3 ###########################
from tp2 import kruskal

def test_kruskal():
    A = [
        [0, 1, 2],
        [1, 0, 10],
        [2, 10, 0]
    ]
    
    B = [
        [0, 2, 1],
        [2, 0, 10],
        [1, 10, 0]
    ]
    
    C = [
        [0, 10, 2],
        [10, 0, 1],
        [2, 1, 0]
    ]
    
    assert kruskal(A) == [(0, 1), (0, 2)]
    assert kruskal(B) == [(0, 2), (0, 1)]
    assert kruskal(C) == [(1, 2), (0, 2)]
    