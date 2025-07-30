import math

class Solution:
    """
        1. 인덱스 슬라이싱을 활용한 풀이
            - 인덱스 슬라이싱을 활용하여 해당 인덱스를 제외한 나머지 원소들의 곲을 math.prod()를 이용하여 배열에 삽입
            - 시간초과 O(n^2)
        2. 
    """
    # 1번 풀이
    # def productExceptSelf(self, nums: List[int]) -> List[int]:
    #     answer = [1] * len(n)

    #     for i in range(len(nums)):
    #         answer.append(math.prod(nums[:i] + nums[i+1:]))

    #     return answer

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        dp = [1] * len(nums)

        left = 1
        for i in range(len(nums)):
            dp[i] = left
            left *= nums[i]
        
        right = 1
        for i in range(len(nums) - 1, -1, -1):
            dp[i] *= right
            right *= nums[i]
        return dp