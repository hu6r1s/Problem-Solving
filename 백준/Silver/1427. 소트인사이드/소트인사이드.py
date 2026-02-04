"""
선택정렬 활용 풀이
선택 정렬은 최댓값 또는 최솟값을 찾아 가장 앞에 있는 데이터와 swap하는 것
"""
import sys
input = sys.stdin.readline

lst = list(input())
for i in range(len(lst)-1):
    max_idx = i
    for j in range(i+1, len(lst)):
        if lst[j] > lst[max_idx]:
            max_idx = j
    lst[max_idx], lst[i] = lst[i], lst[max_idx]
print("".join(lst))