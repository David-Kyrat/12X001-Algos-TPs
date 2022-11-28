########################### Exercise 1 ###########################
from exo1 import get_solution

def test_get_solution():
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
    
    T = [
        [0, None, None, None, None, None, None, None],
        [4.9, 0, None, None, None, None, None, None],
        [6, 3, 0, None, None, None, None, None],
        [7.6, 4.5, 2.8, 0, None, None, None, None],
        [11.4, 9.3, 8.3, 6.5, 0, None, None, None],
        [14, 11.4, 11.1, 9.3, 3.7, 0, None, None],
        [16.5, 14, 13.9, 12.9, 7.4, 5.6, 0, None],
        [19.9, 16.9, 13.9, 13.9, 13.9, 12, 7.4, 0]
    ]
    
    count, path = 19.9, [0, 2, 7]
    assert get_solution(M) == (T, count, path)


########################### Exercise 2 ###########################
from exo3 import compute_change

def test_compute_change():
    coin_set = [30, 24, 12, 6, 3, 1]
    
    assert compute_change(1, coin_set) == [1]
    assert compute_change(30, coin_set) == [30]
    assert compute_change(48, coin_set) == [24, 24] # Optimal solution greedy could not find.

########################### Exercise 3 ###########################
from exo2 import longest_common_subsequence, longest_common_substring

def test_longest_common_subsequence():
    a, b = ["a", "c", "t", "g", "a", "a"], ["c", "g", "a", "t"]
    assert longest_common_subsequence(a, b) == ["c", "g", "a"]

def test_longest_common_substring():
    a, b = ["a", "c", "t", "g", "a", "a"], ["c", "g", "a", "t"]
    assert longest_common_substring(a, b) == ["g", "a"]
