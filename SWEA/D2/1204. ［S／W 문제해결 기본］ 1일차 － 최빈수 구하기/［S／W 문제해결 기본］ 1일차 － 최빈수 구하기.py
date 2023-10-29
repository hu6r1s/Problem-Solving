T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    count = [0] * 1001
    nums = list(map(int, input().split()))
    for i in nums:
        count[i] += 1
    result = []
    for i in range(len(count)):
        if count[i] == max(count):
            result.append(i)
    print("#{} {}".format(test_case, max(result)))