########################### Exercise 1 ###########################
# Definitions
UP, RIGHT, DOWN, LEFT = "up", "right", "down", "left"


def c_hat(board):
    """Cost function for a given E-Node 'x'.
    The cost of a node of the game is the number of squares that are not at their place (16 excluded)."""
    # TODO
    ...


def solve_taquin(board):
    """Returns a list of actions to be done to solve the game of Taquin from the given starting solution."""
    # TODO
    ...

########################### Exercise 2 ###########################
def solve_tasks(cost_matrix):
    """Finds the best combination of agents and tasks given the cost matrix.
    Returns the answer as a list of task numbers for each agent (in order of agents)."""
    # TODO
    ...


########################### Exercise 3 ###########################
def solve_shortest_path(domain, a, b):
    """Finds the shortest path from point a to point b according to the 2-dimensional domain.
    The path is returned as a list of steps from a to b, where each step is a tuple with 2 integers."""
    # TODO
    ...
