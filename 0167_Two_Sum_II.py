class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if len(numbers) == 0:
            return []

        left = 0
        right = len(numbers) - 1

        while left < right:
            total = numbers[left] + numbers[right]
            if total == target:
                return [left + 1, right + 1]
            elif total < target:
                left += 1
            else:
                right -= 1

        return [0, 0]
