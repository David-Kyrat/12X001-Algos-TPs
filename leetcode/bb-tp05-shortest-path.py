from typing import Dict, List, Optional, Set, Self, Tuple

# from enum import Enum


class Cell:
    def __init__(self, coords: Tuple[int, int], board: List[List[Self]]) -> None:
        row, col = coords
        self.row = row
        self.col = col
        self.free = board[row][col] == 0
    
    def __repr__(self):
        free_str = '✅' if self.free else '❌'
        return f"({self.row}, {self.col} {free_str})"


class Node:
    def __init__(self, pos: Cell, cost: int, state: List[Cell], last_move: Optional[int]) -> None:
        self.pos = pos
        self.cost = cost
        self.state = state.copy()
        self.last_move = last_move

    def depth(self) -> int:
        """Return: Depth i.e. nb of parent from root up to `self`"""
        return len(self.state)

    def __repr__(self):
        #return f"({self.path}, val={self.val} cost={self.cost})"
        return f"({(self.pos.row, self.pos.col)}, cost={self.cost}, lm={self.last_move})"


def up(row: int, col: int): return row - 1, col

def right(row: int, col: int): return row, col + 1

def down(row: int, col: int): return row + 1, col

def left(row: int, col: int): return row, col - 1


UP, RIGHT, DOWN, LEFT = 0, 1, 2, 3
MOVES: Dict = {UP: up, RIGHT: right, DOWN: down, LEFT: left}

def opposite(move: int):
    """Return: opposite of `move` i.e. LEFT => RIGHT ..."""
    return move + 2 % len(MOVES)

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

def listOfChildren(node: Node, board: List[List[Cell]]) -> Set[int]:
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

def _cost(node: Node, goal: Cell) -> int:
    """ 'Overload' of cost method """
    return cost(node.pos, node.depth(), goal)

def addToLiveNodes(pq: List[Node], node: Node):
    """Emulate behavior of add PriorityQueue """
    pq.append(node)
    for i in range(len(pq) - 1, 0, -1): # iterate from the end
        crt, next = pq[i], pq[i - 1]
        if next.cost < crt.cost :
            pq[i], pq[i - 1] = next, crt # keep sorted decreasing order
        else: break # rest is sorted

def nextENode(pq: List[Node]) -> Node:
    return pq.pop()

def P(node: Node, goal: Cell):
    return node.pos == goal

def shortest_path(goal: Cell, board: List[List[Cell]], start: Cell):
    root = Node(start, 0, [], None)
    live_nodes = []
    enode = root
    while not P(enode, goal):
        
        print("enode =", enode)
        for move in listOfChildren(enode, board):
            new_cell: Cell = Cell(MOVES[move](enode.pos.row, enode.pos.col), board)
            new_node = Node(new_cell, cost(new_cell, enode.depth() + 1, goal), [*enode.state, enode.pos], move)
            addToLiveNodes(live_nodes, new_node)

        print(live_nodes)
        enode = nextENode(live_nodes)



FREE, BLOCKED = False, True
