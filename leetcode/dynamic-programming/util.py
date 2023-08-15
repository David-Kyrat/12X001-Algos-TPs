import matplotlib.pyplot as plt
import numpy as np
from prettytable import PrettyTable
from typing import List

def plotVS(plot_x, plot_f1, plot_f2, title: str = None, xlabel: str = None, ylabel: str = None, f1Label: str = None, f2Label: str = None):
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
    plt.grid()
    if title: plt.title(title)
    m1, m2, gap = min(plot_f2), max(plot_f1), 0.2
    plt.ylim(m1, m2 - gap * m2)
    if xlabel: plt.xlabel(xlabel)
    if ylabel: plt.ylabel(ylabel)
    plt.xticks(plot_x)
    if f1Label:  plt.plot(plot_x, plot_f1, '-k', label=f1Label, linewidth=1)
    else: plt.plot(plot_x, plot_f1, '-k', linewidth=1)
    
    if f2Label: plt.plot(plot_x, plot_f2, '-r', label=f2Label, linewidth=1)
    else: plt.plot(plot_x, plot_f2, '-r', linewidth=1)
    
    #plt.legend(prop={'size': 5})
    #plt.legend(fontsize=7)
    plt.legend()
    plt.show()

def plot_solo(plot_x, plot_f, title: str = None, xlabel: str = None, ylabel: str = None, fLabel: str = None):
    """Plots a single function
    - plot_x: the x-axis values
    - plot_f: the y-values of the function
    - title: the title of the plot
    - xlabel: the label of the x-axis
    - ylabel: the label of the y-axis
    - fLabel: the label of the function
    """
    #plt.tight_layout(pad=5)
    fig = plt.figure()
    if title: plt.title(title)
    plt.grid()
    if xlabel: plt.xlabel(xlabel)
    if ylabel: plt.ylabel(ylabel)
    M, gap = max(plot_f), 0.25
    
    plt.xticks(plot_x)
    #plt.ylim(0, M + gap*M)
    plt.yticks(np.linspace(0, M, 27))
    if fLabel:
        plt.plot(plot_x, plot_f, '-b', label=fLabel, linewidth=1)
    else:
        plt.plot(plot_x, plot_f, '-b')
    #  plt.legend(prop={'size': 5})
    #  plt.legend(fontsize=7)
    fig.set_figheight(7)
    plt.legend()
    print("\nshowing plot\n")
    plt.show()
    #fig.show()
    #fig.tight_layout()


def mprint(matrix: List[List], cns: str | List[int] = ""):
    p = PrettyTable()
    for i, row in enumerate(matrix):
        p.add_row([f"{i}:", *(row or [""] * len(cns))])
    print("_________________")
    print("   ", cns)
    print(p.get_string(header=False, border=False))
    print("-----------------")

def get_sol(filled_mat, goal: int, coin_set: List[int]) -> List[int]:
    """takes filled matrix of solution for the coins problem
    where `S` in [0, goal] and return the array of coined used"""
    amounts = filled_mat[goal - 1]
    out = []
    for idx, amount in enumerate(amounts):
        # appends `amount` times `coin_set[idx]` to `out`
        out.extend(coin_set[idx] for _ in range(amount))
    return out



