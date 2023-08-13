from typing import Dict, List, Optional, Set, Tuple

class Cell:
    def __init__(self, coords: Tuple[int, int], board: List[List[int]]) -> None:
        row, col = coords
        self.row = row
        self.col = col
        self.free = board[row][col] == 0
    
    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value, Cell): return False
        return self.row == __value.row and self.col == __value.col


class Node:
    def __init__(self, pos: Cell, cost: int, state: List[Cell], last_move: Optional[int]) -> None:
        self.pos = pos
        self.cost = cost
        self.state = state.copy()
        self.last_move = last_move

    # Return: Depth i.e. nb of parent from root up to `self`
    def depth(self) -> int: return len(self.state)

def up(row: int, col: int): return row - 1, col
def right(row: int, col: int): return row, col + 1
def down(row: int, col: int): return row + 1, col
def left(row: int, col: int): return row, col - 1

UP, RIGHT, DOWN, LEFT = 0, 1, 2, 3
MOVES: Dict = {UP: up, RIGHT: right, DOWN: down, LEFT: left}


# Return: opposite of `move` i.e. LEFT => RIGHT...
def opposite(move: int): return move + 2 % len(MOVES)

def valid_moves(node: Node, N: int, M: int) -> Set[int]:
    """NxM: dimension of the board. i.e.  N:nb of rows, M: nb of columns.
    Return moves that would not cause an index out of bounds exception.
    (not guaranteed to be actually usable => doesnt check if next cell is free or not)"""
    out: Set[int] = set(range(UP, LEFT + 1))
    i, j = node.pos.row, node.pos.col
    if i >= N-1: out.discard(DOWN)
    if j >= M-1: out.discard(RIGHT)
    if i <= 0: out.discard(UP)
    if j <= 0: out.discard(LEFT)
    return out

def listOfChildren(node: Node, board: List[List[int]]) -> Set[int]:
    not_out_of_bounds: Set[int] = valid_moves(node, len(board), len(board[0]))
    # remove last move to avoid having 2 consecutive moves cancelling each other
    if node.last_move is not None: not_out_of_bounds.discard(opposite(node.last_move))
    to_remove: Set[int] = set()
    cell = node.pos
    for move in not_out_of_bounds:
       new_row, new_col = MOVES[move](cell.row, cell.col)
       if board[new_row][new_col] == 1: to_remove.add(move) # if cell is blocked remove it
    
    return not_out_of_bounds.difference(to_remove)

def cost(cell: Cell, depth: int, goal: Cell) -> int:
    crt_row, crt_col = cell.row, cell.col
    goal_row, goal_col = goal.row, goal.col
    l1_norm = abs(crt_row - goal_row) + abs(crt_col - goal_col) # g(x) i.e. distance
    return depth + l1_norm

def addToLiveNodes(pq: List[Node], node: Node):
    """Emulate behavior of add PriorityQueue """
    pq.append(node)
    for i in range(len(pq) - 1, 0, -1): # iterate from the end
        crt, next = pq[i], pq[i - 1]
        if next.cost < crt.cost :
            pq[i], pq[i - 1] = next, crt # keep sorted decreasing order
        else: break # rest is sorted

def nextENode(pq: List[Node]) -> Node: return pq.pop()

def P(node: Node, goal: Cell): return node.pos == goal


def shortest_path(board: List[List[int]], _start: Tuple[int, int], _goal: Tuple[int, int]) -> Node:
    start, goal = Cell(_start, board), Cell(_goal, board)
    live_nodes = []
    root = Node(start, 0, [], None)
    enode = root
    while not P(enode, goal):
        for move in listOfChildren(enode, board):
            new_cell: Cell = Cell(MOVES[move](enode.pos.row, enode.pos.col), board)
            new_node = Node(new_cell, cost(new_cell, enode.depth() + 1, goal), [*enode.state, enode.pos], move)
            addToLiveNodes(live_nodes, new_node)

        enode = nextENode(live_nodes)
    return enode
