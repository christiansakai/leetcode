class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return -1

        largest = nums[0]
        largest_idx = 0
        for i in range(1, len(nums)):
            if nums[i] > largest:
                largest = nums[i]
                largest_idx = i

        for i in range(0, len(nums)):
            if i != largest_idx and not(largest >= 2 * nums[i]):
                return -1

        return largest_idx
