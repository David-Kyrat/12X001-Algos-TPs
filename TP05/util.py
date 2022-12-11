from timeit import timeit
import matplotlib.pyplot as plt
from time import time, time_ns


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
    plt.grid()
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
    plt.tight_layout()
    plt.show()


def plot_solo(plot_x, plot_f, title: str, xlabel: str, ylabel: str, fLabel: str, xticks=None, yticks=None):
    """Plots a single function

    Parameters
    ----------
    @ `plot_x` - x-axis values
    @ `plot_f` - y-axis values (i.e. values of the function)
    @ `title`  - Title of the plot
    @ `xlabel` - Label of the x-axis
    @ `ylabel` - Label of the y-axis
    @ `fLabel` - Label of the function
    @ `xticks` (optional) - list of ticks to display on x-axis, (default: None)
    @ `yticks` (optional) - list of ticks to display on y-axis, (default: None)
    """

    #plt.tight_layout(pad=5)
    fig = plt.figure()
    plt.title(title)
    plt.grid()
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    if xticks is not None:
        plt.xticks(xticks)
    else: 
        mx, Mx, gapx = min(plot_x), max(plot_x), 0.25
        plt.xlim(mx - gapx * mx, Mx + gapx * Mx)
    if yticks is not None:
        plt.yticks(yticks)
    else:
        my, My, gapy = min(plot_f), max(plot_f), 0.25
        plt.ylim(my - gapy, My + gapy * My)
    plt.plot(plot_x, plot_f, '-b', label=fLabel, linewidth=1)
    #plt.legend(prop={'size': 5})
    #plt.legend(fontsize=7)
    fig.set_figheight(12)
    fig.set_figwidth(9)
    plt.tight_layout(pad=2.5)
    plt.legend()
    plt.show()


def runtime(f, args, unpack: bool, number: int = 1):
    '''It takes a function f and an argument arg, and returns the time (in ns) it takes to run f(arg)
    
    Parameters
    ----------
    @ f - the function to be timed
    @ args - the arguments to pass to the function
    @ unpack - bool, optional if True, the function will unpack the arguments 
    @ number - int, optional, the number of times to run the function
    before passing them to the function.
    
    Returns
    -------
        The time it takes to run the function f with the arguments args'''
    
    delta_time = timeit(lambda : f(*args) if (unpack) else f(args), number=number) #* 1.000    
    return delta_time

def runtime_arr(f, argArray, unpack: bool, number:int = 1): 
    """ See "runtime()" function above for explaination """
    return [runtime(f, arg, unpack, number) for arg in argArray]
