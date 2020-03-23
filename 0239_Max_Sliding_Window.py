from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 0 or k == 0 or len(nums) < k:
            return []

        maximums = []
        window = []

        for i in range(0, len(nums) - (k - 1)):
            if i == 0:
                for j in range(i, i + k):
                    window.append(nums[j])
            else:
                window.pop(0)
                window.append(nums[i + k - 1])

            maximums.append(self.count_max(window))

        return maximums


    def count_max(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        maximum = nums[0]
        for i in range(1, len(nums)):
            maximum = max(maximum, nums[i])

        return maximum


s = Solution()
arr = [1,3,-1,-3,5,3,6,7]
k = 3
print(s.maxSlidingWindow(arr, k))

arr = [1]
k = 1
print(s.maxSlidingWindow(arr, k))

arr = []
k = 0
print(s.maxSlidingWindow(arr, k))
