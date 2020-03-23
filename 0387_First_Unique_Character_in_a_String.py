class Solution:
    def firstUniqChar(self, s: str) -> int:
        if len(s) == 0:
            return -1
        
        count = {}
        for i in range(0, len(s)):
            ch = s[i]
            
            if ch in count:
                count[ch] += 1
            else:
                count[ch] = 1
                
        for i in range(0, len(s)):
            ch = s[i]
            
            if count[ch] == 1:
                return i
            
        return -1
            
