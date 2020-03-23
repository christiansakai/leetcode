from typing import Dict

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if len(s) == 0:
            return False
        
        wordMap = {}
        for word in wordDict:
            wordMap[word] = True
            
        cache = {}
            
        return self.recurse(s, wordMap, cache)
    

    def recurse(self, s: str, wordMap: Dict[str, bool], cache: Dict[str, bool]) -> bool:
        if s in wordMap:
            return True
        
        if s in cache:
            return cache[s]
        
        path_found = False
        for i in range(len(s)):
            first_half, second_half = s[:i + 1], s[i + 1:]
            can_be_broken = first_half in wordMap and self.recurse(second_half, wordMap, cache)
            
            path_found = path_found or can_be_broken
            
        cache[s] = path_found
            
        return path_found
            
