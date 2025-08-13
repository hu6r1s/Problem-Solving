from collections import deque

class Solution:
    def findMin(self, nums: List[int]) -> int:
        nums = deque(nums)
        if len(nums) == 1:
            return nums[0]
            
        while True:
            cur = nums[0]
            nums.rotate(1)
            if cur < nums[0]:
                nums.rotate(-1)
                return nums[0]


"""
[3, 4, 5, 1, 2] -> [2, 3, 4, 5, 1] -> [1, 2, 3, 4, 5]
1. 큐의 rotate 이용 -> 회전 전의 첫 요소가 회전 후의 요소 비교
"""