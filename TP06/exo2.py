########################### Exercise 2 ###########################
class El:
    """A class representing an element of the knapsack problem.
        It has a weight `w` , a value `v`, a ratio `r` and pair of weight-list, value-list, `wv_list`."""
    
    def __init__(self, weight:int, value:int, wv_list: tuple[list[int], list[int]] | None = None):
        """Constructor for El instances.

        Parameters
        ----------
        @ `weight` - (int), weight of the element
        @ `value` - (int), value of the element
        @ (optional) `wv_list` - tuple of list of weight-list & value-list, containing those that sums up to
                            ``weight`` and ``value`` i.e. ``sum(wv_list[0]) == weight`` and 
                             ``sum(wv_list[1]) == value`` if not given, default to ``([weight], [value])``"""
        self.w: int = weight
        self.v: int = value
        self.r: float = value / weight if weight != 0 else 0
        self.wv_list = wv_list if wv_list is not None else ([weight], [value])
        
    def __repr__(self): return f"(w={self.w:2d}, v={self.v}, r={self.r}, {self.wv_list})"

    def get(self, i): return [] if i >= len(self.wv_list) else self.wv_list[i]
    
    # useful because we're not going to store a solution as a list but instead as one element that will contain the sum of each values and weight and the list of indexes
    def __add__(self, other): return El(self.w + other.w, self.v + other.v, (self.get(0) + other.get(0), self.get(1) + other.get(1)))

    
def greedy_knapsack(items: list, W, b0: El = El(0,0)) -> El:
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
        # we're not going to store a solution as a list but instead as one element that will contain the sum of each values and weight and the list of each summed values&weights
        if bag.w + crt.w <= W: bag += crt
        i +=1
    
    return bag


def approx_knapsack(weights, values, max_weight) -> tuple:
    """Returns an approximation for the (0-1) knapsack problem.
    The approximation is at most 2-times worse than the optimal solution"""
    # For the approximation algorithm we must have monotically decreasing indices for the values (i.e. v1 >= v2 >= ... >= vn)
    # We sort the values and the corresponding weights in decreasing order
    if max_weight <= 0 or values is None or values is None : return [], []
    E: list[El] = [El(*wv_pair) for wv_pair in zip(weights, values)]
    
    R = [greedy_knapsack( E[j+1:], max_weight, (el if (el.w <= max_weight) else El(0, 0))) for j, el in enumerate(E)]
    
    return max(R, key=lambda x: x.v).wv_list # takes max w.r.t. values
