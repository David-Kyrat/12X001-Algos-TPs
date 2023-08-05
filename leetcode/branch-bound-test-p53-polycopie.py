from typing import List


class Node:
    def __init__(self, val: int, cost: int, path: List):
        self.val = val
        self.cost = cost
        self.path = path.copy()


DEPTH = 3


def get_children(node: Node) -> List[Node]:
    """Returns: all children of `node`
    Here binary tree => each `node` has 2 children"""
    _new_path: List[Node] = node.path + node


if __name__ == "__main__":
    print("lul")
