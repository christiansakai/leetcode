class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return -1
        
        if len(nums) == 1:
            return 0
        
        left_sums = [0 for _ in nums]
        for i in range(len(nums)):
            if i == 0:
                left_sums[i] = 0
            else:
                left_sums[i] = left_sums[i - 1] + nums[i - 1]
            
        right_sums = [0 for _ in nums]
        for i in range(len(nums) -1, -1, -1):
            if i == len(nums) - 1:
                right_sums[i] = 0
            else:
                right_sums[i] = right_sums[i + 1] + nums[i + 1]
                
        for i in range(len(nums)):
            if left_sums[i] == right_sums[i]:
                return i
            
        return -1
