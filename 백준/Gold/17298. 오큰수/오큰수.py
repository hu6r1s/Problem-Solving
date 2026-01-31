# n = int(input())
# a = list(map(int, input().split()))
#
# for i in range(n):
#     stack = []
#     for nxt in a[i+1:]:
#         if a[i] < nxt:
#             stack.append(nxt)
#     print(stack[0] if stack else -1, end=" ")


n = int(input())
a = list(map(int, input().split()))
idx = 0
result = [-1] * n
stack = []
for i in range(n):
    while stack and a[stack[-1]] < a[i]:
        idx = stack.pop()
        result[idx] = a[i]
    stack.append(i)
print(*result)
"""
a(i)의 오큰수는
오른쪽에 있으면서 a(i)보다 큰 수 중에서 가장 왼쪽에 있는 수
그런게 없으면 -1
a = [3, 5, 2, 7]
i = 0
a를 차례대로 돌면서 해당 인덱스보다 1 큰 수들 중
큰 해당 인덱스 값보다 큰 숫자들만 스택 저장
스택의 0번째 인덱스 출력
"""