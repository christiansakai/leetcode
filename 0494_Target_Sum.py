from typing import List, Dict


class Solution:
    # Top Down
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        if len(nums) == 0:
            return 0

        cache = {}
        return self.recurse(nums, S, 0, 0, cache)

    def recurse(
            self,
            nums: List[int],
            S: int,
            index: int,
            total: int,
            cache: Dict[int, Dict[int, int]],
    ) -> int:
        if index == len(nums):
            if total == S:
                return 1

            return 0

        if index in cache:
            if total in cache[index]:
                return cache[index][total]

        plus = self.recurse(nums, S, index + 1, total + nums[index], cache)
        minus = self.recurse(nums, S, index + 1, total - nums[index], cache)

        result = plus + minus

        if index not in cache:
            cache[index] = {}

        cache[index][total] = result

        return result
