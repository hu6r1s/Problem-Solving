def count(arr):
    result = 0
    for li in arr:
        count = 0
        for j in range(len(li)):
            if li[j]:
                count += 1
            else:
            	if count == k:
                	result += 1
            	count = 0
    return result

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    li = [list(map(int, input().split())) + [0] for _ in range(n)] + [[0] * (n+ 1)]
    li2 = list(zip(*li))
	
    print("#{} {}" .format(test_case, count(li) + count(li2)))