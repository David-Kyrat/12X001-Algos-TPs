""" EXERCISE 1.3 - Efficiency Test of fifteen_puzzle solution (see fifteen_puzzle.py)"""

from fifteen_puzzle import *



def gen_disorder(board, node:Node, n):
    """Creates disorder in the board by moving (at random) the blank space n times. (Usually ``node`` is a goal node but need not necessarily be.)
    NB: the moves are selected at random but they are still filtered to try to avoid cycles, and out of bounds exceptions.
    (I.e. the move is selected at random among the result of  ``children_moves()``)

    The distance to the initial state will be at most n, but it is actually just equal len(misplaced)

    Parameters
    ----------
    @ `board` - The initial state of the board associated to ``node``
    @ `node`  - Usually a goal node. (if it is not, then the current state will be inferred from ```node.misplaced`` and ``node.moves``)
    @ `n`     - Number of random moves to perform to "shuffle" the board

    NB: board is modified in place
    """
    misplaced: set[tuple[int, int]] = node.misplaced # empty if node is a goal node
    
    apply_moves(board, node.tx0, node.moves, )

