import numpy as np
import numba
from numba import njit, jit, prange


def f(a, b): return a + b


@njit(parallel=True)
def go_fastp(a):  # Function is compiled to machine code when called the first time
    trace = 0.0
    # assuming square input matrix
    for i in range(a.shape[0]):   # Numba likes loops
        trace += np.tanh(a[i, i])  # Numba likes NumPy functions
    return a + trace  # Numba likes NumPy broadcasting


@njit
def go_fast(a):  # Function is compiled to machine code when called the first time
    trace = 0.0
    # assuming square input matrix
    for i in range(a.shape[0]):   # Numba likes loops
        trace += np.tanh(a[i, i])  # Numba likes NumPy functions
    return a + trace  # Numba likes NumPy broadcasting


def go_numpy(a):
    return a + np.tanh(np.diagonal(a)).sum()


@jit
def go_lessfast(a):
    trace = 0.0
    # assuming square input matrix
    for i in range(a.shape[0]):   # Numba likes loops
        trace += np.tanh(a[i, i])  # Numba likes NumPy functions
    return a + trace  # Numba likes NumPy broadcasting


@jit(parallel=True)
def go_par(a):
    trace = 0.0
    for i in range(a.shape[0]):
        trace += np.tanh(a[i,i])
    return a + trace