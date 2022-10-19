########################### Exercise 1 ###########################
# NOTE: Each 'knapsack' method returns two lists: 
# selected weights and values (in order of selection).
# Two lists can be returned as a tuple (selected_w, selected_v).

# HINT: Check out python functions 'sorted()' and 'zip()' for nicer code.


def knapsack_a(weights, values, max_weight):
    """Adds available item with the highest value first"""
    # TODO
    ...
    
def knapsack_b(weights, values, max_weight):
    """Adds available item with the lowest weigth first"""
    # TODO
    ...
    
    
def knapsack_c(weights, values, max_weight):
    """Adds available item with the highest (value / weight) ratio first"""
    # TODO
    ...
            


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
