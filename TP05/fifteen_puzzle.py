from enum import Enum

########################### Exercise 1 ###########################
# Definitions
UP, RIGHT, DOWN, LEFT = "up", "right", "down", "left"
DIM = 4  # Dimension of the board


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

    def inv(self): return M((-self()[0], -self()[1]))

def isMisplaced(board: list[list[int]], coord:tuple[int, int]) -> bool:
    """Returns True if the element at coord is misplaced, False otherwise. i.e. 15 should be at (3, 3)"""
    return board[coord[0]][coord[1]] == 4 * coord[0] + coord[1] + 1


def tmp():
    import numpy
    B = numpy.dstack(numpy.indices((4,4)))
    return [list(map(lambda x: 4*x[0]+x[1]+1, B[i])) for i in range(len(B))]

B = tmp()

def swap(board: list[list[int]], tx:tuple[int, int], move: M, misplaced: set[tuple[int, int]]) -> set[tuple[int, int]]:
    """Swap index and index coord in coord in the board.

    Parameters
    ----------
    @ `board` - Game board
    @ `tx` - index of white square (16)
    @ `move` - move applied to the white square
    @ `misplaced` - set of misplaced tiles

    Returns
    ----------
        `misplaced` - updated set of misplaced tiles
    """
    nc = move + tx # new coord
    board[tx[0]][tx[1]], board[nc[0]][nc[1]] = board[nc[0]][nc[1]], board[tx[0]][tx[1]] # swap

    print(isMisplaced(board, nc), nc)
    # if the new coord is misplaced, add it to the misplaced set
    if isMisplaced(board, nc): misplaced.add(nc)
    
    print(isMisplaced(board, tx), tx)
    # if the swap corrected the position of a tile, remove it from the misplaced set
    if not isMisplaced(board, tx) and tx in misplaced: 
        misplaced.remove(tx)
    
    

class Node: 
    """Node of the game tree. Each node has a ``depth`` (``int``), a cost (``int``), a list of moves ``moves`` (``list[M]``) 
    the index of the empty square, ``tx``, (``tuple[int, int]``) in its associated board, and the value of g(this) (``int``)."""
    
    def __init__(self, cost:int, move: M, parent, tx: tuple[int, int] = None):
        """Primary constructor of the Node class.

        Parameters
        ----------
        @ `cost`   - cost of this, defined by ``c_hat(this) = h(this) + g(this)``
        @ `move`   - move that led to this node from its parent
        @ `parent` - parent of this node (Can be None, If it is, then this node is the root of the game tree, and tx has to be given)
        @ (optional)`tx` - index of the empty square in the associated board. (If not given, => will be inferred from `parent`)
        @ `depth`  - depth of this node in the game tree (i.e. ``h(this)``)
        @ `gx`      - value of ``g(this)``
        """
        if parent is None:
            self.__init_root__(cost, tx)
            return
        
        self.depth = parent.depth + 1
        self.cost = cost
        self.moves = parent.moves + [move]
        self.tx = move + parent.tx # addition between a move and a tuple was defined in the M class above. e.g. ``M.UP + (3, 2)`` returns ``(2, 2)``
        self.gx = cost - (parent.depth + 1)

    def __init_root__(self, cost:int, taquin_index: tuple[int, int]):
        """'Private' constructor of root, ``taquin_index`` is the index of the empty square in the initial board """
        self.depth = 0
        self.cost = cost
        self.moves = []
        self.tx = taquin_index
        self.gx = cost

    def __repr__(self):
        """Representation of a node as a string."""
        return f"Node(ĉ={self.cost}, h={self.depth}, tx={self.tx}, moves={self.moves})"



# associate each direction to its corresponding move
mv: dict[str, M] = {UP: M.UP, RIGHT: M.RIGHT, DOWN: M.DOWN, LEFT: M.LEFT}
# associate each move to its corresponding direction
mv_inv: dict[M, str] = {M.UP: UP, M.RIGHT: RIGHT, M.DOWN: DOWN, M.LEFT: LEFT}



def c_hat(board: list[list[int]]) -> int:
    """Cost function for a given E-Node 'x'.
    The cost of a node of the game is the number of squares that are not at their place (16 excluded)."""
    # TODO
    ...


def solve_taquin(board: list[list[int]]) -> list[str]:
    """Function that solves the 15-puzzle using branch and bound.

    Parameters
    ----------
    @ `board` - board to solve
    """


