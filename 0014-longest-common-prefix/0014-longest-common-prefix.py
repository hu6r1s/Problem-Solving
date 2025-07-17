class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        strs.sort(key=len)

        is_break = False
        standard = strs[0]
        for i in range(len(standard)):
            if is_break:
                break
                
            for str in strs[1:]:
                if str[i] != standard[i]:
                    is_break = True
                    break
            else:
                result += standard[i]
        return result
                