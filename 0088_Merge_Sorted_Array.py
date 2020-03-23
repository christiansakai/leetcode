from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1 = 0
        p2 = 0

        while (p1 < len(nums1)) and (p2 < len(nums2)):
            if p1 >= m:
                nums1[p1] = nums2[p2]

                p1 += 1
                p2 += 1
            else:
                if nums1[p1] <= nums2[p2]:
                    p1 += 1
                else:
                    self.shift_to_right_by_one(nums1, p1)

                    # Very important
                    m += 1

                    nums1[p1] = nums2[p2]
                    p2 += 1



    def shift_to_right_by_one(self, nums: List[int], start_idx: int):
        for i in range(len(nums) - 2, start_idx - 1, -1):
            nums[i + 1] = nums[i]
