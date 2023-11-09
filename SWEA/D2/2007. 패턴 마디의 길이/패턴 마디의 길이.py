T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    s = input()
    c = ""
    for i in s:
        c += i
        if c == s[len(c):2 * len(c)]:
            print("#{} {}" .format(test_case, len(c)))
            break