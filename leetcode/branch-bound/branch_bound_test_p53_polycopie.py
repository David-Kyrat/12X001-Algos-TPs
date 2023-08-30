from typing import List, Self, Optional

def path_str(node) -> str: return str([x.val for x in [*node.path, node]])

class Node:
    def __init__(self, val: int, cost: int, path: Optional[List[Self]] = None):
        self.val = val
        self.cost = cost
        self.path = path.copy() if path is not None else [] # HINT: Useful to keep track of path?

    def __repr__(self):
        return f"({path_str(self)}, cost={self.cost})"


def branch_bound():
    DEPTH = 3

    # idx is node. starts at 2 (because node values starts at 1 and node 1 has no weight)
    WEIGHTS: List[int] = [4, 9, 9, 6, 2, 7, 8, 7, 10, 8, 5, 3, 8, 1]
    MIN_W: int = min(WEIGHTS[2:])
    root_cost = MIN_W * DEPTH # c^(root) = c^(optimum)
    root = Node(1, root_cost, [])

    def W(node_val: int):
        # w(i) => weight of node i. indexing starts at 2 (because node values starts at 1 and node 1 has no cost)
        if node_val - 2 >= len(WEIGHTS): print(node_val)
        return WEIGHTS[node_val - 2]

    def cost(child_val: int, parent: Node):
        # computed as cost up to there (parent) + distance (child's weight) from Minimum weight
        return parent.cost + (W(child_val) - MIN_W) 

    def get_children(node: Node) -> List[Node]:
        """Returns: all children of `node`"""
        # new_path: List[Node] = [*node.path, node]
        # WARN: In this implementation path depends on previously visited nodes not on the parent
        # y child of x =\\> y.path = [x, ...]. y.path[0] may be y's neighbour
        #
        # HINT: Dépend de ce qu'on cherche. Si la solution est juste le résultat final, ou le path optimal / nombre de noeuds visités ou autre. Car si on veut minimiser le nb de coups et le poids (ici) alors changer de branch sera tres penalisant car on aura 2 nodes pour une même depth.
        # => Pour shortest path par exemple osef du nombre de noeud visité on veut juste trouver le plus petit chemin même s'il nous a pris 15 coups à trouver.
        val_left, val_right = (
            2 * node.val,
            2 * node.val + 1,
        )  # binary tree hence each node i has children 2*i and 2*i + 1
        new_path = [*node.path, node]
        cost_left, cost_right = cost(val_left, node), cost(val_right, node)
        left, right = Node(val_left, cost_left, new_path), Node(val_right, cost_right, new_path)

        return [left, right]

    def addToLiveNodes(pq: List[Node], node: Node):
        """add `node` to `pq` while maintining order i.e. emulating behavior of a priority queue for `pq`"""
        pq.append(node)
        for i in range(len(pq) - 1, 0, -1):  # iterate in reversed order
            crt, next = pq[i], pq[i - 1]
            if crt.cost > next.cost:
                pq[i], pq[i - 1] = next, crt
            else: break # rest of pq is sorted
        
    def nextENode(pq: List[Node], old_enode: Node) -> Node:
        """ Return: `pq.pop()` i.e. also removes element """
        out = pq.pop()
        # WARN: if we care about all visited nodes to solution keep below lines and comment path
        # assignation in constructor. Otherwise comment this one.
        
        # out.path = [*old_enode.path, old_enode] # adjusts current visited nodes between `root` and `out`
        return out
    

    def P(node: Node) -> bool:
        """ Return: Whether `node` is a solution or not.
        Here it is the case when the path is complete. i.e. reached the end
        i.e. contains 3 node"""
        if not node: return False
        #return DEPTH <= len(node.path)
        return node.val in range(8, 16)

    live_nodes: List[Node] = []
    enode: Node = root
    tmp = True
    while not P(enode):
        print("enode =", enode)
        if tmp:
            addToLiveNodes(live_nodes, root)
            tmp = False
        for node in get_children(enode): addToLiveNodes(live_nodes, node)
        print(live_nodes)
        enode = nextENode(live_nodes, enode)
        print(" ")

    solution: Node = enode
    print(f"Solution found: {solution.val} ({solution.cost})")
    print([x.val for x in [*solution.path, solution]])


if __name__ == "__main__":
    branch_bound()
    # Entire parcours: [1, 2, 5, 3, 6, 13] (bin tree indexed 1 -> 15)
    # Best path found: [1, 3, 6, 13] (after having inspected [1, 2, 5, 3, 6, 13])
