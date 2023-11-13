T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    count = 0
    n = int(input())
    k = 1
    li = set()
    while True:
        for i in str(k * n):
            li.add(int(i))
        if len(li) == 10:
            break
        else:
            k += 1
    print("#{} {}" .format(test_case, k * n))