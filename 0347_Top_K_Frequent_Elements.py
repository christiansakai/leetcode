import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 0:
            return []
        
        count = {}
        for n in nums:
            if n not in count:
                count[n] = 1
            else:
                count[n] += 1
                
        heap = []
        for n in count:
            tupl = (count[n] * -1, n)
            heapq.heappush(heap, tupl)
            
        result = []    
        for i in range(k):
            tpl = heapq.heappop(heap)
            result.append(tpl[1])
            
        return result
            
        
