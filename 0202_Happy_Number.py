class Solution:
    def isHappy(self, n: int) -> bool:
        visited = {}
        
        while n > 1:
            if n in visited:
                return False
            
            visited[n] = True
            n = self.get_next(n)
            
        return n == 1
    
    
    def get_next(self, n: int) -> int:
        next_n = 0
        
        for d in str(n):
            next_n += (int(d) * int(d))
            
        return next_n
            
        
