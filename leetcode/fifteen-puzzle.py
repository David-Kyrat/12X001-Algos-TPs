from typing import List, Optional, Self, Set, Tuple


def cost(_board: List[List[int]], state: List[int], start_pos: Tuple[int, int] ) -> int:
    """state: List of moves to apply to get the board from which to compute the cost
            NB: must include last move. i.e. call this function like this: `cost(..., parent_state + [crt_move], ...)`
    start_pos: position of blank space for root node"""
    return 0

class Node:
    def __init__(self, move: int, bpos: Tuple[int, int], state: List[int], board: List[List[int|None]], start_pos: Tuple[int, int]) -> None:
        """bpos: position of blank space,
        state: list of moves (a move is an int in [0, 3])"""
        self.move = move
        self.bpos = bpos
        self.state = state
        self.cost = cost(board, state + [move], )

    
