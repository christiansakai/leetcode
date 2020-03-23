from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            if k != nums[0]:
                return 0

            return 1

        subarr_count = 0

        total = 0
        slow = 0
        fast = 0

        while fast < len(nums):
            total += nums[fast]

            if total == k:
                subarr_count += 1
            elif total > k:
                while total > k:
                    total -= nums[slow]
                    slow += 1

                if total == k:
                    subarr_count += 1

            fast += 1

        return subarr_count


s = Solution()
print(s.subarraySum([-1,-1,1], 0))
