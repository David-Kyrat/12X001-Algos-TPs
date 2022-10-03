import random

########################### Exercise 1 ###########################
from tp1 import is_majority, reduce, dandc

def create_two(n):
    a = []
    b = []
    for i in range(n // 2 + 1):
        a.append(1)
    
        if i > 0:
            b.append(1)
        
    for i in range(n - len(a)):
        a.append(i+100)
            
    for i in range(n - len(b)):
        b.append(i+100)
        
    random.shuffle(a)
    random.shuffle(b)
    return a, b

def test_is_majority():
    assert is_majority([], 3) == False
    assert is_majority([3], None) == False
    assert is_majority([3], 3) == True
    assert is_majority([3, 3, 1], 3) == True
    assert is_majority([3, 3, 1, 1], 3) == False
    
    for n in [1000, 1001]:
        a, b = create_two(n)
        assert is_majority(a, 1) == True
        assert is_majority(b, 1) == False
        
def test_reduce():
    assert reduce([1, 1]) == [1]
    assert reduce([1, 2]) == []
    assert reduce([1, 1, 2, 2, 3, 3]) == [1, 2, 3]
    assert reduce([1, 2, 2, 2, 3, 1]) == [2]
    assert reduce([0, 1, 0, 2, 0, 1]) == []
    assert reduce([0, 0, 0, 0, 0, 0, 0, 0]) == [0, 0, 0, 0]
    
def test_dandc():
    assert dandc([]) == None
    assert dandc([1]) == 1
    assert dandc([1, 1]) == 1
    assert dandc([1, 0, 1]) == 1
    assert dandc([1, 0, 1, 0]) == None
    
    for n in [10, 11]:
        a, b = create_two(n)
        assert dandc(a) == 1
        assert dandc(b) == None


########################### Exercise 2 ###########################
from tp1 import exp_naive, exp_dandc


def exp_test(fn):
    assert fn(2, 0) == 1
    assert fn(2, 1) == 2
    assert fn(2, 10) == 1024
    assert fn(-1, 0) == 1
    assert fn(-1, 1) == -1
    assert fn(-1, 2) == 1
    assert fn(-4, 2) == 16
    assert fn(-4, 3) == -64

def test_exp_naive():
    exp_test(exp_naive)
    
def test_exp_dandc():
    exp_test(exp_dandc)
