from typing import Dict

class Solution:
    def myPow(self, x: float, n: int) -> float:
        cache = {}
        power = abs(n) 
        result = self.recurse(x, power, cache)
        
        if n < 0:
            return 1 / result
        
        return result
    
    def recurse(self, x: float, n: int, cache: Dict[int, float]) -> float:
        if n == 0:
            return 1

        if n == 1:
            return x

        result = 0
        if n % 2 == 0:
            sub_prob = self.recurse(x, n / 2, cache)
            result = sub_prob * sub_prob
        else:
            result = x * self.recurse(x, n - 1, cache)    
            
        cache[n] = result
        return cache[n] 
