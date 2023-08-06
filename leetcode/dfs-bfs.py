from typing import List, Set, Optional, Self


class Node:
    """Node of binary tree. i.e. has 2 children until max depth is atteined"""
    MAX_DEPTH = 4  # hard-coded for test purposes
    # not max_depth -1 bcs values starts at 2**0 (1 | 2, 3 | 4, 5,6,7) so we added +1 as well
    MAX_VAL = 2 ** (MAX_DEPTH) - 1

    def __init__(self, val: int) -> None: self.val = val

    def get_adjacents(self) -> List[Self]:
        """Return: nodes adjacent to `self`. (i.e. children for a tree)"""
        val_left, val_right, val_top = self.val * 2, self.val * 2 + 1, max(self.val // 2, 1)  # last make graph undirected i.e <->
        return ([] if val_right >= Node.MAX_VAL else [Node(val_top), Node(val_left), Node(val_right)])


def BFS(root: Node, goal: int) -> Optional[Node]:
    visited: Set[int] = set()
    queue: List[Node] = [root]  # emulate queue behavior with list
    _x = 5
    while len(queue) > 0:
        crt = queue.pop(0)  # queue => First in, First Out
        if crt.val not in visited:  # avoid cycle
            if crt.val == goal:
                return crt
            # adds to end => prioritize node on same depth
            for node in crt.get_adjacents():
                queue.append(node)
            visited.add(crt.val)
            print(crt.val)
    return None


if __name__ == "__main__":
    root = Node(1)
    found = BFS(root, 12)
    print("Not Found" if found is None else f"Found: {found.val}")
