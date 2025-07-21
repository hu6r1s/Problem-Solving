from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_nums = Counter(nums)
        count_nums = dict(sorted(count_nums.items(), reverse=True, key=lambda x: x[1])).keys()
        return list(count_nums)[:k]