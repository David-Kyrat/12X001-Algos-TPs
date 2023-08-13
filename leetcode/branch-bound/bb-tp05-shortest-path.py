from typing import Dict, List, Optional, Set, Tuple

# from enum import Enum


class Cell:
    def __init__(self, coords: Tuple[int, int], board: List[List[int]]) -> None:
        row, col = coords
        self.row = row
        self.col = col
        self.free = board[row][col] == 0
    
    def __repr__(self):
        free_str = '✅' if self.free else '❌'
        return f"({self.row}, {self.col} {free_str})"

    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value, Cell): return False
        return self.row == __value.row and self.col == __value.col


class Node:
    def __init__(self, pos: Cell, cost: int, state: List[Cell], last_move: Optional[int]) -> None:
        self.pos = pos
        self.cost = cost
        self.state = state.copy()
        self.last_move = last_move

    def depth(self) -> int:
        """Return: Depth i.e. nb of parent from root up to `self`"""
        return len(self.state)

    @staticmethod
    def move_to_str(move: Optional[int]) -> str:
        match move:
            case 0: return "⬆️"
            case 3: return "▶️"
            case 2: return "⬇️"
            case 1: return "◀️"
            case _: return ""
    #NB: in test index on (left, right) axis is reversed hence the swap 3,1
    def __repr__(self):
        #return f"({self.path}, val={self.val} cost={self.cost})"
        return f"({(self.pos.row, self.pos.col)}, cost={self.cost}, {Node.move_to_str(self.last_move)})"


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

def nextENode(pq: List[Node]) -> Node:
    return pq.pop()

def P(node: Node, goal: Cell):
    return node.pos == goal

def shortest_path(board: List[List[int]], _start: Tuple[int, int], _goal: Tuple[int, int]) -> Node:
    start, goal = Cell(_start, board), Cell(_goal, board)
    live_nodes = []
    root = Node(start, 0, [], None)
    # print("goal  =", goal, "\n")
    enode = root
    while not P(enode, goal): #and idx < count:
        # print("enode =", enode.pos)
        for move in listOfChildren(enode, board):
            new_cell: Cell = Cell(MOVES[move](enode.pos.row, enode.pos.col), board)
            new_node = Node(new_cell, cost(new_cell, enode.depth() + 1, goal), [*enode.state, enode.pos], move)
            addToLiveNodes(live_nodes, new_node)

        #print(live_nodes)
        # print("\n")
        enode = nextENode(live_nodes)

    print("\n\n")
    return enode

def node_to_path(node: Node) -> List[Tuple[int, int]]:
    """ return list of pair from root node to given node """
    out = [(x.row, x.col) for x in node.state]
    out.append((node.pos.row, node.pos.col))
    return out

#FREE, BLOCKED = False, True


def test_solve_shortest_path():
    domain = [
        # We want to get here
        # |
        # v
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 0, 0],
        [0, 0, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        #   ^
        #   |
        #   We start from here
    ]
    a, b = (7, 6), (0, 7)
    expected = [a, (7, 7), (6, 7), (5, 7), (4, 7), (3, 7), (2, 7), (1, 7), b]
    obtained = node_to_path(shortest_path(domain, a, b))

    for cell in obtained: print(cell)

    print("-----")
    print("expected:")
    for pair in expected:
        print(pair)
    assert obtained == expected

if __name__ == "__mai__":
    goal = test_solve_shortest_path()
