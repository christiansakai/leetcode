class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        dic = {}
        for ch in s:
            if ch not in dic:
                dic[ch] = 1
            else:
                del dic[ch]
        
        return len(dic.keys()) <= 1
        
                
