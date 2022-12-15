########################### Exercise 1 ###########################
from exo1 import approx_vertex_cover

def test_approx_vertex_cover():
    # In case of a fully connected graph, the algorithm simply returns all nodes in order
    n = 10
    matrix = [[1 if i != j else 0 for j in range(n)] for i in range(n)]
    assert approx_vertex_cover(matrix) == list(range(n))
    
    # Example from the slides
    matrix = [
        [0, 1, 0, 0, 0, 0, 0],
        [1, 0, 1, 0, 0, 0, 0],
        [0, 1, 0, 1, 1, 0, 0],
        [0, 0, 1, 0, 1, 1, 1],
        [0, 0, 1, 1, 0, 1, 0],
        [0, 0, 0, 1, 1, 0, 0],
        [0, 0, 0, 1, 0, 0, 0],
    ]
    assert approx_vertex_cover(matrix) == [0, 1, 2, 3, 4, 5]
    
    # Another example
    matrix = [
        [0, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0]
    ]

    assert approx_vertex_cover(matrix) == [0, 1]
    
    


########################### Exercise 2 ###########################
from exo2 import approx_knapsack

def test_approx_knapsack():
    w, v = [12, 10, 7, 3, 1], [9, 5, 4, 2, 2]
    assert approx_knapsack(w, v, 0) == ([], [])
    assert approx_knapsack(w, v, 10) == ([7, 1], [4, 2])
    assert approx_knapsack(w, v, 12) == ([12], [9])
    assert approx_knapsack(w, v, 22) == ([12, 1, 3], [9, 2, 2])  
    # ^^ i belive this one is wrong, because even ([12, 10], [9, 5]) 
    #    has weight sum of 10+12=22<=MaxWeight=22 and Value 9+5=14 > 9+2+2=13
    # Furthermore the solution [1, 12, 7], [2, 9, 4] (which is the one i get) gives a value of 15, while having a weight of 20.
    
    assert approx_knapsack(w, v, 29) == ([12, 1, 3, 7], [9, 2, 2, 4])
