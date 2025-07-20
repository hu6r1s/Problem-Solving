from collections import Counter

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        cnt = Counter(nums)
        for k, v in cnt.items():
            if v >= 2:
                return True
        else:
            return False