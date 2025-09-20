class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_count, window = {}, {}

        for c in t:
            t_count[c] = 1 + t_count.get(c, 0)
        
        have, need = 0, len(t_count)
        res, len_res = [-1, -1], float("infinity")
        left = 0
        for right in range(len(s)):
            c = s[right]
            window[c] = 1 + window.get(c, 0)

            if c in t_count and window[c] == t_count[c]:
                have += 1
            
            while have == need:
                if (right - left + 1) < len_res:
                    res = [left, right]
                    len_res = (right - left + 1)
                window[s[left]] -= 1
                if s[left] in t_count and window[s[left]] < t_count[s[left]]:
                    have -= 1
                left += 1
        left, right = res
        return s[left:right+1] if len_res != float("infinity") else ""