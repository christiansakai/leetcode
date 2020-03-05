class Solution:
    # Iterative
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1

        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

    # Recursive
    def reverseString(self, s: List[str]) -> None:
        self.recurse(s, 0, len(s) - 1)

    def recurse(self, s: List[str], left: int, right: int) -> None:
        if left == right:
            return

        s[left], s[right] = s[right], s[left]

        self.recurse(s, left + 1, right - 1)
