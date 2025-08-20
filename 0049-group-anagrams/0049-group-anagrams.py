class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_strs = {}
        
        for word in strs:
            if not str(sorted(word)) in dict_strs:
                dict_strs[str(sorted(word))] = []
            dict_strs[str(sorted(word))].append(word)
        return list(dict_strs.values())