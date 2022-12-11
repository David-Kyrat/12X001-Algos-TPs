""" EXERCISE 1.3 - Efficiency Test of fifteen_puzzle solution (see fifteen_puzzle.py)"""
from copy import deepcopy
from fifteen_puzzle import *
import util
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

def gen_disorder(board: list[list[int]], n:int, node:Node=None, tx: tuple[int, int]=(3,3)):
    """Creates disorder in the board by moving (at random) the blank space n times. (Usually ``node`` is a goal node but need not necessarily be.)
    NB: the moves are selected at random but they are still filtered to try to avoid cycles, and out of bounds exceptions.
    (I.e. the move is selected at random among the result of a modified version ``children_moves()``)

    The distance to the initial state will be at most n, but it is actually just equal len(misplaced)

    Parameters
    ----------
    @ `board` - The initial state of the board associated to ``node``
    @ `n`     - Number of random moves to perform to "shuffle" the board
    @ (optional) `node`  - Usually a goal node. (if it is not, then the current state will be inferred from ``node.misplaced`` and ``node.moves``). (If it is not given, the current state will be will be the initial state and a root node will be created (with empty ``node.misplaced`` and ``node.moves``))
    @ (optional) `tx`    - Position of the white square (16). (If it is not given, it will be inferred from ``node``, ! has to be given, if node is not ! )

    NB: board is modified in place

    Returns
    ----------
        ``(tx_final, misplaced_final)``  - Pair containing the final position of the white square and the final set of misplaced tiles (after the n random moves).
    """
    DIM: int = len(board)
    # empty if node is a goal node
    misplaced, tx = (node.misplaced.copy(), node.tx0) if node is not None else (set(), tx)
    if node is not None: 
        apply_moves(board, node.tx0, node.moves, misplaced)
    
    move: M = random.choice(list(children_move_fromList(None, tx, DIM)))
    for _ in range(n):
        move = random.choice(list(children_move_fromList(move, tx, DIM)))
        tx = apply_moves(board, tx, [move], misplaced)

    return tx, misplaced

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
    gen_disorder(_board, _dim2//2, tx=(_DIM-1, _DIM-1))
        
    _goalNode: Node = solve_taquin(_board, extract_path_from_goalNode=False, white_square=_dim2)
    print("Initial board:")
    printBoard(_board, _DIM, _goalNode.tx0, init_misplaced(_board, _dim2)[1])
    print("\nSolved Board:")
    apply_moves(_board, _goalNode.tx0, _goalNode.moves, _goalNode.misplaced)
    printBoard(_board, _DIM, _goalNode.tx0, _goalNode.misplaced)
    return _goalNode

def test_cost_efficiency(nMax: int, amount:int):
    """ For each ``n`` from ``1`` to ``nMax`` (inclusive), do 50 times the following:
            generates a sorted board, then call ``gen_disorder(board, n)`` on it to create a random board 
             (shuffle the board with n 'moves' ). Then solve it and count the number explored nodes ``k``

    Parameters
    ----------
    @ `nMax` - max number of moves to perform to shuffle the board. i.e. max "level of disorder"
    @ `amount` - number of time to perform the test for each ``n``
    """
    board = sorted_board(4)
    avgs:dict[int: float] = {}
    
    for n in range(1, nMax+1):
        k = 0
        for i in range(amount):
            crt_board = deepcopy(board)
            gen_disorder(crt_board, n)
            goalNode:Node = solve_taquin(crt_board, extract_path_from_goalNode=False)
            k += goalNode.depth # number of explored nodes is the depth of the goal node
            #print(f"n: {n:2d}", f"   k: {k:3d}", f"   crt: {goalNode.depth:2d}", "   avg:", k/(i+1))
        avgs[n] = k/amount
    return avgs
            
if __name__ == '__main__':    
    """ board = [[1, 2, 3, 4], 
            [5, 6, 16, 8], 
            [9, 10, 7, 11],
            [13, 14, 15, 12]] """
    """ m = 7
    _goalNode:Node = test_solve_taquin_for_any_dim(m)
    print(convert_solution(_goalNode))
    print("----------------------\n") """

    # ----------- Test the efficiency of the cost function ----------------

    """ board = sorted_board(4) # generate a solution board of dim m x m
    n:int = 20
    final_tx, misplaced = gen_disorder(board, n, tx=(3, 3))
    goalNode: Node = solve_taquin(board, extract_path_from_goalNode=False) """

    nMax, amount = 14, 100 # max level of disorder, number of time to perform the test for each level
    print(test_cost_efficiency(nMax, amount))
    avgs = test_cost_efficiency(nMax, amount)
    x_plot, x_label = list(avgs.keys()), "disorder level, (max distance from solution)"
    y_plot, y_label = list(avgs.values()), r"average number $k$ of explored nodes (to get to the solution)"
    flabel = r'average $k = \hat{c}(x^*)$ for cost: $\hat{c}(x)=h(x)+g(x)$ and goal node $x^*$'
    #flabel = r'lul'
    from numpy import linspace
    yticks = linspace(0, nMax, 2*nMax)
    util.plot_solo(x_plot, y_plot, title=r'Average number (100 runs) of explored nodes for given disorder level, with $\hat{c}(x)=h(x)+g(x)$', xlabel=x_label, ylabel=y_label, fLabel=flabel, xticks=x_plot, yticks=yticks)
    

#
#* We now have to test the efficiency of the used cost function, 
#* 
#*
#
