class Solution:
    # Iterative Bottom Up
    def climbStairs(self, n: int) -> int:
        stairs = [0] * n

        for i in range(0, n):
            if i == 0:
                stairs[i] = 1
            elif i == 1:
                stairs[i] = 2
            else:
                stairs[i] = stairs[i - 1] + stairs[i - 2]

        return stairs[n - 1]

    # Recursive Top Down
    def climbStairs(self, n: int) -> int:
        cache = {}
        return self.recurse(n, cache)

    def recurse(self, n: int, cache: Dict[int, int]) -> int:
        if n == 1:
            return 1

        if n == 2:
            return 2

        if n in cache:
            return cache[n]

        cache[n] = self.recurse(n - 1, cache) + self.recurse(n - 2, cache)

        return cache[n]
