class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = {}
        for ch in s:
            if ch not in dic:
                dic[ch] = 1
            else:
                dic[ch] += 1

        for ch in t:
            if ch not in dic:
                return False

            if dic[ch] == 1:
                del dic[ch]
            else:
                dic[ch] -= 1    
                
        return len(dic.keys()) == 0
                
