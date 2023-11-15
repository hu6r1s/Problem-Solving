T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    r = 0
    result = 0
    for _ in range(n):
        li = list(map(int, input().split()))
        if li[0] == 1:
            r += li[1]
            result += r
        elif li[0] == 2:
            if r >= abs(r - li[1]):
                r -= li[1]
            else:
                r = 0
            result += r
        elif li[0] == 0:
            result += r
    print("#{} {}" .format(test_case, result))