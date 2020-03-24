class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums_bool = [False for _ in range(0, len(nums) + 1)]
        for n in nums:
            nums_bool[n] = True
            
        for i in range(0, len(nums_bool)):
            if nums_bool[i] is False:
                return i
            
        return -1    
            
