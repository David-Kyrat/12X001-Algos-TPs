########################### Exercise 1 ###########################
# NOTE: Each 'knapsack' method returns two lists: 
# selected weights and values (in order of selection).
# Two lists can be returned as a tuple (selected_w, selected_v).

# HINT: Check out python functions 'sorted()' and 'zip()' for nicer code.
import matplotlib.pyplot as plt



class El:
    def __init__(self, weight, value):
        self.w = weight
        self.v = value

    def __repr__(self): return f"({self.w}, {self.v})"

    def __add__(self, other): return El(self.w + other.w, self.v + other.v)


def knapsack(items: list[El], W, sorting_key, highest: bool = True):
    """:return: Solution of Knapsack problem for set of item "items" and max weight W, by selecting first
        all the items with the highest <characteristic defined by sorting key>
        NB: if "highest" is set to false then select the lowest ... items first  """
    if items is None: return None
    n, w, i, bag = len(items), 0, 0, []
    if n == 0: return bag
    if n == 1: return bag if items[0].w > W else [items[0]]
    items = sorted(items, key=sorting_key, reverse=highest)

    def try_rec(k, w, n):
        if k >= n: return k, w, n
        crt = items[k]
        if crt.w + w > W: return try_rec(k + 1, w, n)
        else:
            bag.append(items.pop(k))
            return k, w + crt.w, n - 1

    while w < W and i < n:
        i, w, n = try_rec(i, w, n)
    return bag

def knapsack_upk(knap: list[El]):
    """ :return: Unpacked list of El. i.e. creates 2 separated list of weight, value from the given list of El."""
    weights, values = [], []
    for el in knap:
        weights.append(el.w)
        values.append(el.v)
    return weights, values


def knapsack_a(weights, values, max_weight):
    """Adds available item with the highest value first"""
    items: list[El] = [El(w, v) for w, v in zip(weights, values)]
    return (knapsack(items, max_weight, sorting_key=lambda el: el.v))


def knapsack_b(weights, values, max_weight):
    """Adds available item with the lowest weigth first"""
    items: list[El] = [El(w, v) for w, v in zip(weights, values)]
    return (knapsack(items, max_weight, sorting_key=lambda el: el.w, highest=False))


def knapsack_c(weights, values, max_weight):
    """Adds available item with the highest (value / weight) ratio first"""
    items: list[El] = [El(w, v) for w, v in zip(weights, values)]
    return (knapsack(items, max_weight, sorting_key=lambda el: el.v / el.w))



########################### Exercise 2 ###########################


def compute_change(money, coin_set):
    """Returns a list of coin values (in the coin set) that sums up to 'money'"""
    if coin_set is None or money <= 0: return []
    n = len(coin_set)
    if n == 0: return []

    def try_rec(left, i, acc):
        """ left := money left to partition into coins, i:= current coin index, acc:= accumulator containing the solution
            Try recursively to put the biggest amount of the biggest coin into acc without "overflowing" 'money'  """
        if i >= n or left <= 0: return acc

        if left - coin_set[i] >= 0: return try_rec(left - coin_set[i], i, acc + [coin_set[i]])
        else: return try_rec(left, i + 1, acc)

    change = try_rec(money, 0, [])
    return change

########################### Exercise 3 ###########################


def find_set(S, u):
    """:return: Index of 1st set in 'S' that contains 'u' """
    for i in range(len(S)):
        if u in S[i]: return i

def union(S, Su, Sv, u_idx):
    """ Replace S[u_idx] by Su.union(Sv) and remove Sv from list of sets S """
    tmp = Su.union(Sv)
    S[u_idx] = tmp
    S.remove(Sv)

def kruskal(A):
    """Given A, a square matrix (list of lists), returns a list of edges that compose the MST"""
    # NOTE: A weight of 0 means that there is no edge between nodes, and it should not be taken into the MST
    n = len(A)
    if n <= 0: return []
    if n == 1: return [(0, 0)]
    S, F, E = [{i} for i in range(n)], [], []

    for i in range(n):
        for j in range(i + 1):
            if A[i][j] != 0: E.append((i, j, A[i][j]))
    # visits each edge only once => O(|E|)
    E = sorted(E, key=lambda edge: edge[2])  # sorted according to weight in increasing order
    for e in E:
        u, v = e[1], e[0]
        u_idx, v_idx = find_set(S, u), find_set(S, v)
        Su, Sv = S[u_idx], S[v_idx]
        if Su != Sv:
            F += [(u, v)]
            union(S, Su, Sv, u_idx)
    return F

def sum_els(items: list[El]) -> El :
    """:return: new El created as the sum of each element in given list """
    tmp = El(0, 0)
    for el in items: tmp += el
    return tmp

def plotVS(plot_x, plot_f1, plot_f2, plot_f3, title: str, xlabel: str, ylabel: str, f1Label: str, f2Label: str, f3Label:str):
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
    # m1, m2, gap = min(plot_f2), min(plot_f1[1:]), 0.2
    # plt.ylim(m1 - gap * m1, m2 + gap * m2)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.plot(plot_x, plot_f1, '-k', label=f1Label, linewidth=1)
    plt.plot(plot_x, plot_f2, '-b', label=f2Label, linewidth=1)
    plt.plot(plot_x, plot_f3, '-r', label=f3Label)
    #plt.legend(prop={'size': 5})
    #plt.legend(fontsize=7)
    plt.legend()
    plt.show()


if __name__ == '__main__':
    print("")
    # w, v, W = [10, 3, 7, 12, 1], [5, 2, 4, 9, 2], 22
    import random
    n = 200
    def getw(n):
        return [random.randint(1, 200) for i in range(n)]

    w = [random.randint(1, 200) for i in range(n)]
    v = [random.randint(1, 200) for i in range(n)]
    W = 1000
    #x_plot = [] #f1_plot = f2_plot = f3_plot = []
    test_range = range(50, 1001, 50)
    x_plot = list(test_range)
    f1_plot = [sum_els(knapsack_a(getw(n), getw(n), W)).v for n in test_range]
    f2_plot = [sum_els(knapsack_b(getw(n), getw(n), W)).v for n in test_range]
    f3_plot = [sum_els(knapsack_c(getw(n), getw(n), W)).v for n in test_range]

    xLabel = "size of item's list"
    yLabel = "Computed Max Value"
    f1Label = "Highest Values 1st"
    f2Label = "Lowest Weight 1st"
    f3Label = "Highest val/weight 1st"
    plotVS(x_plot, f1_plot, f2_plot, f3_plot, "Optimality of KNAPSACK (random elements, W=1000)", xLabel, yLabel, f1Label, f2Label, f3Label)

