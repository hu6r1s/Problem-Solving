T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    h1, m1, h2, m2 = map(int, input().split())
    h, m = h1 + h2, m1 + m2
    time = h * 60 + m
    h = time // 60
    if h > 12:
        h -= 12
    print("#{} {} {}" .format(test_case, h, time % 60))