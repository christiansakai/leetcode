from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i in range(len(nums)):
            num = nums[i]
            remaining = target - num

            if remaining in hashMap:
                return [hashMap[remaining], i]

            hashMap[num] = i

        return [-1, -1]
