for test_case in range(1, 11):
    n = int(input())
    li = list(map(int, input().split()))
    li.sort()
    for _ in range(n):
        li[0], li[-1] = li[0] + 1, li[-1] - 1
        li.sort()
        result = li[-1] - li[0]
        if result == 0 or result == 1:
            break
    print("#{} {}" .format(test_case, result))