########################### Exercise 3 ###########################
from fifteen_puzzle import M, M_ALL, mv, UP, RIGHT, DOWN, LEFT

#
#* Lets call ``a_k`` the index of our current location after the k-th move, we want to move from the starting point ``a0`` to the arrival/destination ``b = a_{c(x_0)}``  (``x_0`` is the root of the tree of all possible moves/outcome).
#* We'll use the same cost function approximation ``ĉ(x) = h(x) + g(x)`` as in fifteen_puzzle .
# 

class Node: 
    """Node of the moves tree. Each attribute is detailled below."""
    
    def __init__(self, move: M | None, parent):
        """Constructor of the Node class.

        Parameters
        ----------
        @ `move`     - move that led to this node from its parent
        @ `parent`   - parent of this node (Can be None, If it is, then this node is the root of the game tree, and tx has to be given)
        
        Other attributes
        ---------
        @ `ak`      - ``tuple[int, int]``, index of this node in the domain (i.e. current location)
        @ `b`       - ``tuple[int, int]``, index of the destination (computed from ``parent``, to construct root node see ``init_root``)
        @ `path`    - ``list[tuple[int, int]]``, list of indexes from the root to this node (i.e. ``path = [a0, a1, ..., ak]``)
        @ `depth`   - ``int``, depth of this node in the moves tree (i.e. number of moves: ``h(this) = parent.depth + 1``)
        @ `cost`    - ``int``, cost (i.e. ``ĉ(this) = h(this) + g(this)``) where ``g(this) = ||b-a||_1`` (i.e. distance (norm ``L1``) between the current location and the destination)
        @ `move`    - ``M``, last move that led to this node (i.e. ``a_k = move + a_k-1`` (``a_k-1 = parent.a_k``))
        """
        if parent is None: return # root node
        self.ak: tuple[int, int] = move + parent.ak
        self.b: tuple[int, int] = parent.b
        self.depth : int = parent.depth + 1
        self.path: list[tuple[int, int]] = parent.path + [self.ak]
        self.cost: int = Node.c_hat(self)
        self.move = move
        
        #self.cost, self.gx = update_misplaced_compute_cost(self, parent.misplaced, domain, self.moves)

    @classmethod
    def init_root(cls, a: tuple[int, int], b: tuple[int, int]):
        """ Constructor of root nodes, ``a`` is the starting point, `b` is the destination. """
        newnode = Node(None, None)
        newnode.depth = 0
        newnode.ak = a
        newnode.b = b
        newnode.cost = Node.d(a, b)
        newnode.path = [a]
        newnode.move = None
        return newnode

    @classmethod
    def d(cls, x1, x2) -> int:
        """Returns the distance d(this, x) = ||a_k - x||_1 (i.e. norm ``L1``) between the current location and x"""

        if isinstance(x1, Node) and isinstance(x2, Node): return x1.__d__(x2)
        if isinstance(x1, Node): return dist(x1.ak, x2)
        if isinstance(x2, Node): return dist(x1, x2.ak)
        return dist(x1, x2)

    def __d__(self, node)->int:
        """ same as ``d()`` but does not performe type check """
        return abs(self.ak[0] - node.ak[0]) + abs(self.ak[1] - node.ak[1])

   
    @classmethod
    def c_hat(cls, node) -> int:
        """Returns the cost of a node (i.e. ``ĉ(node) = h(node) + g(node)``)"""
        return node.depth + Node.d(node, node.b)

    def __repr__(self):
        """Representation of a node as a string."""
        return f"Node(ĉ={self.cost}, ak={self.ak}, g={self.cost}, h={self.depth}, b={self.b}, path={self.path})"


def dist(p1: tuple[int, int], p2: tuple[int, int]):
    """Conveniance function to compute the distance (L1 norm) between two points (i.e. ``||p1-p2||_1``)

    Parameters
    ----------
    @ `p1` - first pair of coordinates
    @ `p2` - second pair of coordinates

    Returns
    ----------
        distance between p1 and p2, ``||p1-p2||_1``"""
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def get(matrix: list[list[int]], index: tuple[int, int]) -> int:
    """ Allow using tuple to access elements in a matrix. (Does not check for bounds correctness)"""
    return matrix[index[0]][index[1]]


def children_moves(domain: list[list[int]], node: Node, n:int, m:int) -> set[M]:
    """ Return a set of all possible moves for the children of the given node.

    Parameters
    ----------
    @ `node` - Node to compute the cost of
    @ `n`    - number of rows in the domain
    @ `m`    - number of columns in the domain

    Returns
    -------
        set of all possible moves from a given node. (avoiding obstacles and out of bounds errors)"""
    moves: set[M] = M_ALL.copy()
    if node.move is not None: moves.remove(node.move.inv()) # remove inverse of last move to avoid cycles in the game "tree"    

    # now remove moves that would lead to an out of bounds error, like we did in fifteen_puzzle.py

    if node.ak[0] == 0: moves.discard(M.UP)
    if node.ak[0] == n-1: moves.discard(M.DOWN)
    
    # idem, if column of current white square (16) is on a side (i.e. if can't go LEFT or RIGHT)        
    if node.ak[1] == 0: moves.discard(M.LEFT)
    if node.ak[1] == m-1: moves.discard(M.RIGHT)

    rm: set[M] = set()

    # Remove all obstacles from the set of possible moves
    for m in moves:
        if get(domain, m + node.ak) == 1: rm.add(m) 

    return moves.difference(rm)


def P(enode: Node):
    """ Return true if and only if enode is a goal node.  ``enode`` has arrived 
    at its destination ``b`` if and only if its distance to ``b`` is null (in the matical sense) 
    i.e. if ``||enode.ak - b||_1 = 0`` i.e. ``enode.ak == b``"""
    return Node.d(enode, enode.b) == 0 # A solution is found when there is no misplaced tiles i.e. the set of misplaced tiles is empty


def addToLiveNodes(enode: Node, liveNodes: list[Node]):
    """ Adds (in place) given ``enode`` to ``liveNodes`` list, while maintaining the order. (sorted by cost ĉ)

    Parameters
    ----------
    @ `enode` - Node to add to liveNodes list
    @ `liveNodes` - List of live nodes (i.e. nodes that have not been expanded yet)
    """
    liveNodes.append(enode)
    for i in range(len(liveNodes)-1, 0, -1): # loop backward
        if liveNodes[i].cost > liveNodes[i-1].cost: # if the cost of the node at index i is smaller than the cost of the node at index i-1, swap them
            liveNodes[i], liveNodes[i-1] = liveNodes[i-1], liveNodes[i]
        else: break # because the oher elements are sorted


def nextENode(liveNodes: list[Node]) -> Node:
    """ Return the next node to expand. 
    Since we maintain the list sorted by cost, the next node is just ``liveNodes.pop()``.

    Parameters
    ----------
    @ `liveNodes` - List of live nodes (i.e. nodes that have not been expanded yet)

    Returns
    -------
        ``liveNodes.pop()`` i.e. Node with that minimize the cost ĉ in given liveNodes list.
    """
    return liveNodes.pop()


def solve_shortest_path(domain:list[list[int]], a:tuple[int, int], b:tuple[int, int]) -> list[tuple[int, int]]:
    """Finds the shortest path from point a to point b according to the 2-dimensional domain.
    The path is returned as a list of steps from a to b, where each step is a tuple with 2 integers."""
    n, m = len(domain), len(domain[0])
    liveNodes: list[Node] = []
    
    enode: Node = Node.init_root(a, b)
    while not P(enode):
        available_moves: set[M] = children_moves(domain, enode, n, m)

        for move in available_moves:
            child = Node(move, enode)
            addToLiveNodes(child, liveNodes)

        enode = nextENode(liveNodes)
    return enode.path

def test_solve_shortest_path():
    domain = [
        # We want to get here
        # |
        # v
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 0, 0],
        [0, 0, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        # ^
        # |
        # We start from here
    ]
    a, b = (7, 6), (0, 7)
    solution = [a, (7, 7), (6, 7), (5, 7), (4, 7), (3, 7), (2, 7), (1, 7), b]
    sol = solve_shortest_path(domain, a, b)
    assert sol == solution

if __name__ == '__main__':
    test_solve_shortest_path()