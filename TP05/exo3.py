########################### Exercise 3 ###########################
from fifteen_puzzle import M, M_ALL, mv, UP, RIGHT, DOWN, LEFT

#
#* Lets call ``a`` the index of our current location, we want to move ``a`` from the starting point ``a0`` to the arrival/destination ``b``.
# 

def swap(board: list[list[int]], tx: tuple[int, int], move: M, misplaced: set[tuple[int, int]] = None) -> tuple[int, int]:
    """Swap index and index coord in coord in the board and update set of misplaced tiles (if not none).

    Parameters
    ----------
    @ `board` - Game board
    @ `move` - move to be made
    @ (optional) `misplaced` - set of misplaced tiles

    Returns
    ----------
        New position of ``a``
    """
    nc = move + tx # new coord of white square
    board[tx[0]][tx[1]], board[nc[0]][nc[1]] = board[nc[0]][nc[1]], board[tx[0]][tx[1]] # swap

    if misplaced is None: return nc

    return nc


class Node: 
    """Node of the game tree. Each node has a ``depth`` (``int``), a cost (``int``), a list of moves ``moves`` (``list[M]``) 
    the index of the empty square, ``tx``, (``tuple[int, int]``) in its associated board, a set of misplaced tiles ``misplaced`` (``set[tuple[int, int]]``)
    and the value of g(this) (``int``)."""
    
    def __init__(self, move: M, parent, board: list[list[int]]):
        """Constructor of the Node class.

        Parameters
        ----------
        @ `move`   - move that led to this node from its parent
        @ `parent` - parent of this node (Can be None, If it is, then this node is the root of the game tree, and tx has to be given)
        @ `board`  - initial board (needed because neither this board nor its update will ever be stored/copied in any node)

        Other attributes
        ---------
        @ `tx`        - index of the empty square in the associated board.
        @ `depth`     - depth of this node in the game tree (i.e. ``h(this) = parent.depth + 1``)
        @ `misplaced` - set of misplaced tiles. (If not given, => will be inferred from `parent` and `move`)
        @ `gx`        - value of ``g(this) = len(misplaced)``
        @ `cost`      - cost of this, defined by ``c_hat(this) = h(this) + g(this)`` (Computed from `parent.depth`, `parent.misplaced` and `move`)
        """
        if parent is None: 
            self.__init_root__(board)
            return
        
        self.depth = parent.depth + 1
        self.tx0 = parent.tx0 # index of the empty square in the initial board
        self.moves = parent.moves + [move]
        self.tx = move + parent.tx # addition between a move and a tuple was defined in the M class above. e.g. ``M.UP + (3, 2)`` returns ``(2, 2)``
        self.cost, self.gx, self.misplaced = update_misplaced_compute_cost(self, parent.misplaced, board, self.moves)

    def __init_root__(self, board: list[list[int]], white_square_value: int = 16):
        """'Private' constructor of root, ``taquin_index`` is the index of the empty square in the initial board """
        self.depth = 0
        self.tx0, self.misplaced = init_misplaced(board, white_square_value)
        self.cost = max(0, len(self.misplaced) - 1) # -1 because we do not count the empty square
        self.moves = []
        self.tx = self.tx0
        self.gx = self.cost

    def __repr__(self):
        """Representation of a node as a string."""
        return f"Node(ĉ={self.cost}, h={self.depth}, tx={self.tx}, moves={self.moves})"



def update_misplaced_compute_cost(node: Node, misplaced: set[tuple[int, int]], board: list[list[int]], moves: list[M])-> tuple[int, int, set[tuple[int, int]]]: 
    """ Instead of storing copies of the board (which would be memory consuming since board is a 2d matrix), 
    this function recomputes the different changes each move would have on the board, and updates the set of misplaced tiles accordingly.

    Then the cost of a node ``x`` is just its depth (``h(x)=x.depth``) ``+`` the length of the set of misplaced tiles (``g(x)=len(x.misplaced)``).
    the total should be in O(2*h(x)) where h(x) is the current number of moves. (swap should be O(1) since add() and contains checks are O(1) for sets)

    Parameters
    ----------
    @ `node` - Node to compute the cost of
    @ `board` - Game board
    @ `moves` - list of moves to get from the root of the game tree to this node (i.e. each "parent" edge of node)

    Returns
    -------
        Triple ``(ĉ(node), g(node), update_misplaced_set)`` where ``ĉ(node) = h(node) + g(node)`` and ``update_misplaced_set`` is the updated set of misplaced tiles
    """
    _misplaced = misplaced.copy() # set of misplaced tiles
    
    tx = apply_moves(board, node.tx0, moves, _misplaced) # node.tx0 = index of the empty square in the initial board
    
    #* Reverting the swaps of Board, since it is modified to computed the updated set of misplaced tiles.
    #* making the changes and reverting them (O(2*n) where n = h(x) is the number of Moves (which is at most g(root)) since if a solution is found the it is optimal.) 
    #* is still faster than making a copy of the board at each iteration. O(m^2) 
    #* (where m is the dimension of the board, here m is a constant but we could have the exact same problem for m unknown and the same implementation would suffice)
    
    unapply_moves(board, tx, moves)
    
    gx = len(_misplaced) # g(x) = number of misplaced tiles
    hx = node.depth
    return gx+hx, gx, _misplaced


def children_moves(node: Node, DIM: int) -> set[M]:
    """ Return a set of all possible moves for the children of the given node.

    Parameters
    ----------
    @ `node` - Node to compute the cost of
    @ `DIM` - Dimension of the board

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
    """ Return true if and only if enode is a goal node. """
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
    # TODO
    n, m = len(domain), len(domain[0])
    DIM = n, m
    liveNodes: list[Node] = []
    
    enode:Node = None # TODO
    while not P(enode):
        available_moves: set[M] = children_moves(enode, DIM)

        for move in available_moves:
            child = None # TODO
            addToLiveNodes(child, liveNodes)

        enode = nextENode(liveNodes)
    return enode.path
