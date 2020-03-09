class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        maximum = 0

        i = 0
        while i < len(nums):
            if nums[i] == 1:
                j = i
                while j < len(nums) and nums[j] == 1:
                    j += 1

                maximum = max(maximum, j - i)
                i = j
            else:
                i += 1

        return maximum
