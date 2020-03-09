import math


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for el in tokens:
            if el == '+':
                a = stack.pop()
                b = stack.pop()
                stack.append(str(int(a) + int(b)))
            elif el == '-':
                a = stack.pop()
                b = stack.pop()
                stack.append(str(int(b) - int(a)))
            elif el == '*':
                a = stack.pop()
                b = stack.pop()
                stack.append(str(int(a) * int(b)))
            elif el == '/':
                a = stack.pop()
                b = stack.pop()
                division = int(b) / int(a)

                if division < 0:
                    stack.append(str(math.ceil(division)))
                else:
                    stack.append(str(math.floor(division)))
            else:
                stack.append(el)

        return stack.pop()
