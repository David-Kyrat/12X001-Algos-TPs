from time import time
import matplotlib.pyplot as plt
from random import randint


def plotVS(plot_x, plot_f1, plot_f2, title: str, xlabel: str, ylabel: str, f1Label: str, f2Label: str):
    """Plots two functions against each other.  
    - plot_x: the x-axis values
    - plot_f1: the y-values of the first function
    - plot_f2: the y-values of the second function
    - title: the title of the plot
    - xlabel: the label of the x-axis
    - ylabel: the label of the y-axis
    - f1Label: the label of the first function
    - f2Label: the label of the second function
    """
    plt.title(title)
    #plt.ylim(np.min(plot_y) - 0.1, np.max(plot_y) + 0.1)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.plot(plot_x, plot_f1, '-k', label=f1Label, linewidth=1)
    plt.plot(plot_x, ploty_f2, '-b', label=f2Label, linewidth=1.2)
    plt.legend()

def exp_naive(base, p):
    """Naive implementation of exponentiation"""
    pr = 1
    for _ in range(p):
        pr *= base
    return pr
    # complexité theta(n*f) où f est la complexité de multiplier pr par base (au moins Omega(n)).


def runtime(f, arg):
    """ Takes a function f and an argument arg, and returns the time it takes to run f(arg)
    f: the function to be timed
    arg: the argument to pass to the function
    """
    before = time()
    out = f(arg)
    after = time()
    delta_time = after - before
    return delta_time

def runtime_arr(f, argArray):
    return [runtime(f, arg) for arg in argArray]

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
        crt_pow = crt_pow * crt_pow
        if binP[i] == '1': prod *= crt_pow
        return exp_rec(prod, crt_pow, i+1)

    prod0, pow_0 = 1, base
    if (binP[0] == '1'):
        prod0 = base
    # if P is odd then we have to multiply by base at the beginning => hence why we start our product at base
    return exp_rec(prod0, pow_0, i0)


def compare_exp():
    """Compare runtimes of the naive and D&C algorithms using matplotlib"""
    from time import time
    import matplotlib.pyplot as plt
    plot_x = list(range(1000, 6000, 1000))
    plot_y_naive = runtime_arr(exp_naive,  plot_x)
    plot_y_dandc = runtime_arr(exp_dandc, plot_x)
    plotVS(plot_x, plot_y_naive, plot_y_dandc, "Runtime - naive_exp VS dandc_exp", "input size", "runtime", "naive", "divide & conquer")

if __name__ == '__main__':
    compare_exp()