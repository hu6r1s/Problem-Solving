class Solution:
    """
        [1,2,3,1]
        인덱스 0에서 훔쳤을 때, 인덱스 1은 훔치면 안되므로 nums[0] + F(nums[2:])
        인덱스 0에서 안훔쳤을 때, 인덱스 1에서 훔쳐야 하므로 F(nums[1:])
        
        F[nums] = max(nums[0] + F[nums[2:]], F(nums[1:]))
        F[i] = max(nums[i] + F(i+2), F(i+1))
    """
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(dp[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        
        return dp[-1]