T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    result = []
    if len(a) < len(b):
        for i in range(len(b)-len(a)+1):
            new_b = b[i:i+len(a)]
            count = 0
            for j in range(len(a)):
                count += a[j] * new_b[j]
            result.append(count)
    else:
        for i in range(len(a)-len(b)+1):
            new_a = a[i:i+len(b)]
            count = 0
            for j in range(len(b)):
                count += b[j] * new_a[j]
            result.append(count)
    print("#{} {}" .format(test_case, max(result)))