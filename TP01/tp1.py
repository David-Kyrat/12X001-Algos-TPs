from math import floor, ceil

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
    n = len(A)
    anc = floor(n/2) + 1 #ac := appearence number constraint. number of times it must appear to be the majority element
    i, crt_an = 0, 0 # current appearence number
    for el in A:
        if el == element:
            crt_an += 1
            if crt_an >= anc: return True
    else: return False


def reduce(A):
    """Reduces A in at most len(A) // 2 parts using pair-wise votes"""
    n = len(A)
    A_prime = []
    for i in range(floor(n/2)):
      a, b = A[i], A[i+1]
      if a == b: A_prime.append(a)
    return A_prime
        
    
    
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
