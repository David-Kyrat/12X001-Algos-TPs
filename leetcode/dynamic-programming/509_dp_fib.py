class Solution:

    def fib(self, n: int) -> int:
        if n < 2: return n
        if n == 2: return 1

        cache = [0] * (n + 1)
        cache[0], cache[1], cache[2] = 0, 1, 1

        for i in range(3, n + 1):
            # if not computed yet
            if cache[i] == 0:
                cache[i] = cache[i - 1] + cache[i - 2]
        return cache[n]

    def tribonacci(self, n: int) -> int:
        if n < 2: return n
        if n == 2: return 1

        cache = [0]*(n + 1)
        cache[0], cache[1], cache[2] = 0, 1, 1
        
        for i in range(3, n + 1):
            # if not computed yet
            if cache[i] == 0:
                cache[i] = cache[i - 1] + cache[i - 2] + cache[i - 3]
            print(cache)

        return cache[n]

if __name__ == "__main__":
    s = Solution()
    print(s.tribonacci(4))
