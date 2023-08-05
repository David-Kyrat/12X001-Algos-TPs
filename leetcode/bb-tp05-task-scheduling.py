from typing import Dict, List, Optional, Set, Tuple, Self


class Node:
    def __init__(self, val: int, cost: int, state: List[int]):
        self.val = val
        self.cost = cost
        self.state = state.copy()

    def __repr__(self):
        return f"({self.state}, val={self.val} cost={self.cost})"


