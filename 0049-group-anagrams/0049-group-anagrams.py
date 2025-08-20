from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_strs = defaultdict(list)
        
        for word in strs:
            dict_strs[str(sorted(word))].append(word)
        return list(dict_strs.values())