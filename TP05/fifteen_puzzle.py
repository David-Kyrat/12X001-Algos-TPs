from copy import deepcopy
from enum import Enum
from shutil import move

########################### Exercise 1 ###########################
# Definitions
UP, RIGHT, DOWN, LEFT = "up", "right", "down", "left"
#DIM:int = 4  # Dimension of the board


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

def isMisplaced(board: list[list[int]], coord: tuple[int, int]) -> bool:
    """Returns True if the element at coord is misplaced, False otherwise. i.e. 15 should be at (3, 3)"""
    return board[coord[0]][coord[1]] != 4 * coord[0] + coord[1] + 1


def swap(board: list[list[int]], tx: tuple[int, int], move: M, misplaced: set[tuple[int, int]] = None) -> tuple[int, int]:
    """Swap index and index coord in coord in the board and update set of misplaced tiles (if not none).

    Parameters
    ----------
    @ `board` - Game board
    @ `tx` - index of white square (16)
    @ `move` - move applied to the white square
    @ (optional) `misplaced` - set of misplaced tiles

    Returns
    ----------
        New position of the white square
    """
    nc = move + tx # new coord of white square
    board[tx[0]][tx[1]], board[nc[0]][nc[1]] = board[nc[0]][nc[1]], board[tx[0]][tx[1]] # swap

    if misplaced is None: return nc
    
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
    for i in range(len(board)):
        for j in range(len(board[i])):
            if isMisplaced(board, (i, j)):
                misplaced += 1
    return max(0, misplaced - 1) # -1 because we do not coun the empty square


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
        @ `board`  - initial board

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

    def __init_root__(self, board: list[list[int]]):
        """'Private' constructor of root, ``taquin_index`` is the index of the empty square in the initial board """
        self.depth = 0
        self.tx0, self.misplaced = init_misplaced(board)
        self.cost = max(0, len(self.misplaced) - 1) # -1 because we do not count the empty square
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
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 16: tx0 = (i, j)
            if isMisplaced(board, (i, j)):
                misplaced.add((i, j))
    return tx0, misplaced


def update_misplaced_compute_cost(node: Node, misplaced: set[tuple[int, int]], board: list[list[int]], moves: list[M])-> tuple[int, int, set[tuple[int, int]]]: 
    """ Instead of storing copies of the board (which would be memory consuming since board is a 2d matrix), 
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
    _misplaced, tx = misplaced.copy(), node.tx0 # set of misplaced tiles, index of the empty square in the initial board

    for move in moves: 
        tx = swap(board, tx, move, _misplaced)

    # Reverting the swaps of Board, since it is modified to computed the updated set of misplaced tiles.
    # making the changes and reverting them (O(2*M) where M is the number of Move at max) is still faster than making a copy of the board at each iteration. O(n^2)
    for i in range(len(moves)-1, -1, -1):
        tx = swap(board, tx, moves[i].inv(), None)
    
    gx = len(_misplaced) # g(x) = number of misplaced tiles
    hx = node.depth
    return gx+hx, gx, _misplaced


# associate each direction to its corresponding move
mv: dict[str, M] = {UP: M.UP, RIGHT: M.RIGHT, DOWN: M.DOWN, LEFT: M.LEFT}
# associate each move to its corresponding direction
mv_inv: dict[M, str] = {M.UP: UP, M.RIGHT: RIGHT, M.DOWN: DOWN, M.LEFT: LEFT}

M_ALL = set(mv.values()) # set of all possible moves


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

    # if row of current whitespace is on a side (i.e. if can't go UP or DOWN)
    if node.tx[0] == 0: moves.discard(M.UP)
    if node.tx[0] == DIM-1: moves.discard(M.DOWN)
    
    # idem, if column of current whitespace is on a side (i.e. if can't go LEFT or RIGHT)        
    if node.tx[1] == 0: moves.discard(M.LEFT)
    if node.tx[1] == DIM-1: moves.discard(M.RIGHT)

    """  match node.tx[0]:
        case 0: moves.discard(M.UP)
        case _BOARD_ND: moves.discard(M.DOWN)

    _BOARD_ND = DIM-1 # reassign end because its getting modified somewhere apparently
    match node.tx[1]:
        case 0: 
            moves.discard(M.LEFT)
        case _BOARD_ND: 
            moves.discard(M.RIGHT) """
            
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


def convert_solution(goal_node: Node) -> list[str]:
    """ Return the list of moves (as string i.e. "up", "down"...) to get from the initial state to the goal state.

    Parameters
    ----------
    @ `goal_node` - Node representing the goal state

    Returns
    -------
        List of moves to get from the initial state to the goal state.
    """
    return [mv_inv[move] for move in goal_node.moves]


def solve_taquin(board: list[list[int]]) -> list[str]:
    """Function that solves the 15-puzzle using branch and bound.
    NB: technically the algorithm could work for more than 16 tiles (i.e. for a board of size n x n where n >= 4)
    
    Parameters
    ----------
    @ `board` - Matrix representing the initial state of the game
    """
    DIM = len(board) # board should be a square matrix
    liveNodes: list[Node] = []
    enode = Node(None, None, board) # special constructor for root node
    while not P(enode):
        available_moves: set[M] = children_moves(enode, DIM)

        for move in available_moves: 
            child = Node(move, enode, board)
            addToLiveNodes(child, liveNodes)

        enode = nextENode(liveNodes)

    return convert_solution(enode)

if __name__ == '__main__':
    board = [[1, 2, 3, 4], 
         [5, 6, 16, 8], 
         [9, 10, 7, 11],
         [13, 14, 15, 12]]

    sol = solve_taquin(board)
    print(sol)
