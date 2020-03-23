from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) <= 1:
            return len(chars)

        write = 0
        for read in range(len(chars)):
            print('before ' , ' write ', write, ' read ',read)
            ch = chars[read]
            count = 1

            while read < len(chars) - 1 and chars[read] == chars[read + 1]:
                count += 1
                read += 1

            chars[write] = ch

            if count > 1:
                digit_str = str(count)

                for d in digit_str:
                    write += 1
                    chars[write] = d

            print(chars)
            print('after ' , ' write ', write, ' read ',read)
            print()

        return write



            




s = Solution()

# arr = ["a","a","b","b","c","c","c"]
# print(s.compress(arr))
# print(arr)

arr = ["a","a","b","c","c","c"]
print(s.compress(arr))
print(arr)
