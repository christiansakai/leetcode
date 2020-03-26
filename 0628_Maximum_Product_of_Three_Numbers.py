class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        
        choice_a = nums[len(nums) - 3] * nums[len(nums) - 2] * nums[len(nums) - 1]
        choice_b = nums[0] * nums[1] * nums[len(nums) - 1]
        
        return max(choice_a, choice_b)
        
        
        
