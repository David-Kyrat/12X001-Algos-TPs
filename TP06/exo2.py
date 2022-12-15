from copy import deepcopy
from itertools import zip_longest
from multiprocessing.sharedctypes import Value


class El:
    """A class representing an element of the knapsack problem.
        It has a weight `w`, a value `v` and a ratio `r`."""
    
    def __init__(self, idx:tuple[list[int], list[int]], weight:int, value:int):
        """Constructor for El instances.

        Parameters
        ----------
        @ `index` - (int), index of the element in the original list
        @ `weight` - (int), weight of the element
        @ `value` - (int), value of the element
        """
        self.w: int = weight
        self.v: int = value
        self.r: float = value / weight if weight != 0 else 0
        self.idxs:tuple[list[int], list[int]] = idx
        
    def __repr__(self):
        return f"(w={self.w:2d}, v={self.v}, r={self.r}, {self.idxs})"
    def get(self, i): return [] if i >= len(self.idxs) else self.idxs[i]
    # useful because we're not going to store a solution as a list but instead as one element that will contain the sum of each values and weight and the list of indexes
    def __add__(self, other): return El((self.get(0) + other.get(0), self.get(1) + other.get(1)), self.w + other.w, self.v + other.v)

    def __eq__(self, __o: object) -> bool:
        if not isinstance(__o, El): return False
        return self.v == __o.v and self.w == __o.w

    def __lt__(self, __o: object) -> bool:
        """ El_1 < El_2 if and only if El_2 has a greater value than El_1.
            i.e. the max of a list of El is the one with the greatest value"""
        if not isinstance(__o, El): raise ValueError("Cannot compare El with other types")
        return self.v < __o.v
    
    # to be able to add an El in a set
    def __hash__(self) -> int: return hash((self.w, self.v))
    
#def sort_and_createEls(weights, values):
    """Sorts the weights and values in decreasing order of the ratio (value / weight).
    Returns a list of El instances"""
    # We sort the values and the corresponding weights in decreasing order
    

def greedy_knapsack(items: list[El], W) -> El:
    """:return: Solution of Knapsack problem for set of item "items" and max weight W, by selecting first
        all the items with the highest <characteristic defined by sorting key>
        NB: if "highest" is set to false then select the lowest ... items first  """
    if items is None: return None
    n, w, i = len(items), 0, 0
    #bag: list[El] = []
    bag = El([], 0, 0)
    if n == 0: return bag
    if n == 1: return bag if items[0].w > W else items[0]
    items.sort(key=lambda el: el.r, reverse=True)
    #res:El = None
    
    def try_rec(k, w, n):
        nonlocal bag
        if k >= n: return k, w, n
        crt = items[k]
        if crt.w + w > W: return try_rec(k + 1, w, n)
        else:  
            #bag.append(items.pop(k))
            # we're not going to store a solution as a list but instead as one element that will contain the sum of each values and weight and the list of indexes
            if bag is None: bag = items.pop(k)
            else: bag += items.pop(k) 
            #bag += items.pop(k)
            return k, w + crt.w, n - 1

    while w < W and i < n:
        i, w, n = try_rec(i, w, n)
    return bag

########################### Exercise 2 ###########################
def approx_knapsack(weights, values, max_weight) -> tuple[list[int], list[int]]:
    """Returns an approximation for the (0-1) knapsack problem.
    The approximation is at most 2-times worse than the optimal solution"""
    # For the approximation algorithm we must have monotically decreasing indices for the values (i.e. v1 >= v2 >= ... >= vn)
    # We sort the values and the corresponding weights in decreasing order
    if max_weight <= 0: return [], []
    E: list[El] = [El(([weights[i]], [values[i]]), weights[i], values[i]) for i in range(len(weights))]
    E.sort(key=lambda e: e.v)
    R = set()
    for j in range(len(E)):
        Ij:list[El] = E[j:]
        # we're not going to store a solution as a list but instead as one element that will contain the sum of each values and weight and the list of indexes
        Rj:El = greedy_knapsack(deepcopy(Ij), max_weight)
        R.add(Rj)
        
        def pr():
            print("Ij", "\n".join([str(x) for x in Ij]), "\n")
            print("Rj", Rj, "\n")
            print("R","\n".join([str(x) for x in R]), "\n")
        #pr()
        if 2 == 3: print("lul")
    tmp = max(R).idxs
    #out=[weights[i] for i in tmp][::-1], [values[i] for i in tmp][::-1]
    return tmp[0][::-1], tmp[1][::-1]
    #return max(R).idxs

def test_sol(weights, values, sol: tuple[list[int], list[int]]):
    #sol_w = sum([weights[i] for i in sol[0]])
    #sol_v = sum([values[i] for i in sol[1]])
    tmp = list(zip(sol[0], sol[1]))
    return tmp, (sum(sol[0]), sum(sol[1]))
 
if __name__ == '__main__':
    w, v = [12, 10, 7, 3, 1], [9, 5, 4, 2, 2]
    """ print("Res1", approx_knapsack(w, v, 0)) # == ([], [])
    print("Res2",approx_knapsack(w, v, 10)) # == ([7, 1], [4, 2])
    print("Res3",approx_knapsack(w, v, 12)) # == ([12], [9]) """
    print("Res4",approx_knapsack(w, v, 22)) # == ([12, 1, 3], [9, 2, 2])
    exp4 = ([12, 1, 3], [9, 2, 2])
    exp4 = set(zip(exp4[0], exp4[1]))
    print("Res5",approx_knapsack(w, v, 29)) # == ([12, 1, 3, 7], [9, 2, 2, 4])
    