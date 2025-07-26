class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {num: idx for idx, num in enumerate(nums)}

        for i, v in enumerate(nums):
            idx = target - v
            if idx in d and d[idx] != i:
                return [i, d[idx]]