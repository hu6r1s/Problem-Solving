def dfs(v, sum_a):
    global count

    if v >= n:
        if sum_a == k:
            count += 1
        return

    dfs(v+1, sum_a + a[v])
    dfs(v+1, sum_a)

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    count = 0
    dfs(0, 0)
    print("#{} {}".format(test_case, count))