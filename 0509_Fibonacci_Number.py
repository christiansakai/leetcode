from typing import Dict


class Solution:
    def fib(self, N: int) -> int:
        cache = {}
        return self.recurse(N, cache)

    def recurse(self, N: int, cache: Dict[int, int]) -> int:
        if N == 0:
            return 0

        if N == 1:
            return 1

        if N in cache:
            return cache[N]

        cache[N] = self.recurse(N - 1, cache) + self.recurse(N - 2, cache)

        return cache[N]
