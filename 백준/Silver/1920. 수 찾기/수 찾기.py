import sys
input = sys.stdin.readline

def binary_search(array, target):
    start = 0
    end = n - 1
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return True
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

n = int(input())
a = list(map(int, input().split()))
a.sort()
m = int(input())
m_list = list(map(int, input().split()))
for i in m_list:
    if binary_search(a, i):
        print(1)
    else:
        print(0)