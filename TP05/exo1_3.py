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

    return moves

def gen_disorder(board: list[list[int]], node:Node, n:int):
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
        ``(tx_final, misplaced_final)``  - Pair containing the final position of the white square and the final set of misplaced tiles (after the n random moves).
    """
    misplaced: set[tuple[int, int]] = node.misplaced.copy() # empty if node is a goal node
    
    DIM, tx = len(board), apply_moves(board, node.tx0, node.moves, misplaced)
    move: M = random.choice(list(children_move_fromList(None, tx, DIM)))
    for _ in range(n):
        move = random.choice(list(children_move_fromList(move, tx, DIM)))
        tx = apply_moves(board, tx, [move], misplaced)

    return tx, misplaced

def gen_disorder2(board: list[list[int]], n:int):
    """"Overload" of ``gen_disorder()`` that does not require a node as input. (It will create a root node from the given board and then call ``gen_disorder()``)
        (see ``gen_disorder()`` for more details) """
    root: Node = Node(None, None, board)
    DIM: int = len(board)
    root.__init_root__(board, DIM*DIM)
    return gen_disorder(board, root, n)

#! Since printing the board did not seem like a fundamental task of this TP, The following function to print the board in color was taken from internet.
def printBoard(board:list[list[int]], DIM:int, tx:tuple[int, int], misplaced:set[tuple[int, int]]):
    """Prints the board with the white square (16) and the misplaced tiles highlighted."""
    for i in range(DIM):
        for j in range(DIM):
            if (i, j) in misplaced:
                if (i, j) == tx:
                    print(f"\033[1;33m{board[i][j]:2d}\033[0m ", end="")
                else:
                    print(f"\033[1;31m{board[i][j]:2d}\033[0m ", end="")
            else:
                print(f"{board[i][j]:2d} ", end="")
        print("\033[0m")


def pb(board:list[list[int]]):
    """Prints the board with the white square (16) and the misplaced tiles highlighted."""
    DIM = len(board)
    for i in range(DIM):
        for j in range(DIM):
            print(f"{board[i][j]:2d} ", end="")
        print()


def sorted_board(n:int):
    """ return an nxn matrix where each value increase by 1 (starting at 0). e.g. [[1, 2, 3,...],...]  """
    return [[n*i+j+1 for j in range(n)] for i in range(n)]


def test_solve_taquin_for_any_dim(DIM:int):
    """Generates a random board of size DIM x DIM, where the white square value is always the one in the bottom right corner.
    Then solves the puzzle and prints the solution.

    Parameters
    ----------
    @ `DIM` - Dimension of the board to generate and solve.
    """
    _DIM = DIM
    _dim2: int = _DIM*_DIM
    _board = sorted_board(_DIM)
    gen_disorder2(_board, _dim2//2)
        
    _goalNode: Node = solve_taquin(_board, extract_path_from_goalNode=False, white_square=_dim2)
    print("Initial board:")
    printBoard(_board, _DIM, _goalNode.tx0, init_misplaced(_board, _dim2)[1])
    print("\nSolved Board:")
    apply_moves(_board, _goalNode.tx0, _goalNode.moves, _goalNode.misplaced)
    printBoard(_board, _DIM, _goalNode.tx0, _goalNode.misplaced)
    return _goalNode


if __name__ == '__main__':    
    """ board = [[1, 2, 3, 4], 
            [5, 6, 16, 8], 
            [9, 10, 7, 11],
            [13, 14, 15, 12]] """
    # m = 6
    # _goalNode:Node = test_solve_taquin_for_any_dim(m)
    # print(convert_solution(_goalNode))
    # print("----------------------\n")

    # ----------- Test the efficiency of the cost function ----------------

    board = sorted_board(4) # generate a solution board of dim m x m
    goalNode: Node = solve_taquin(board, extract_path_from_goalNode=False)
    print(convert_solution(goalNode))

    n:int = 20
    final_tx, misplaced = gen_disorder(board, goalNode, n)
    print([board[p[0]][p[1]] for p in misplaced])
    printBoard(board, len(board), final_tx, misplaced)

#
#* We now have to test the efficiency of the used cost function, 
#* 
#*
#
