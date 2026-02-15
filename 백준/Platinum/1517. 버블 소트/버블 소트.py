import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
cnt = 0

def merge_sort(x):
    global cnt

    if len(x) <= 1:
        return x
    m = len(x) // 2
    left = merge_sort(x[:m])
    right = merge_sort(x[m:])

    tmp = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            tmp.append(left[i])
            i += 1
        else:
            tmp.append(right[j])
            cnt += len(left) - i
            j += 1
    tmp.extend(left[i:])
    tmp.extend(right[j:])
    return tmp


a = merge_sort(a)
print(cnt)