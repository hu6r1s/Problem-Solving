class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        cur = 0

        for i in range(len(nums)):
            if nums[i] == target:
                return i
            else:
                if nums[i] < target:
                    cur = i + 1
        else:
            return cur