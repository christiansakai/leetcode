from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        last_non_zero_idx = -1

        for i in range(len(nums)):
            if nums[i] != 0:
                last_non_zero_idx += 1
                self.swap(nums, i, last_non_zero_idx)


    def swap(self, nums: List[int], i: int, j: int) -> None:
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
