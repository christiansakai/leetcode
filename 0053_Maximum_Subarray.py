class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        if len(nums) <= 1:
            return nums[0]
        
        dp_table = [0 for _ in nums]
        dp_table[0] = nums[0]
        maximum = dp_table[0]
        
        for i in range(1, len(nums)):
            dp_table[i] = max(dp_table[i - 1] + nums[i], nums[i])
            maximum = max(dp_table[i], maximum)
            
        return maximum
            
            
