class Solution:
    """
    1. n이 11일때, 이진수로 변환해보면 1011이다. set bits는 1의 값을 찾는 것이기에 1을 카운트해준다.
    """
    def hammingWeight(self, n: int) -> int:
        return str(bin(n)).count('1')