""" EXERCISE 1.3 - Efficiency Test of fifteen_puzzle solution (see fifteen_puzzle.py)"""

from fifteen_puzzle import *
import random

def children_move_fromList(move:M, tx:tuple[int, int], DIM:int) -> set[M]:
    """ Return a set of all possible moves that would not produce an out of bounds error and that are not the given move.

    Parameters
    ----------
    @ `move` - Move to avoid (last move made)
    @ `tx`   - Position of the white square (16)
    @ `DIM`  - Dimension of the board

    Returns
    -------
        set of all possible moves from a given node."""
    moves = M_ALL.copy()
    if move is not None: moves.remove(move.inv()) # remove inverse of last move to avoid cycles in the game "tree"    

    # now remove moves that would lead to an out of bounds error

    # if row of current white square (16) is on a side (i.e. if can't go UP or DOWN)
    if tx[0] == 0: moves.discard(M.UP)
    if tx[0] == DIM-1: moves.discard(M.DOWN)
    
    # idem, if column of current white square (16) is on a side (i.e. if can't go LEFT or RIGHT)        
    if tx[1] == 0: moves.discard(M.LEFT)
    if tx[1] == DIM-1: moves.discard(M.RIGHT)

def gen_disorder(board: list[list[int]], node:Node, n):
    """Creates disorder in the board by moving (at random) the blank space n times. (Usually ``node`` is a goal node but need not necessarily be.)
    NB: the moves are selected at random but they are still filtered to try to avoid cycles, and out of bounds exceptions.
    (I.e. the move is selected at random among the result of a modified version ``children_moves()``)

    The distance to the initial state will be at most n, but it is actually just equal len(misplaced)

    Parameters
    ----------
    @ `board` - The initial state of the board associated to ``node``
    @ `node`  - Usually a goal node. (if it is not, then the current state will be inferred from ```node.misplaced`` and ``node.moves``)
    @ `n`     - Number of random moves to perform to "shuffle" the board

    NB: board is modified in place

    Returns
    ----------
        (``tx_final``, ``misplaced_final``)  - Pair containing the final position of the white square and the final set of misplaced tiles (after the n random moves).
    """
    misplaced: set[tuple[int, int]] = node.misplaced.copy() # empty if node is a goal node
    
    DIM, tx = len(board), apply_moves(board, node.tx0, node.moves, misplaced)

    for _ in range(n):
        move = random.choice(list(children_move_fromList(move, tx, DIM)))
        tx = apply_moves(board, tx, [move], misplaced)

    
