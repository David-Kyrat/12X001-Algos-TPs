########################### Exercise 1 ###########################
# Definitions
UP, RIGHT, DOWN, LEFT = "up", "right", "down", "left"


def c_hat(board: list[list[int]]) -> int:
    """Cost function for a given E-Node 'x'.
    The cost of a node of the game is the number of squares that are not at their place (16 excluded)."""
    # TODO
    ...


def solve_fifteen_puzzle(board: list[list[int]]) -> list[str]:
    """Function that solves the 15-puzzle using branch and bound.

    Parameters
    ----------
    @ `board` - board to solve
    """
