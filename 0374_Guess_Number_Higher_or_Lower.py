# The guess API is already defined for you.
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:


class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n

        while left <= right:
            mid = left + (int((right - left) / 2))
            guessed = guess(mid)

            if guessed == 0:
                return mid
            elif guessed == -1:
                right = mid - 1
            else:
                left = mid + 1

        return -1
