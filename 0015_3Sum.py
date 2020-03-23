from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        result = []

        for i in range(0, len(sorted_nums) - 2):
            if i > 0 and sorted_nums[i] == sorted_nums[i - 1]:
                continue

            self.two_sums(sorted_nums, i + 1, sorted_nums[i], result)

        return result


    def two_sums(self, nums: List[int], start_idx: int, found: int, result: List[List[int]]):
        start = start_idx
        end = len(nums) - 1
        target = -found

        while start < end:
            curr_sum = nums[start] + nums[end]

            if curr_sum < target:
                start += 1
            elif curr_sum > target:
                end -= 1
            else:
                result.append([found, nums[start], nums[end]])

                while start < end and nums[start] == nums[start + 1]:
                    start += 1

                while start < end and nums[end] == nums[end - 1]:
                    end -= 1

                start += 1
                end -= 1
