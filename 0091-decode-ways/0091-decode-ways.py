class Solution:
    def numDecodings(self, s: str) -> int:
        """
        1. 재귀 알고리즘 사용
        _
        226 -> B, 26
        _
        26 -> B, 6
        _
        6 -> F "BBF"
        __
        26 -> Z "BZ"
        __
        226 -> V, 6
        _
        6 -> F "VF"
        """
        # def dfs(start):
        #     if start == len(s):
        #         return 1
        #     if s[start] == "0":
        #         return 0
        #     if start + 1 < len(s) and int(s[start:start+2]) < 27:
        #         return dfs(start+1) + dfs(start+2)
        #     else:
        #         return dfs(start+1)
        # return dfs(0)
        
        """
        2. 재귀 + 메모리제이션
        """
        memo = {len(s): 1}
        def dfs(start):
            if start in memo:
                return memo[start]
            if s[start] == "0":
                memo[start] = 0
            elif start + 1 < len(s) and int(s[start:start+2]) < 27:
                memo[start] = dfs(start+1) + dfs(start+2)
            else:
                memo[start] = dfs(start+1)

            return memo[start]
        return dfs(0)