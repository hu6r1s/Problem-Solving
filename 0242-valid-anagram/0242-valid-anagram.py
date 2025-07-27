from collections import defaultdict

class Solution:
    """
        1. Counter를 이용한 풀이
            - Counter로 풀이하였으나 s, t 길이가 서로 다를 때 해결되지 않음
        2. defaultdict 활용 풀이
            - 똑같이 개수 세고 제외
    """
    def isAnagram(self, s: str, t: str) -> bool:
        counter = defaultdict(int)
        
        for i in s:
            counter[i] += 1
        
        for i in t:
            if i not in counter:
                return False
            counter[i] -= 1

            if counter[i] == 0:
                del counter[i]
        return False if counter else True