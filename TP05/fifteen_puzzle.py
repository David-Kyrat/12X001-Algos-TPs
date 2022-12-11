from email.policy import default
from enum import Enum
from copy import deepcopy

########################### Exercise 1 ###########################
# Definitions
UP, RIGHT, DOWN, LEFT = "up", "right", "down", "left"
DIM:int = 4  # Dimension of the board


class M(Enum):
    UP = (-1, 0)
    DOWN = (1, 0)
    RIGHT = (0, 1)
    LEFT = (0, -1)

    v = property(lambda self: self.value)

    # e.g. M.UP() returns (0, -1)
    def __call__(self): return self.v

    def __add__(self, other):
        if isinstance(other, (tuple, list)):
            return (self()[0] + other[0], self()[1] + other[1])
        if isinstance(other, M):
            return self + other()
        raise ValueError(f"Cannot add {type(other)} to {type(self)}")

    def __sub__(self, other):
        if isinstance(other, (tuple, list)):
            return (self.v[0] - other[0], self.v[1] - other[1])
        if isinstance(other, M):
            return self - other.v
        raise ValueError(f"Cannot subtract {type(other)} from {type(self)}")

    def inv(self): 
        """Returns the inverse of the move. e.g. M.UP.inv() returns M.DOWN"""
        return M((-self()[0], -self()[1]))

def isMisplaced(board: list[list[int]], coord:tuple[int, int]) -> bool:
    """Returns True if the element at coord is misplaced, False otherwise. i.e. 15 should be at (3, 3)"""
    return board[coord[0]][coord[1]] != 4 * coord[0] + coord[1] + 1


def tmp():
    import numpy
    B = numpy.dstack(numpy.indices((4,4)))
    return [list(map(lambda x: 4*x[0]+x[1]+1, B[i])) for i in range(len(B))]

B = tmp()

def swap(board: list[list[int]], tx:tuple[int, int], move: M, misplaced: set[tuple[int, int]]) -> tuple[int, int]:
    """Swap index and index coord in coord in the board.

    Parameters
    ----------
    @ `board` - Game board
    @ `tx` - index of white square (16)
    @ `move` - move applied to the white square
    @ `misplaced` - set of misplaced tiles

    Returns
    ----------
        New position of the white square
    """
    nc = move + tx # new coord
    board[tx[0]][tx[1]], board[nc[0]][nc[1]] = board[nc[0]][nc[1]], board[tx[0]][tx[1]] # swap

    # if the new coord is misplaced, add it to the misplaced set
    if isMisplaced(board, nc): misplaced.add(nc)
    else: misplaced.discard(nc) # if not in it => does nothing
    
    # if the swap corrected the position of a tile, remove it from the misplaced set
    if isMisplaced(board, tx): misplaced.add(tx) # if already in it => does nothing
    else: misplaced.discard(tx)

    return nc

def c_hat(board: list[list[int]]) -> int:
    """Cost function for a given board. (where everything has to be recomputed from scratch, 
    for more info see ``update_misplaced_compute_cost()`` below.)
    The cost of a node of the game is the number of squares that are not at their place (16 excluded)."""
    misplaced = 0
    for i in range(DIM):
        for j in range(DIM):
            if isMisplaced(board, (i, j)):
                misplaced += 1
    return min(0, misplaced - 1) # -1 because we do not coun the empty square


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
        self.cost, self.gx, self.misplaced = update_misplaced_compute_cost(self, board, self.moves)

    def __init_root__(self, board: list[list[int]]):
        """'Private' constructor of root, ``taquin_index`` is the index of the empty square in the initial board """
        self.depth = 0
        self.tx0, self.misplaced = init_misplaced(board)
        self.cost = len(self.misplaced)
        self.moves = []
        self.tx = self.tx0
        self.gx = self.cost

    def __repr__(self):
        """Representation of a node as a string."""
        return f"Node(ĉ={self.cost}, h={self.depth}, tx={self.tx}, moves={self.moves})"


def init_misplaced(board: list[list[int]]) -> tuple[tuple[int, int], set[tuple[int, int]]]:
    """Initialize the set of misplaced tiles and return index of white square (16).

    Parameters
    ----------
    @ `board` - Game board

    Returns
    ----------
        Tuple: (index of white square (16),   Set of misplaced tiles)
    """
    misplaced = set()
    tx0 = (-1, -1) # index of white square (16) 
    for i in range(DIM):
        for j in range(DIM):
            if board[i][j] == 16: tx0 = (i, j)
            if isMisplaced(board, (i, j)):
                misplaced.add((i, j))
    return tx0, misplaced


def update_misplaced_compute_cost(node: Node, board: list[list[int]], moves: list[M])-> tuple[int, int, set[tuple[int, int]]]: 
    """ Instead of storing copies of the board (which would be memory and time consuming since board is a 2d matrix), 
    this function recomputes the different changes each move would have on the board, and updates the set of misplaced tiles accordingly.

    Then the cost of a node x is just its depth (h(x)) the length of the set of misplaced tiles (g(x)).
    the total should be in O(m) where m is the number of moves. (swap should be O(1) since add() and contains checks are O(1) for sets)

    Parameters
    ----------
    @ `node` - Node to compute the cost of
    @ `board` - Game board
    @ `moves` - list of moves to get from the root of the game tree to this node (i.e. each "parent" edge of node)

    Returns
    -------
        Triple ``(ĉ(node), g(node), update_misplaced_set)`` where ``ĉ(node) = h(node) + g(node)`` and ``update_misplaced_set`` is the updated set of misplaced tiles
    """
    misplaced, tx = set(), node.tx0 # set of misplaced tiles, index of the empty square in the initial board
    
    for move in moves: 
        tx = swap(board, tx, move, misplaced)

    gx = len(misplaced)
    hx = node.depth
    return gx+hx, gx, misplaced


# associate each direction to its corresponding move
mv: dict[str, M] = {UP: M.UP, RIGHT: M.RIGHT, DOWN: M.DOWN, LEFT: M.LEFT}
# associate each move to its corresponding direction
mv_inv: dict[M, str] = {M.UP: UP, M.RIGHT: RIGHT, M.DOWN: DOWN, M.LEFT: LEFT}

M_ALL = set(mv.values()) # set of all possible moves

def children(node: Node) -> set[M]:
    """ Return a set of all possible moves from a given node.

    Parameters
    ----------
    @ `node` - Node to compute the cost of

    Returns
    -------
        set of all possible moves from a given node."""
    moves = M_ALL.copy()
    moves.remove(node.moves[-1].inv()) # remove inverse of last move to avoid cycles in the game "tree"
    global DIM
    end:int = DIM-1 # for some reason, i have to declare it here, otherwise it wont work

    # now remove moves that would lead to an out of bounds error
    match node.tx[0]:
        # if row of current whitespace is on a side (i.e. if can't go UP or DOWN)
        case 0: 
            moves.discard(M.UP)
            print("UP")

        case end:
            moves.discard(M.DOWN)
            print("DOWN")

    # idem, if column of current whitespace is on a side (i.e. if can't go LEFT or RIGHT)        
    match node.tx[1]:
        case 0:
            moves.discard(M.LEFT)
            print("LEFT")
            
        case end:
            moves.discard(M.RIGHT)
            print("RIGHT")
        

def solve_taquin(board: list[list[int]]) -> list[str]:
    """Function that solves the 15-puzzle using branch and bound.

    Parameters
    ----------
    @ `board` - board to solve
    """
    s:set = set()
    s.discard()

