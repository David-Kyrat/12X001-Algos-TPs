DIM = 5
VALUES: list[int] = list(range(10))

def coord(k: int, n: int) -> tuple[int, int]:
    """k: idx of current step, n:dimension of sudoku (i.e. 4x4 => n=4).
    Take index in {0..(n-1)^2} and return index in {0..n}^2"""
    return k // n, k % n

def discard_all(s: set, to_disc) -> None:
    for x in to_disc: s.discard(x)

def getCol(M: list[list], idx: int, k: int = 0) -> list:
    return [M[i][idx] for i in range(k)]

def T(x: list[list[int]], k: int, n: int = DIM) -> set[int]:
    """Explicit conditions, no 2 same nb on row or colum"""
    crt_val = set(VALUES)
    i, j = coord(k, n)  # idx of row, cols
    discard_all(crt_val, x[i])  # discard already used values in row
    if i > 0:  # if (i, j) is not the first index of column j
        discard_all(crt_val, [x[m][j] for m in range(i)])  #! i not j, discard already used values in column,
        #* we process line by line so the amount of element filled in any column at step k is at most coord(k, n)[0] 
        # (i.e. row but works since k do not decrease)
    return crt_val

def isSameDiag(i1: int, j1: int, i2: int, j2: int) -> bool: 
    return abs(i1 - i2) == abs(j1 - j2)  # i.e. |i1-i2| == |j1-j2|

def B(x: list[list[int]], k: int, n: int = DIM) -> bool:
    """Implicit conditions, no 2 same nb on the each diagonal"""
    ki, kj = coord(k, n)
    crt= x[ki][kj]
    for m in range(k):
        i,j = coord(m, n)
        if isSameDiag(ki, kj, i,j) and crt == x[i][j]: return False
    return True

def P(x: list[list[int]], k: int, n: int = DIM) -> bool:
    N: int = n**2
    if k < N-1: return False #! if at least N-1 steps haven't been made => x never a solution
    for crt_idx in range(N - 1):
        if not B(x, crt_idx): return False
    return True

def add_el(x: list[list[int]], yi: int, yj: int, y: int) -> None:
    """if row x[yi] not long enough => append element"""
    if len(x[yi]) <= yj: x[yi].append(y)
    else: x[yi][yj] = y

def BT_sudoku(dim: int) -> list[list[int]]:
    """dim: length of a row of sudoku grid"""
    found: bool = False
    def rBT(x: list[list[int]], k: int, n: int = DIM) -> list[list[int]]:
        """x nxn matrix initialized as n empty list,  k in [|0, (n^2)-1 |] step idx"""
        for y in T(x, k, n):
            yi, yj = coord(k, n)
            add_el(x, yi, yj, y)
            if B(x, k, n):
                if P(x, k, n): return (x, found:=True)[0]
                rBT(x, k + 1, n)
                if found: return x
    return rBT([[] for _ in range(dim)], 0, dim)
