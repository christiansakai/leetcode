from typing import List

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for ch in s:
            if ch == ']':
                curr_ch = []
                while len(stack) > 0 and stack[len(stack) - 1] != '[':
                    popped = stack.pop()
                    curr_ch.insert(0, popped)

                # pop '['
                stack.pop()

                num_ch = []
                while len(stack) > 0 and stack[len(stack) - 1].isdigit():
                    popped = stack.pop()
                    num_ch.insert(0, popped)

                num_str = ''.join(num_ch)
                num = int(num_str)

                multiplied_str = self.multiply(curr_ch, num)
                stack.append(multiplied_str)
            else:
                stack.append(ch)

        return ''.join(stack)


    def multiply(self, s: List[str], num: int) -> str:
        result = []
        for i in range(0, num):
            result.extend(s)

        return ''.join(result)
