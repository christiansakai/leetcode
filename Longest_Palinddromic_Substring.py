from typing import Tuple, Dict

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s

        cache = {}
        start, end = self.recurse(s, 0, len(s) - 1, cache)
        return s[start:end + 1]


    def recurse(self,
                s: str,
                start: int,
                end: int,
                cache: Dict[int, Dict[int, Tuple[int, int]]],
                ) -> Tuple[int, int]:
        if start >= end:
            return [start, end]

        if start in cache and end in cache[start]:
            return cache[start][end]

        if s[start] == s[end]:
            sub_prob = self.recurse(s, start + 1, end - 1, cache)

            if sub_prob[0] == start + 1 and sub_prob[1] == end - 1:
                return [start, end]

        skip_front = self.recurse(s, start + 1, end, cache)
        skip_front_len = skip_front[1] - skip_front[0] + 1

        skip_back = self.recurse(s, start, end - 1, cache)
        skip_back_len = skip_back[1] - skip_back[0] + 1

        if start not in cache:
            cache[start] = {}

        if skip_front_len < skip_back_len:
            cache[start][end] = skip_back
            return skip_back

        cache[start][end] = skip_front
        return skip_front


s = Solution()
# print(s.longestPalindrome('babad'))
# print(s.longestPalindrome('cbbd'))
# print(s.longestPalindrome('balalaracecarlabalab'))
# print(s.longestPalindrome('ac'))

print(s.longestPalindrome("321012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210123210012321001232100123210123"))






        
