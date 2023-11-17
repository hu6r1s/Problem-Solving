T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    string = input()
    a, b = 1, 1
    for s in string:
        if s == "L":
            a, b = a, a + b
        else:
            a, b = a + b, b
    print("#{} {} {}" .format(test_case, a, b))