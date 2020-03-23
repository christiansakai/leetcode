from typing import Dict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        dic = {
            s[0]: 1
        }

        i = 0
        j = 1
        maximum = 0

        while j < len(s):
            ch = s[j]

            if ch not in dic:
                dic[ch] = 1
                maximum = max(maximum, j - i + 1)
            else:
                dic[ch] += 1

                while self.has_duplicates(dic):
                    ch = s[i]

                    if dic[ch] == 1:
                        del dic[ch]
                    else:
                        dic[ch] -= 1

                    i += 1

                maximum = max(maximum, j - i + 1)

            j += 1

        return maximum

    def has_duplicates(self, dic: Dict[str, int]) -> bool:
        for ch in dic:
            if dic[ch] > 1:
                return True

        return False
