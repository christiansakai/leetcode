import math

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1

        pivot_index = self.find_minimum_index(nums)
        if pivot_index == -1:
            return -1
        
        if pivot_index == 0:
            return self.binary_search(nums, 0, len(nums) - 1, target)
        
        if nums[pivot_index] <= target and target <= nums[len(nums) - 1]:
            return self.binary_search(nums, pivot_index, len(nums) - 1, target)

        return self.binary_search(nums, 0, pivot_index - 1, target) 
    
    
    def find_minimum_index(self, nums: List[int]) -> int:
        if nums[0] <= nums[len(nums) - 1]:
            return 0

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + math.floor((right - left) / 2)
            
            # if mid is greater than mid + 1
            # then mid is the cliff and mid + 1 is the minimum(pivot)
            if nums[mid] > nums[mid + 1]:
                return mid + 1 
            elif nums[left] <= nums[mid]:
                # array is already sorted correctly on the left side
                # so look for pivot to the right
                left = mid + 1
            else:
                # else, we know that pivot is likely on the left side
                right = mid - 1    
                
        # array is not actually rotated        
        return -1

    
    def binary_search(self, nums: List[int], left: int, right: int, target: int) -> int:
        while left <= right:
            mid = left + math.floor((right - left) / 2)
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
                    
        return -1


