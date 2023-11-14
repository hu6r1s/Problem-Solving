T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    result = []
    p, q, r, s, w = map(int,input().split())
    result.append(1 * p * w)
    if w <= r:
        result.append(q)
    else:
        result.append(q + 1 * s * (w -r))
    print("#{} {}" .format(test_case, min(result)))