T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    li = list(map(int, input().split()))
    avg = sum(li) / n
    count = 0
    for l in li:
        if l <= avg:
            count += 1

    print("#{} {}" .format(test_case, count))