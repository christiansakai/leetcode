import math

class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return -1
        
        left = 0
        right = len(nums) - 1
        
        if nums[left] <= nums[right]:
            # normal array (not rotated at all)
            return nums[0]
        
        while left <= right:
            mid = left + math.floor((right - left) / 2)
            
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            elif nums[left] <= nums[mid]:
                # left array is not rotated, so pivot must be on right side
                # go right
                left = mid + 1
            else:
                # right array is not rotated, so pivot must be on the left side
                # go left
                right = mid - 1
                
        return -1
            
