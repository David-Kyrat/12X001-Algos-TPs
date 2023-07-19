from typing import List


# compute sum of array with D&C
def dc(nums: List[int]) -> int:
    i = 0
    # return S(J)
    def combine(s_i1, s_i2) -> int:
        return s_i1 + s_i2

    def dc_rec(p: int, q: int) -> int:
        nonlocal i
        if p >= q:
            assert p == q
            print(f"nums[{p}] = {nums[p]}\n")
            return nums[p]
        else:
            m = (q + p) // 2
            print(f"p{i} = {p}  m{i} = {m}  q{i} = {q} {nums[p: m + 1]} | {nums[m+1 : q+1]}")
            return combine(dc_rec(p, m), dc_rec(m + 1, q))

    return dc_rec(0, len(nums) - 1)


# must be sorted and increased only by 1
def correct_sum(nums: List[int]) -> int:
    if not nums or len(nums) < 1: return 0
    if len(nums) == 1: return nums[0]
    max = nums[-1]
    return int(max * (max + 1) / 2)

def test(n: int):
    inp = list(range(n+1))
    print("\t", inp)
    expected = correct_sum(inp)
    obtained = dc(inp)
    print(f"expected: {expected}, obtained: {obtained}")
    

if __name__ == "__main__":
    test(5)
