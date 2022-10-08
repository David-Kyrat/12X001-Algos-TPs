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

def toBin(x): return bin(x)[2:][::-1]


b = toBin(25)
print(b)
prod = 1
for i in range(len(b)):
    bi = int(b[i])
    print("bi", bi, (2**i) if (bi == 1) else 1)
    prod = prod * ((3**(2**i)) if (bi == 1) else 1)
print("prod =", prod)


def exp_dandc(base, p):
    from math import log2
    """Divide and Conquer implementation of exponentiation"""
    k = base #* renaming base to k for readability
    binP = bin(p)[2:]
    start=stop = int(log2(p))
    
    print("arr:", binP, "len:", len(binP), "last:", start)
    def exp_rec(summ, crt_pow, i):
        """ summ : contains the sum of the k^(2^i)
        crt_pow: the current power of k (should be equal to k^(2^i))
        bin: contains the binary representation of k (as an array)
        i : the current step
        stop: the max number of step i.e. stopping condition is "i >= stop" (stop := floor(log_2(p)))
        """
        if i < 0: return summ
        print(f"start - i = {start} - {i} = {start - i}" )
        print(f"bin[{i}]={binP[i]}", "check:", binP, f" k^(2^i) = {k}^(2^{(start-i)}) = {k}^{2**(start-i)} =", crt_pow)
        crt_pow = crt_pow * (crt_pow if (i != stop-1) else k)
        if binP[i] == '1': 
            summ += crt_pow
        print("summ:", summ, "crt_pow:", crt_pow)
        print("--------------------")
        return exp_rec(summ, crt_pow, i-1)

    out = exp_rec(0, k, start)

    if k % 2 != 0: out += 1
    return out     
    
def compare_exp():
    """Compare runtimes of the naive and D&C algorithms using matplotlib"""
    from time import time
    import matplotlib.pyplot as plt
    
    # TODO
    ...
    
# TODO: Uncomment to see comparison
# compare_exp()
