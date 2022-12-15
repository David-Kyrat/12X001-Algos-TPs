from copy import deepcopy

class El:
    """A class representing an element of the knapsack problem.
        It has a weight `w`, a value `v` and a ratio `r`."""
    
    def __init__(self, wv_list, weight:int, value:int):
        """Constructor for El instances.

        Parameters
        ----------
        @ `wv_list` - tuple of list of weight & values, containing those that sums up to weight and value
        @ `weight` - (int), weight of the element
        @ `value` - (int), value of the element
        """
        self.w: int = weight
        self.v: int = value
        self.r: float = value / weight if weight != 0 else 0
        self.wv_list = wv_list
        
    def __repr__(self):
        return f"(w={self.w:2d}, v={self.v}, r={self.r}, {self.wv_list})"
    def get(self, i): return [] if i >= len(self.wv_list) else self.wv_list[i]
    # useful because we're not going to store a solution as a list but instead as one element that will contain the sum of each values and weight and the list of indexes
    def __add__(self, other): return El((self.get(0) + other.get(0), self.get(1) + other.get(1)), self.w + other.w, self.v + other.v)
    
def greedy_knapsack(items: list, W, b0:El=El([],0,0)) -> El:
    """:return: Solution of Knapsack problem for set of item "items" and max weight W, by selecting first
        all the items with the highest <characteristic defined by sorting key>
        NB: if "highest" is set to false then select the lowest ... items first  """
    if items is None or W <= 0: return b0
    
    bag, n, i = b0, len(items), 0 # its convenient to be able to pass an initial bag
    if n == 0: return bag
    if n == 1: return bag if items[0].w > W else items[0]
    items.sort(key=lambda el: el.r, reverse=True)
    
    while bag.w <= W and i < n : 
        crt:El = items[i]
        if bag.w + crt.w <= W: bag += crt
        i +=1
    
    return bag

########################### Exercise 2 ###########################
def approx_knapsack(weights, values, max_weight) -> tuple:
    """Returns an approximation for the (0-1) knapsack problem.
    The approximation is at most 2-times worse than the optimal solution"""
    # For the approximation algorithm we must have monotically decreasing indices for the values (i.e. v1 >= v2 >= ... >= vn)
    # We sort the values and the corresponding weights in decreasing order
    if max_weight <= 0: return [], []
    E: list[El] = [El(([weights[i]], [values[i]]), weights[i], values[i]) for i in range(len(weights))]
    R = []
    for j, el in enumerate(E):
        crt:el = el if (el.w <= max_weight) else El([], 0, 0)
        Ij:list[El] = E[j+1:]
        # we're not going to store a solution as a list but instead as one element that will contain the sum of each values and weight and the list of each summed values&weights
        Rj:El = greedy_knapsack(Ij, max_weight, crt)        
        R.append(Rj)
    
    return max(R, key=lambda x: x.v).idxs # takes max w.r.t. values

if __name__ == '__main__':
    w, v = [12, 10, 7, 3, 1], [9, 5, 4, 2, 2]
    print("Res1", approx_knapsack(w, v, 0)) # == ([], [])
    print("Res2",approx_knapsack(w, v, 10)) # == ([7, 1], [4, 2])
    print("Res3",approx_knapsack(w, v, 12)) # == ([12], [9])
    print("Res4",approx_knapsack(w, v, 22)) # == ([12, 1, 3], [9, 2, 2])
    
    
    print("Res5",approx_knapsack(w, v, 29)) # == ([12, 1, 3, 7], [9, 2, 2, 4])