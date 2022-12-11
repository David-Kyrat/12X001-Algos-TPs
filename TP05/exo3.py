########################### Exercise 3 ###########################
from fifteen_puzzle import M, M_ALL, mv, UP, RIGHT, DOWN, LEFT

#
#* Lets call ``a_k`` the index of our current location after the k-th move, we want to move from the starting point ``a0`` to the arrival/destination ``b = a_{c(x_0)}``  (``x_0`` is the root of the tree of all possible moves/outcome).
#* We'll use the same cost function approximation ``ĉ(x) = h(x) + g(x)`` as in fifteen_puzzle .
# 

def move(domain: list[list[int]], tx: tuple[int, int], dir: M, misplaced: set[tuple[int, int]] = None) -> tuple[int, int]:
    """ Move 1 step from tx in the direction `dir`. (i.e. to ``tx + dir``) in the domain.

    Parameter
    ----------
    @ `domain` - domain to scour
    @ `dir`    - direction in which to move
    @ (optional) `misplaced` - set of misplaced tiles

    Returns
    ----------
        New position ``a_k+1 = a_k + dir``
    """
    nc = dir + tx # new coord of white square
    domain[tx[0]][tx[1]], domain[nc[0]][nc[1]] = domain[nc[0]][nc[1]], domain[tx[0]][tx[1]] # swap

    if misplaced is None: return nc

    return nc
#@ `domain`  - initial domain (needed because neither this domain nor its update will ever be stored/copied in any node)

class Node: 
    """Node of the moves tree. Each attribute is detailled below."""
    
    def __init__(self, move: M, parent):
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
        """
        if move is None or parent is None: return # root node
        self.ak = move + parent.ak
        self.b = parent.b
        self.depth = parent.depth + 1
        self.path = parent.path + [self.ak]
        self.cost = Node.c_hat(self)
        
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
        return newnode

    @classmethod
    def d(cls, x1, x2) -> int:
        """Returns the distance d(this, x) = ||a_k - x||_1 (i.e. norm ``L1``) between the current location and x"""
        if isinstance(x1, Node) and isinstance(x2, Node): return x1.__d__(x1, x2)
        if isinstance(x1, Node): return abs(x1.ak[0] - x2[0]) + abs(x1.ak[1] - x2[1])
        if isinstance(x2, Node): return abs(x2.ak[0] - x1[0]) + abs(x2.ak[1] - x1[1])
        return abs(x1[0] - x2[0]) + abs(x1[1] - x2[1])

    def __d__(self, node)->int:
        """ same as ``d()`` but does not performe type check """
        return abs(self.ak[0] - node.ak[0]) + abs(self.ak[1] - node.ak[1])

   
    @classmethod
    def c_hat(cls, node) -> int:
        """Returns the cost of a node (i.e. ``ĉ(node) = h(node) + g(node)``)"""
        return node.depth + node.__d__(node.b)

    
    def __repr__(self):
        """Representation of a node as a string."""
        return f"Node(ĉ={self.cost}, ak={self.ak}, g={self.cost}, h={self.depth}, b={self.b}, path={self.path})"


def children_moves(node: Node, DIM: int) -> set[M]:
    """ Return a set of all possible moves for the children of the given node.

    Parameters
    ----------
    @ `node` - Node to compute the cost of
    @ `DIM` - Dimension of the domain

    Returns
    -------
        set of all possible moves from a given node."""
    moves = M_ALL.copy()
    if node.moves != []: moves.remove(node.moves[-1].inv()) # remove inverse of last move to avoid cycles in the game "tree"    

    # now remove moves that would lead to an out of bounds error

    # if row of current white square (16) is on a side (i.e. if can't go UP or DOWN)
    if node.tx[0] == 0: moves.discard(M.UP)
    if node.tx[0] == DIM-1: moves.discard(M.DOWN)
    
    # idem, if column of current white square (16) is on a side (i.e. if can't go LEFT or RIGHT)        
    if node.tx[1] == 0: moves.discard(M.LEFT)
    if node.tx[1] == DIM-1: moves.discard(M.RIGHT)
            
    return moves


def P(enode: Node):
    """ Return true if and only if enode is a goal node.  ``enode`` has arrived 
    at its destination ``b`` if and only if its distance to ``b`` is null (in the matical sense) 
    i.e. if ``||enode.ak - b||_1 = 0`` i.e. ``enode.ak == b``"""
    return enode.gx == 0 # A solution is found when there is no misplaced tiles i.e. the set of misplaced tiles is empty


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
    DIM = n, m
    liveNodes: list[Node] = []
    
    enode: Node = Node.init_root(a, b)
    while not P(enode):
        available_moves: set[M] = children_moves(enode, DIM)

        for move in available_moves:
            child = Node(move, enode)
            addToLiveNodes(child, liveNodes)

        enode = nextENode(liveNodes)
    return enode.path
