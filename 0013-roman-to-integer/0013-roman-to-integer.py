class Solution:
    def romanToInt(self, s: str) -> int:
        symbol = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        value = 0
        for i in range(len(s)-1):
            if symbol[s[i]] < symbol[s[i+1]]:
                value -= symbol[s[i]]
            else:
                value += symbol[s[i]]
        value += symbol[s[-1]]
        return value