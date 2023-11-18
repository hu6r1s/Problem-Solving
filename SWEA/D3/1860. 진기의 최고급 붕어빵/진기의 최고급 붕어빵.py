T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, m, k = map(int, input().split())
    arrive = list(map(int, input().split()))
    arrive.sort()
    count = 0
    string = "Possible"

    for t in arrive:
        count += 1
        if (t // m) * k < count:
            string = "Impossible"
            break
    print("#{} {}".format(test_case, string))