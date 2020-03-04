class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []

        self.recurse(nums, 0, subset, result)
        return result

    def recurse(self,
                nums: List[int],
                index: int,
                subset: List[int],
                result: List[List[int]]):
        if index == len(nums):
            subset = [x for x in subset]
            result.append(subset)
            return

        self.recurse(nums, index + 1, subset, result)

        subset.append(nums[index])
        self.recurse(nums, index + 1, subset, result)
        subset.pop()
