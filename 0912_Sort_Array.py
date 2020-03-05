from typing import List


class Solution:
    # Merge Sort
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums

        pivot = int(len(nums) / 2)
        left = self.sortArray(nums[:pivot])
        right = self.sortArray(nums[pivot:])

        return self.merge(left, right)

    def merge(self, left: List[int], right: List[int]) -> List[int]:
        result = []
        lp = 0
        rp = 0

        while lp < len(left) and rp < len(right):
            if left[lp] < right[rp]:
                result.append(left[lp])
                lp += 1
            else:
                result.append(right[rp])
                rp += 1

        # append remaining
        result.extend(left[lp:])
        result.extend(right[rp:])

        return result
