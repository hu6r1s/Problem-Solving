class Solution:
    """
        [1,2,3,1]
        인덱스 0에서 훔쳤을 때, 인덱스 1은 훔치면 안되므로 nums[0] + F(nums[2:])
        인덱스 0에서 안훔쳤을 때, 인덱스 1에서 훔쳐야 하므로 F(nums[1:])
        
        F[nums] = max(nums[0] + F[nums[2:]], F(nums[1:]))
        F[i] = max(nums[i] + F(i+2), F(i+1))
    """
    def rob(self, nums: List[int]) -> int:
        memo = dict()
        def dfs(start):
            if start in memo:
                return memo[start]
            if start >= len(nums):
                memo[start] = 0
                return memo[start]
            memo[start] = max(nums[start] + dfs(start + 2), dfs(start + 1))
            return memo[start]
        return dfs(0)