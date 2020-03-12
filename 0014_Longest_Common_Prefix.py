class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""

        if len(strs) == 1:
            return strs[0]

        result = []
        pointer = 0

        while True:
            char_same = True

            for i in range(1, len(strs)):
                char_same =\
                    char_same and\
                    pointer < len(strs[i - 1]) and pointer < len(strs[i]) and\
                    strs[i - 1][pointer] == strs[i][pointer]

                if not char_same:
                    return "".join(result)

            if char_same:
                result.append(strs[0][pointer])

            pointer += 1

        return "".join(result)
