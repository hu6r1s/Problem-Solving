T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    li = [list(map(int, input().split())) for _ in range(n)]
    result = 0
    for i in range(n):
        count = 0
        for j in range(n):
            if li[i][j] == 1:
                count += 1
            if li[i][j] == 0 or j == n - 1:
                if count == k:
                    result += 1
                count = 0
                
        for j in range(n):
            if li[j][i] == 1:
                count += 1
            if li[j][i] == 0 or j == n - 1:
                if count == k:
                    result += 1
                count = 0
	
    print("#{} {}" .format(test_case, result))