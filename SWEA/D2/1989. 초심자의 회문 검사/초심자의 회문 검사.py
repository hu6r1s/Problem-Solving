T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    s = input()
    if s == s[::-1]:
        print("#{} 1".format(test_case))
    else:
        print("#{} 0".format(test_case))