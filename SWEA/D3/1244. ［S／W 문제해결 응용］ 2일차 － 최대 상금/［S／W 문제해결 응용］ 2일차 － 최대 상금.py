# T = int(input())
# for test_case in range(1, T + 1):
#     s, n = input().split()
#     li = [int(i) for i in s]
#     count = 0
#     for j in range(len(li) - 1, 0, -1):
#         if li[j] == max(li):
#             li[j-len(li)], li[j] = li[j], li[0]
#             count += 1
#         if count == int(n):
#             break
#     print("#{} {}" .format(test_case, "".join(str(i) for i in li)))
def dfs(v):
    global result
    if v == int(n):
        result = max(result, int("".join(map(str, li))))
        return
    for i in range(len(li) - 1):
        for j in range(i + 1, len(li)):
            li[i], li[j] = li[j], li[i]

            check = int("".join(map(str, li)))
            if (v, check) not in visited:
                dfs(v+1)
                visited.append((v, check))
            li[i], li[j] = li[j], li[i]

T = int(input())
for test_case in range(1, T + 1):
    s, n = input().split()
    li = [int(i) for i in s]
    result = 0
    visited = []
    dfs(0)
    print("#{} {}" .format(test_case, result))