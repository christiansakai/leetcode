class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums_clone = nums.copy()
        for idx in range(len(nums_clone)):
            new_idx = (idx + k) % len(nums) 
            nums[new_idx] = nums_clone[idx] 
        
