from cmath import exp
from math import floor, ceil, log2
from random import randint

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
    if element == None or A == None: return False
    n = len(A)
    if n == 0: return False 
    if n == 1: return element == A[0]
    anc = n // 2 + 1 #* anc := appearence number constraint. number of times it must appear to be the majority element
    i, crt_an = 0, 0 #* current appearence number
    for el in A:
        if el == element:
            crt_an += 1
            if crt_an >= anc: return True
    else: return False


def reduce(A):
    """Reduces A in at most len(A) // 2 parts using pair-wise votes"""
    n = len(A)
    if n <= 1: return A #* If A is empty or a singleton => result will be A itself

    if n % 2 == 1:
       rand_el = A[randint(0, n-1)]
       if is_majority(A, rand_el): return rand_el
       else: A.remove(rand_el) # Now n is even

    A_prime = []
    for i in range(0, n-1, 2):
      a, b = A[i], A[i+1]
      if a == b: A_prime.append(a)
    return A_prime
        
def handle_reduce_odd(A):
     n = len(A)
     
    
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
  pr = 1
  for _ in range(p): pr *= base
  return pr
  # complexité theta(n*f) où f est la complexité de multiplier pr par base (au moins Omega(n)).






def exp_dandc(base, p):
    if p == 0: return 1 
    if p == 1: return base
    
    from math import log2
    """Divide and Conquer implementation of exponentiation"""
    def toBin(x): return bin(x)[2:][::-1]
    binP, i0, stop = toBin(p),  1, int(log2(p))
    
    def exp_rec(prod, crt_pow, i):
        """ summ : contains the sum of the base^(2^i)
        crt_pow: the current power of k (should be equal to k^(2^i))
        binP: contains the binary representation of k (as an array)
        i : the current step
        stop: the max number of step i.e. stopping condition is "i >= stop" (stop := floor(log_2(p)))
        """
        if i > stop: return prod
        crt_pow = crt_pow * crt_pow #if (i != 0) else k)
        if binP[i] == '1': prod *= crt_pow
        return exp_rec(prod, crt_pow, i+1)

    prod0, pow_0 = 1, base
    if (binP[0] == '1'): prod0 = pow_0
    return exp_rec(prod0, pow_0, i0)


    
def compare_exp():
    """Compare runtimes of the naive and D&C algorithms using matplotlib"""
    from time import time
    import matplotlib.pyplot as plt
    
    # TODO
    ...
    
# TODO: Uncomment to see comparison
# compare_exp()
