import math

class Solution:
    def reverse(self, x: int) -> int:
        is_neg = x < 0
        x = abs(x)

        new_int = 0

        while x > 0:
            digit = x % 10

            if self.is_going_to_overflow(is_neg, new_int, digit):
                return 0
            else:
                new_int = (10 * new_int) + digit

            x = math.floor(x / 10)

        if is_neg:
            return -1 * new_int

        return new_int

    def is_going_to_overflow(self, negative: bool, new_int: int, digit: int) -> bool:
        if negative:
            if new_int > 214748364 or (new_int == 214748364 and digit > 8):
                return True
        else:
            if new_int > 214748364 or (new_int == 214748364 and digit > 7):
                return True

        return False
