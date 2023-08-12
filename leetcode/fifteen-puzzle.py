from copy import deepcopy
from typing import List, Set, Tuple, Optional
from prettytable import PrettyTable


class M:
    UP, RIGHT, DOWN, LEFT = 0, 1, 2, 3
    ALL = [UP, RIGHT, DOWN, LEFT]


def swap(board: List[List[int | None]], pos1: Tuple[int, int], pos2: Tuple[int, int]):
    r1, c1 = pos1
    r2, c2 = pos2
    tmp = board[r1][c1]
    board[r1][c1] = board[r2][c2]
    board[r2][c2] = tmp

def apply_move(board: List[List[int | None]], move: int, blank_pos: Tuple[int, int]):
    """Apply given move on board (switch relevant cells)
    and returns the new position of the whitespace"""
    mr, mc = 0, 0  # modifiers: row, column
    match move:
        case M.UP: mr -= 1
        case M.RIGHT: mc += 1
        case M.DOWN: mr += 1
        case M.LEFT: mc -= 1
    orow, ocol = blank_pos # old row old col
    nr, nc = orow + mr, ocol + mc
    swap(board, blank_pos, (nr, nc))
    return nr, nc

def count_misplaced(board: List[List[int | None]]) -> int:
    N, misp = len(board), 0
    for i, row in enumerate(board):
        for j, val in enumerate(row):
            if val is not None and i * N + j + 1 != val: misp += 1
    return misp

def cost(board: List[List[int | None]], state: List[int]) -> int:
    """state: List of moves to apply to get the board from which to compute the cost
    start_pos: position of blank space for root node."""
    h = len(state)
    return h + count_misplaced(board)


class Node:
    def __init__(self, state: List[int], board: List[List[int | None]], old_bpos: Tuple[int, int]):
        """
        state: list of moves (a move is an int in [0, 3]) to apply to attain
        this node in the game tree.
        NB: state[-1] is the last move made that "connects" to this node
        board: state of the board for parent/adjacent node
        old_bpos: position of the blank space in the parent config
        bpos: position of blank space in this config,
        bd: resulting board after having applied all moves in state"""
        bd = deepcopy(board)
        self.state = state[:]  # copy
        self.bpos = apply_move(bd, state[-1], old_bpos) if state else old_bpos
        self.bd = bd  # storing them all is at worst O(3^(n^2)) space
        self.cost = cost(self.bd, self.state)

    def last_move(self): return self.state[-1] if self.state else None
    def __repr__(self): return f"({moves_to_str(self.state)}, bpos={self.bpos}, cost={self.cost})"

def opposite(move: int) -> int:
    """Return: opposite of `move` i.e. the one that reverse it (UP => DOWN...)"""
    return (move + 2) % len(M.ALL)


def next_move_not_out(node: Node) -> Set[int]:
    """Return: sets of next moves that won't cause index out of bounds"""
    N = len(node.bd)
    moves = set(M.ALL)
    row, col = node.bpos
    if row <= 0: moves.discard(M.UP)
    if col <= 0: moves.discard(M.LEFT)
    if row >= N-1: moves.discard(M.DOWN)
    if col >= N-1: moves.discard(M.RIGHT)
    return moves


def listOfChildren(node: Node) -> List[Node]:
    next_moves: Set[int] = next_move_not_out(node)
    last_move: Optional[int] = node.last_move()
    if last_move: next_moves.discard(opposite(last_move))
    return [Node(node.state + [move], node.bd, node.bpos) for move in next_moves]

def addToLiveNodes(pq: List[Node], node: Node):
    pq.append(node)
    for i in range(len(pq) - 1, 0, -1):
        crt, next = pq[i], pq[i-1]
        if crt.cost > next.cost:
            pq[i], pq[i-1] = next, crt
        else: break

def P(node: Node) -> bool: return count_misplaced(node.bd) <= 0


def fifteen_puzzle(board: List[List[int | None]]) -> Node:
    blank_pos = 0, 0
    for i, row in enumerate(board):
        for j, val in enumerate(row):
            if val is None : blank_pos = i, j

    live_nodes: List[Node] = []
    root = Node([], board, blank_pos)
    enode: Node = root
    while not P(enode):
        for node in listOfChildren(enode): addToLiveNodes(live_nodes, node)
        print([node.cost for node in live_nodes])
        enode = live_nodes.pop()
        print(enode); mprint(enode.bd); print(" ")  # noqa: E702
    return enode


# ----------------------------------------

def move_to_str(move: int) -> str:
    match move:
        case 0: return "⬆️"
        case 1: return "▶️"
        case 2: return "⬇️"
        case 3: return "◀️"
        case _: return ""

def moves_to_str(moves: List[int]) -> List[str]:
    return [move_to_str(move) for move in moves]

def mprint(matrix: List[List]):
    p = PrettyTable()
    for row in matrix: p.add_row(row)
    print("_________________")
    print(p.get_string(header=False, border=False))
    print("-----------------")

import numpy as np
if __name__ == "__main__":
    board = [[1, 2, 3, 4], [5, 6, None, 8], [9, 10, 7, 11], [13, 14, 15, 12]]

    print("-------- input ------")
    mprint(board)
    print(cost(board, []))

    print(" ")
    sol = fifteen_puzzle(board)
    print("---- Sol found ---------")
    for move in sol.state:
        print(move_to_str(move))
