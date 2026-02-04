"""
정렬 전 인덱스와 정렬 후 인덱스 차이가 가장 큰 값
"""
import sys
input = sys.stdin.readline

n = int(input())
lst = [(int(input()), i) for i in range(n)]
sorted_lst = sorted(lst)
result = 0

for i in range(n):
    if result < sorted_lst[i][1] - i:
        result = sorted_lst[i][1] - i
print(result+1)