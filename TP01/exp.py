from time import time
import matplotlib.pyplot as plt
from random import randint
from math import log10

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
    plt.ylim(0, min(plot_f1[1:]))
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.plot(plot_x, plot_f1, '-k', label=f1Label, linewidth=1)
    plt.plot(plot_x, plot_f2, '-b', label=f2Label, linewidth=1.2)
    plt.legend()

def plot_solo(plot_x, plot_f, title: str, xlabel: str, ylabel: str, fLabel: str):
    """Plots two functions against each other.  
    - plot_x: the x-axis values
    - plot_f: the y-values of the function
    - title: the title of the plot
    - xlabel: the label of the x-axis
    - ylabel: the label of the y-axis
    - fLabel: the label of the function
    """
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.plot(plot_x, plot_f, '-b', label=fLabel, linewidth=1)
    plt.legend()

def exp_naive(base, p):
    """Naive implementation of exponentiation"""
    pr = 1
    for _ in range(p):
        pr *= base
    return pr
    # complexité theta(n*f) où f est la complexité de multiplier pr par base (au moins Omega(n)).

from timeit import timeit
#import timeit
def runtime(f, arg:tuple):
    from timeit import timeit
    """ Takes a function f and an argument arg, and returns the time (in ms) it takes to run f(arg)
    f: the function to be timed
    arg: the argument to pass to the function
    """
    #before = time()
    #!
    #! DELTA TIME IS TOO SHORT => ALWAYS GETS DEFAULTED TO 0
    #! => need to use library timeit
    #!
    num = 1000
    delta_time = timeit(lambda: f(*arg), number=num) * (1000/num)
    #after = time()
    #delta_time = (after*2000) - (before*2000)
    #print(before, after)
    #return (delta_time/2000)
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
    from math import log10
    from time import time
    import matplotlib.pyplot as plt
    args = [(2, i) for i in range(1000, 6000, 1000)]
    plot_x = [log10(x) for x in range(1000, 6000, 1000)]
    plot_y_naive = runtime_arr(exp_naive,  args)
    plot_y_dandc = runtime_arr(exp_dandc, args)
    title = "Runtime - naive_exp(2, x) VS dandc_exp(2, x)"
    xlabel, ylabel = "input size (magnitude i.e. nb of digit)", "runtime (ms)"
    print("x_values:", plot_x)
    print("pairs:", args)
    print("y_naive:", plot_y_naive)
    print("y_dandc", plot_y_dandc)
    plot_solo(plot_x, plot_y_naive, "Runtime naive", xlabel, ylabel, "naive")
    plot_solo(plot_x, plot_y_dandc, "Runtime D&C", xlabel, ylabel, "D&C")
    
    plotVS(plot_x, plot_y_naive, plot_y_dandc, "", xlabel, ylabel, "naive", "divide & conquer")

if __name__ == '__main__':
    compare_exp()
    """  args = [(2, i) for i in range(1000, 6000, 1000)]
    plot_x = list(range(1000, 6000, 1000))
    plot_y_naive = runtime_arr(exp_naive,  args)
    plot_y_dandc = runtime_arr(exp_dandc, args)
    print("x_values:", plot_x)
    print("pairs:", args)
    print("y_naive:", plot_y_naive)
    print("y_dandc", plot_y_dandc)

    plt.plot(plot_x, plot_y_naive, '-k', label="naive", linewidth=1)
    plt.plot(plot_x, plot_y_dandc, '-b', label="dandc", linewidth=1.2)

    print("plot") """
    #while(True):
        #pass