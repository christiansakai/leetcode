from typing import List
import math

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) <= len(nums2):
            return self.binary_search_find_pivot(nums1, nums2)

        return self.binary_search_find_pivot(nums2, nums1)


    def binary_search_find_pivot(self, smaller: List[int], bigger: List[int]) -> int:
        left = 0
        right = len(smaller) - 1

        while left <= right:
            smaller_pivot = left + math.floor((right - left) / 2)
            # from the formula
            # important to remember, especially + 1 below
            # smaller_pivot + bigger_pivot = (len(smaller) + len(bigger) + 1) / 2
            bigger_pivot = math.floor(((len(smaller) + len(bigger) + 1) / 2)) - smaller_pivot

            if smaller[smaller_pivot - 1] <= bigger[bigger_pivot] and bigger[bigger_pivot - 1] <= smaller[smaller_pivot]:
                total_len = len(smaller) + len(bigger)

                if total_len % 2 == 0:
                    left_max = max(smaller[smaller_pivot - 1] + bigger[bigger_pivot - 1])
                    right_min = max(smaller[smaller_pivot] + bigger[smaller_pivot])

                    return (left_max + right_min) / 2

                return min(smaller[smaller_pivot - 1], bigger[bigger_pivot - 1])
            elif smaller[smaller_pivot - 1] > bigger[bigger_pivot]:
                # go left
                right = smaller_pivot - 1
            else:
                # go right
                left = smaller_pivot + 1

        return -1


s = Solution()
nums1 = [1, 3, 8, 9, 15]
nums2 = [7, 11, 18, 19, 21, 25]

result = [1, 3, 7, 8, 9, 11, 15, 18, 19, 21, 25]

s = s.findMedianSortedArrays(nums1, nums2)

print(s)

