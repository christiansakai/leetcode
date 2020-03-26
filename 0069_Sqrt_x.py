import math

class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        
        start = 0
        end = x
        
        while start <= end:
            mid = start + math.floor((end - start) / 2)
            midsqr = mid * mid
            
            if midsqr == x:
                return mid
            elif midsqr > x:
                end = mid - 1
            else:
                start = mid + 1
                
        return end
        
