from typing import List, Optional, Self, Set


class Node:
    """Node of binary tree. i.e. has 2 children until max depth is atteined"""
    MAX_DEPTH = 4  # hard-coded for test purposes
    # not max_depth -1 bcs values starts at 2**0 (1 | 2, 3 | 4, 5,6,7) so we added +1 as well
    MAX_VAL = 2 ** (MAX_DEPTH) - 1
    def __init__(self, val: int) -> None: self.val = val
    def get_adjacents(self) -> List[Self]:
        """Return: nodes adjacent to `self`. (i.e. children for a tree)"""
        val_left, val_right, val_top = self.val * 2, self.val * 2 + 1, max(self.val // 2, 1)  # last make graph undirected i.e <->
        return [] if val_right > Node.MAX_VAL else [Node(val_top), Node(val_left), Node(val_right)]
    def __repr__(self) -> str: return repr(self.val)


def BFS(root: Node, goal: int) -> Optional[Node]:
    visited: Set[int] = set()
    queue: List[Node] = [root]  # emulate queue behavior with list
    while len(queue) > 0:
        crt = queue.pop(0)  # queue => First in, First Out
        visited.add(crt.val)
        print(crt)
        if crt.val == goal: return crt
        for node in crt.get_adjacents():
            # avoid cycle
            if node.val not in visited: queue.append(node)
            # adds to end => prioritize node on same depth
    return None

def DFS2(root: Node, goal: int) -> Optional[Node]:
    visited: Set[int] = set()
    stack: List[Node] = [root]
    while len(stack) > 0:
        crt = stack.pop(-1)
        visited.add(crt.val)
        print(crt)
        if crt.val == goal: return crt
        for node in crt.get_adjacents():
            if node.val not in visited: stack.append(node)
    return None

def graph_traversal(root: Node, goal: int, is_bfs: bool):
    """if `is_bfs` search for `goal` with BFS else do it with DFS """
    visited: Set[int] = set()
    live_nodes: List[Node] = [root]
    def queue(): return live_nodes.pop(0)  # First In First Out (BFS)
    def stack(): return live_nodes.pop(-1) # First In Last Out (DFS)
    next_node = queue if is_bfs else stack
    while len(live_nodes) > 0:
        crt = next_node()
        visited.add(crt.val)
        print(crt)
        if crt.val == goal: return crt
        for node in crt.get_adjacents():
            if node.val not in visited: live_nodes.append(node)
    return None


def DFS(root: Node, goal: int) -> Optional[Node]:
    out: Optional[Node] = None
    visited: Set[int] = set()
    def rec(crt: Node):
        nonlocal out
        visited.add(crt.val)
        for node in crt.get_adjacents():
            if node.val == goal:
                out = node
                return
            if node.val not in visited: rec(node)
            if out is not None: return

    rec(root)
    return out




if __name__ == "__main__":
    root = Node(1)
    # found = BFS(root, 16)
    # print("-------------------")
    # found = DFS(root, 15)
    # found = DFS2(root, 16)
    found = graph_traversal(root=root, goal=16, is_bfs=True)
    print("Not Found" if found is None else f"Found: {found.val}")
    print("-------------------")
    found = graph_traversal(root=root, goal=16, is_bfs=False)
    print("Not Found" if found is None else f"Found: {found.val}")
