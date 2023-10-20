T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    n = int(input())
    s = list(map(int, input().split()))
    start = -1
    end = -1
    margin = 0
    while start < n - 1:
        max = 0
        for i in range(end+1, n):
            if s[i] > max:
                max = s[i]
                end = i

        for j in range(start+1, end):
            margin += (max - s[j])
        temp = end
        start = temp
    print("#{} {}" .format(test_case, margin))
    # ///////////////////////////////////////////////////////////////////////////////////
