class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        if len(nums) == 1:
            return nums[0]
        
        max_profits = [0 for _ in nums]
        max_profits[0] = nums[0]
        
        for i in range(1, len(nums)):
            if i == 1:
                max_profits[i] = max(nums[0], nums[1])
            else:    
                max_profits[i] = max(
                    max_profits[i - 2] + nums[i],
                    max_profits[i - 1]
                )
            
        return max_profits[len(max_profits) - 1]
        
