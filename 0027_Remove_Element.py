class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 0:
            return 0

        i = 0
        for k in range(0, len(nums)):
            if nums[k] != val:
                nums[i] = nums[k]
                i += 1

        return i
