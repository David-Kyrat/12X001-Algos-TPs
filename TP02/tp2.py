########################### Exercise 1 ###########################
# NOTE: Each 'knapsack' method returns two lists: 
# selected weights and values (in order of selection).
# Two lists can be returned as a tuple (selected_w, selected_v).

# HINT: Check out python functions 'sorted()' and 'zip()' for nicer code.


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
    weights, values = [], []
    for el in knap:
        weights.append(el.w)
        values.append(el.v)
    return weights, values



def knapsack_a(weights, values, max_weight):
    """Adds available item with the highest value first"""
    items: list[El] = [El(w, v) for w, v in zip(weights, values)]
    return knapsack_upk(knapsack(items, max_weight, sorting_key=lambda el: el.v))


def knapsack_b(weights, values, max_weight):
    """Adds available item with the lowest weigth first"""
    items: list[El] = [El(w, v) for w, v in zip(weights, values)]
    return knapsack_upk(knapsack(items, max_weight, sorting_key=lambda el: el.w, highest=False))


def knapsack_c(weights, values, max_weight):
    """Adds available item with the highest (value / weight) ratio first"""
    items: list[El] = [El(w, v) for w, v in zip(weights, values)]
    return knapsack_upk(knapsack(items, max_weight, sorting_key=lambda el: el.v / el.w))



########################### Exercise 2 ###########################


# def compute_change(money, coin_set):
#     """Returns a list of coin values (in the coin set) that sums up to 'money'"""
#     if coin_set is None or money <= 0: return []
#     n = len(coin_set)
#     if n == 0: return []
#
#     def try_rec(i, left, acc):
#         """ Try recursively to put the biggest amount of the biggest coin into acc without "overflowing" 'money'  """
#         if i >= n or left <= 0: return acc
#         crt_coin = coin_set[i]
#         crt_amnt = int(left / crt_coin)  # how many coin of value coin_set[i] can we put at max ?
#
#         if crt_amnt <= 0: return try_rec(i + 1, left, acc)
#         else: return try_rec(i + 1, left - (crt_amnt * crt_coin), acc + crt_amnt * [crt_coin])
#
#     change = try_rec(0, money, [])
#     return change

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
    print("union:", tmp)
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
        # if (not S[u].issubset(S[v])) and (not S[v].issubset(S[u])):

        u_idx, v_idx = find_set(S, u), find_set(S, v)
        Su, Sv = S[u_idx], S[v_idx]
        print(f"find-set({u}): {Su}")
        print(f"find-set({v}): {Sv}")
        if Su != Sv:
            F += [(u, v)]
            print("(u, v) =", (u, v))
            print("F:", F)
            union(S, Su, Sv, u_idx)
            print("Sets:", S)
            print("-----------------")
    return F

if __name__ == "__main__":
    A = [[0, 1, 2], [1, 0, 10], [2, 10, 0]]

    B = [[0, 2, 1], [2, 0, 10], [1, 10, 0]]

    C = [[0, 10, 2], [10, 0, 1], [2, 1, 0]]

    kruskal(A)
