from math import inf
from typing import List, Tuple

COST_MATRIX = []

class Node:
    def __init__(self, cost: int, state: List[Tuple[int, int]]):
        """affectation: task_index, agent_index , state: list of tuple[task_index, agent_index]"""
        self.cost = cost
        self.state = state.copy()

    def affectation(self) -> Tuple[int, int]: return self.state[-1]
    def __repr__(self): return f"({self.state[-1]}, c={self.cost}), cost={COST_MATRIX[self.affectation()[0]][self.affectation()[1]]}"

def cost(affectations: List[Tuple[int, int]], cost_mat: List[List[int]]) -> int:
    h = sum(cost_mat[task_idx][cost_idx] for (task_idx, cost_idx) in affectations)  # cost accumulated up to here
    used_idx = {affect[0] for affect in affectations}
    g, k = 0, len(affectations)
    for row in cost_mat[k:]:
        min_idx, min_cost = None, inf  # no minimum yet
        for a_idx, a_cost in enumerate(row):
            if a_cost < min_cost and a_idx not in used_idx:
                used_idx.discard(min_idx)  # agent `min_idx` isn't affected anymore
                min_idx, min_cost = a_idx, a_cost
                used_idx.add(a_idx)
        g += min_cost
    return g + h # type: ignore


def listOfChildren(parent: Node, cost_mat: List[List[int]]):
    old_affectations = parent.state
    used_agents = {affectation[1] for affectation in old_affectations}
    # agent already used in previous tasks
    N, task_index = len(cost_mat), parent.affectation()[0] + 1  # nb of agents & tasks
    free_agents = [idx for idx in range(N) if idx not in used_agents]
    return [
        Node(
            cost=cost(old_affectations + [(task_index, agent_idx)], cost_mat),
            state=old_affectations + [(task_index, agent_idx)],
        )
        for agent_idx in free_agents
    ]


def addToLiveNodes(node: Node, pq: List[Node]):
    """Add while maintining priority queue order"""
    pq.append(node)
    for i in range(len(pq) - 1, 0, -1):
        crt, next = pq[i], pq[i - 1]
        # smallest at the end
        if crt.cost > next.cost: pq[i], pq[i - 1] = next, crt
        else: break  # already sorted

def P(node: Node, cost_mat: List[List[int]]) -> bool:
    return len(node.state) == len(cost_mat)  # affectations completed?


def branch_bound(cost_mat: List[List[int]]) -> Tuple[List[Tuple[int, int]], int]:
    """Return: affectations, i.e. list of coordinates"""
    root_affect = 0, cost_mat[0].index(min(cost_mat[0]))
    root = Node(cost([root_affect], cost_mat), [root_affect])
    live_nodes = []
    enode = root
    while not P(enode, cost_mat):
        for node in listOfChildren(enode, cost_mat):
            addToLiveNodes(node, live_nodes)
        enode = live_nodes.pop()
        print(enode)
    return enode.state, enode.cost


if __name__ == "__main__":
    # example : cost of task 1 by agent 2 is 17 ( numbering starts at index 0)
    # COST_MATRIX = [[11, 14, 11, 17, 24], [12, 15, 17, 14, 35], [18, 13, 19, 20, 27], [40, 22, 23, 28, 18], [12, 43, 25, 34, 55]]
    COST_MATRIX = [ [11 , 14 , 11 , 17] , [12 , 15 , 17 , 14] , [18 , 13 , 19 , 20] , [40 , 22 , 23 , 28] ]
    result, cost_tot = branch_bound(COST_MATRIX)
    min_mat = 0
    for row in COST_MATRIX: min_mat += min(row)
    print("theorical c(root):", min_mat)

    print("total cost:", cost_tot)
    for task_idx, agent_idx in result:
        print(f"agent{agent_idx} - task{task_idx}", COST_MATRIX[task_idx][agent_idx])
    # the optimal assignement for this cost matrix is :
    # agent0 - task0 , agent1 - task2 , agent2 - task3 , agent3 - task1 .


# def __repr__(self): return f"({self.affectation}, c={self.cost}), cost={COST_MATRIX[self.affectation[0]][self.affectation[1]]}"

# print(f"task{enode.affectation[0]} - agent{enode.affectation[1]} c = {enode.cost}, cost={COST_MATRIX[enode.affectation[0]][enode.affectation[1]]}")
