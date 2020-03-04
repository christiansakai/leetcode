class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        permutation = []

        self.recurse(nums, permutation, result)
        return result

    def recurse(self,
                nums: List[int],
                permutation: List[int],
                result: List[List[int]]):
        if len(nums) == 0:
            permutation = [x for x in permutation]
            result.append(permutation)
            return

        for n in nums:
            new_nums = [x for x in nums if x != n]

            permutation.append(n)
            self.recurse(new_nums, permutation, result)
            permutation.pop()
