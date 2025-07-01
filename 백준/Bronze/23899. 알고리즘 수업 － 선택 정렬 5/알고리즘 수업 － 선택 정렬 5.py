def selection_sort(A, B):
    for last in range(len(A) - 1, -1, -1):
        if A == B:
            return 1
        max_index = A.index(max(A[:last+1]))
        if max_index != last:
            A[last], A[max_index] = A[max_index], A[last]
    return 0


n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(selection_sort(a, b))