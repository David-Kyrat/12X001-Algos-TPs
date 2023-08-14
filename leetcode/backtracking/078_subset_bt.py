from itertools import chain, combinations
from typing import List, Tuple


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        out = [[]]  # noqa: F841
        def max_k(k: Tuple[int]): return max(k[0], k[1])

        def T(x: List[List[int]], k:Tuple[int], N: int):
            return list(range(max_k(k), N))

        def recBT(x: List[List[int]], k:Tuple[int], path:List[int], N: int):
            # we go through nums in increasing order of indices
            if max_k(k) >= N: return # if we arrived at the end of said indices => stop
            path.append(None) # => else store (or not) elements starting from max(k, old_i) (old_i is the iteration index with which recBT was called)
            _T = T(x, k, N)
            #print(f"T(x, {k}, {N}) =", [nums[xi] for xi in _T])
            for i in _T:
                print("")
                #print(path, f"path | k, nums[{i}] ", k, nums[i])
                print("out =", out, " i =", i)
                path[-1] = nums[i]
                if nums[i] not in path[:-1] and path not in out: # doesnt cover permutation i.e. [1,2,3] and [1, 3, 2]
                    out.append(path.copy())
                    print(path.copy())
                    recBT(x, (k[0] + 1, i), path.copy(), N)

        recBT([[]], (0, 0), [], len(nums))
        return out


def powerset(iterable):
    s = list(iterable)
    tmp = list(chain.from_iterable(combinations(s, r) for r in range(len(s)+1)))
    return [list(x) for x in tmp]

def test_pws():
    exp = [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
    obtained = powerset([1, 2, 3])
    assert exp == obtained
    #assert eq(exp, obtained)

def test_1():
    inp, exp = [1,2,3],  [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
    s = Solution()
    assert exp == s.subsets(inp)

def test_2():
    inp, exp = [2,3,1],  [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
    s = Solution()
    assert exp == s.subsets(inp)

# NOTE: Correct ✅
