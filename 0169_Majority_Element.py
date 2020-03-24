import math

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        major_count = math.floor(len(nums) / 2)
        dic = {}
        
        for n in nums:
            if n not in dic:
                dic[n] = 1
            else:
                dic[n] += 1
                
            if dic[n] > major_count:
                return n
            
        return -1    
        
