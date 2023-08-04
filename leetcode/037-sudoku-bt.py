from typing import List, Set


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        printt = False
        n = len(board) # n is dimension, N is n**2 i.e. max k
        values = {str(x) for x in range(1, n+1)}
        block_coords = []
        for i in range(2, 9, 3):
            for j in range(2, 9, 3):
                block_coords.append((i, j))
 
        def coord(k: int): return (k // n, k % n)
        def to_idx(i: int, j: int): return i * n + j
        def is_same_diag(i1: int, j1: int, i2: int, j2: int):
            z = i1 - i2, j1 - j2
            return z[0] == z[1]
        def is_same_antidiag(i1: int, j1: int, i2: int, j2: int):
            z = i1 - i2, j1 - j2
            return z[0] == -z[1]

        def T(x: List[List[str]], k: int, N: int) -> Set[str]:
            base = values.copy()
            row, col = coord(k)
            # discard same row (before)
            for i, xi in enumerate(x[row]):
                if i >= col: break # only iterate *exclusive* until crt col of given row
                base.discard(xi)
            # discard same column
            for i in range(row):
                base.discard(x[i][col])
            return base

        def B(x: List[List[str]], k: int, N: int):
            row_tc, col_tc = coord(k)
            val = x[row_tc][col_tc]
            #if val == ".": return False
            # check uniqueness in 3x3 bloc
            for i in range(row_tc - (row_tc % 3), row_tc + 1): # min 1 iter max 3 iter
                offset = 2 if i < row_tc else col_tc % 3 # iterate through whole line if its not the last
                # i.e. last line stops at column `col_tc`
                for j in range(min(col_tc - offset, 0), col_tc):
                    #if j < 0: print("j < 0", col_tc, " ", col_tc % 3)
                    #print(f"x[{i}][{j}] = {x[i][j]}, {val}")
                    if x[i][j] == val: return False
            print("")
            return True
        
        def printBlock(x, k, N):
            row_tc, col_tc = coord(k)
            for i in range(row_tc - (row_tc % 3), row_tc + 1): # min 1 iter max 3 iter
                offset = 2 if i < row_tc else col_tc % 3 # iterate through whole line if its not the last
                # i.e. last line stops at column `col_tc`
                s = ""
                for j in range(col_tc - offset, col_tc + 1):
                    s += f"{x[i][j]} "
                print(s)


        def P(x: List[List[str]], k: int, N: int):
            rowt, colt = coord(k)
            for row in x:
                for el in row:
                    if el == ".": return False
            to_check = []
            # get block to check
            for pairs in block_coords:
                p1, p2 = pairs
                if p1 < rowt or (p1 == rowt and p2 <= colt): to_check.append(pairs)
                if p1 > rowt: break
            # for each pair to check
            crt_k = 0
            for p_tc in to_check:
                crt_k = to_idx(*p_tc)
                if x[p_tc[0]][p_tc[1]] == ".": return False
                if not B(x, crt_k, N): return False
            return B(x, k, N) if crt_k < k else True

        done = False
        def rBT(x: List[List[str]], k: int, N: int):
            nonlocal done
            nonlocal printt
            for y in T(x, k, N):
                k1, k2 = coord(k)
                x[k1][k2] = y
                if B(x, k, N):
                    if (k1, k2) in block_coords:
                        print("block:")
                        printt = True
                        printBlock(x, k, N)
                        printt = False
                    if P(x, k, N):
                        done = True
                        return
                    rBT(x, k + 1, N)
                    if done: return
        rBT(board, 0, (n**2) - 1)
        print("")
        for row in board:
            print([int(_x) for _x in row])

        


if __name__ == "__main__":
    board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    s = Solution()
    s.solveSudoku(board)
    for row in board:
        print(row)

