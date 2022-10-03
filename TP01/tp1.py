########################### Exercise 1 ###########################

def naive(A):
    """Finds the majority element of A in a naive way. DO NOT CHANGE"""
    majority_element = None
    for i in range(len(A)):
        element = A[i]
        element_count  = 0
        for j in range(i, len(A)):
            if A[j] == element:
                element_count += 1
                if element_count > len(A) // 2:
                    majority_element = element
    return majority_element
                

def is_majority(A, element):
    """Tells if 'element' is the majority element in A"""
    # TODO
    ...

def reduce(A):
    """Reduces A in at most len(A) // 2 parts using pair-wise votes"""
    # TODO
    ...
    
def dandc(A):
    """Divide and Conquer algorithm"""
    # TODO
    ...

def compare_naiv_and_dandc():
    """Compare runtimes of the naive and D&C algorithms using matplotlib"""
    import random
    from time import time
    import matplotlib.pyplot as plt
    
    # TODO
    ...


# TODO: Uncomment to see comparison
# compare_naiv_and_dandc()


########################### Exercice 2 ###########################
def exp_naive(base, p):
    """Naive implementation of exponentiation"""
    # TODO
    ...
    
def exp_dandc(base, p):
    """Divide and Conquer implementation of exponentiation"""
    # TODO
    ...
    
    
def compare_exp():
    """Compare runtimes of the naive and D&C algorithms using matplotlib"""
    from time import time
    import matplotlib.pyplot as plt
    
    # TODO
    ...
    
# TODO: Uncomment to see comparison
# compare_exp()
