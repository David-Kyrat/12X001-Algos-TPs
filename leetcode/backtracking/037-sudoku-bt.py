from typing import List, Set


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board) # n is dimension, N is n**2 i.e. max k
        values = {str(x) for x in range(1, n+1)}
        block_coords = []
        for i in range(2, 9, 3):
            for j in range(2, 9, 3):
                block_coords.append((i, j))

        def coord(k: int): return (k // n, k % n)

        def to_idx(i: int, j: int): return i * n + j

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
            out = sorted(base)
            return out

        def B(x: List[List[str]], k: int, N: int):
            row_tc, col_tc = coord(k)
            val = x[row_tc][col_tc]
            #print("B: val =", val)
            # check uniqueness in 3x3 bloc
            for i in range(row_tc - (row_tc % 3), row_tc + 1): # min 1 iter max 3 iter
                mod = col_tc % 3
                offset = 2 - mod if i < row_tc else 0 # iterate through whole line if its not the last
                # i.e. last line stops at column `col_tc`
                for j in range(col_tc - mod, col_tc + offset + 1):
                    # print(f"x[{i}][{j}] = {x[i][j]}, {val}")
                    if x[i][j] == val and (i, j) != (row_tc, col_tc):
                        #print((i, j), x[i][j], val)
                        return False
            return True

        def printBlock(x, k, N):
            row_tc, col_tc = coord(k)
            tmp = []
            for i in range(row_tc - (row_tc % 3), row_tc + 1): # min 1 iter max 3 iter
                mod = col_tc % 3
                offset = 2 - mod if i < row_tc else 0 # iterate through whole line if its not the last
                # i.e. last line stops at column `col_tc`
                s = ""
                for j in range(col_tc - mod, col_tc + 1 + offset):
                    s += f"{x[i][j]} "
                    tmp.append(x[i][j])
                print(s)
            print(tmp)
            return len(set(tmp))  == len(tmp)


        def P(x: List[List[str]], k: int, N: int):
            rowt, colt = coord(k)
            for row in x:
                for el in row:
                    if el == ".": return False
                if len(set(row)) != len(row): return False
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
        given = set()
        for i, row in enumerate(board):
            for j, x in enumerate(row):
                if x != ".": given.add(to_idx(i, j))
        print(given)

        def rBT(x: List[List[str]], k: int, N: int):
            nonlocal done
            if k >= N: return
            # check values to assign to x[k1][k2]
            k1, k2 = coord(k)
            if k >= 75:
                if 1 != 1: print("")
            if k in given:
                if k < N: rBT(x, k + 1, N)
            else:
                for y in T(x, k, N):
                    x[k1][k2] = y
                    if B(x, k, N):
                        # if (k1, k2) in block_coords:
                        #     print("block:")
                        #     printBlock(x, k, N)
                        #     print("")
                        if P(x, k, N):
                            done = True
                            print("sol found")
                            for row in board:
                                print(row)
                            print(" ")
                            return
                        rBT(x, k + 1, N)
                    if done or k >= N: return

        rBT(board, 0, (n**2) - 1)

if __name__ == "__main__":
    board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    s = Solution()
    s.solveSudoku(board)
    for row in board:
        print(row)
    
