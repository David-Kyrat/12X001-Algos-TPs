import matplotlib.pyplot as plt
from time import time


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

    # plt.subplot(3, 1, subp_idx)
    # plt.tight_layout()
    plt.title(title)
    m1, m2, gap = min(plot_f2), max(plot_f1), 0.2
    plt.ylim(m1, m2 - gap * m2)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(plot_x)
    plt.plot(plot_x, plot_f1, '-k', label=f1Label, linewidth=1)
    plt.plot(plot_x, plot_f2, '-r', label=f2Label, linewidth=3)
    #plt.legend(prop={'size': 5})
    #plt.legend(fontsize=7)
    plt.legend()
    plt.show()

def plot_solo(plot_x, plot_f, title: str, xlabel: str, ylabel: str, fLabel: str):
    """Plots a single function
    - plot_x: the x-axis values
    - plot_f: the y-values of the function
    - title: the title of the plot
    - xlabel: the label of the x-axis
    - ylabel: the label of the y-axis
    - fLabel: the label of the function
    """
    #plt.tight_layout(pad=5)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    M, gap = max(plot_f), 0.35
    
    plt.ylim(0, M + gap*M)
    plt.plot(plot_x, plot_f, '-b', label=fLabel, linewidth=1)
    #  plt.legend(prop={'size': 5})
    #  plt.legend(fontsize=7)
    plt.legend()


def runtime(f, args, unpack: bool):
    '''It takes a function f and an argument arg, and returns the time (in ns) it takes to run f(arg)
    
    Parameters
    ----------
    @ f - the function to be timed
    @ args - the arguments to pass to the function
    @ unpack - bool, optional if True, the function will unpack the arguments 
    before passing them to the function.
    
    Returns
    -------
        The time it takes to run the function f with the arguments args'''
    before = time()
    f(*args) if (unpack) else f(args)
    delta_time = time() - before
    return delta_time

def runtime_arr(f, argArray, unpack: bool): 
    """ See "runtime()" function above for explaination """
    return [runtime(f, arg, unpack) for arg in argArray]