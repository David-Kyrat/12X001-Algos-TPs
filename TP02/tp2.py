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

    def unpk(self):
        """:return: (self.w, self.v). i.e. unpack the El"""
        return self.w, self.v

def sum_els(items: list[El]) -> El :
    """:return: new El created as the sum of each element in given list """
    tmp = El(0, 0)
    for el in items: tmp += el
    return tmp

def knapsack(items: list[El], W, sorting_key, highest: bool = True):
    """:return: Solution of Knapsack problem for set of item "items" and max weight W, by selecting first
        all the items with the highest <characteristic defined by sorting key>
        NB: if "highest" is set to false then select the lowest ... items first  """
    if items is None: return None
    n, w, i, bag = len(items), 0, 0, []
    if n == 0: return bag
    if n == 1: return bag if items[0].w > W else [items[0]]

    items = sorted(items, key=sorting_key, reverse=highest)
    print("Items:", items)

    def try_rec(k, w, n):
        print("k =", k, " n =", n, " w =", w)
        if k >= n: return k, w, n
        crt = items[k]
        print("items[k] =", crt)

        if crt.w + w > W:
            print((crt.w + w), ">=", W, "\n--")
            return try_rec(k + 1, w, n)
        else:
            bag.append(items.pop(k))
            print("adding", crt, "to knapsack,", "w =", w)
            print("list:", items)
            print("--------------")
            return k, w + crt.w, n - 1

    while w < W and i < n:
        i, w, n = try_rec(i, w, n)

    print("\n\n")
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


def print_knapsack_result(knap: El):
    # print("Result Knapsack", knap)
    # value_sum = sum([el.v for el in knap])
    # weight_sum = sum([el.w for el in knap])
    print("\t", "Total weight:", knap.w, "  Total value:", knap.v)
    print("______________________________________________________________\n")



########################### Exercise 2 ###########################


def compute_change(money, coin_set):
    """Returns a list of coin values (in the coin set) that sums up to 'money'"""
    # TODO
    ...



########################### Exercise 3 ###########################


def kruskal(A):
    """Given A a square matrix (list of lists), returns a list of edges that compose the MST"""
    # NOTE: A weight of 0 means that there is no edge between nodes and it should not be taken into the MST
    
    # TODO
    ...

if __name__ == "__main__":
    print("")
    weights, values, max_weight = [10, 3, 7, 12, 1], [5, 2, 4, 9, 2], 25
    print_knapsack_result(knapsack_a(weights, values, max_weight))
    print_knapsack_result(knapsack_b(weights, values, max_weight))
    print_knapsack_result(knapsack_c(weights, values, max_weight))


