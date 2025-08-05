class Solution:
    """

    """
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        output, nums = [], []

        def dfs(start, total):
            if total > target:
                return
            if total == target:
                output.append(nums[:])
            
            for i in range(start, len(candidates)):
                nums.append(candidates[i])
                dfs(i, total + candidates[i])
                nums.pop()
        
        dfs(0, 0)
        return output