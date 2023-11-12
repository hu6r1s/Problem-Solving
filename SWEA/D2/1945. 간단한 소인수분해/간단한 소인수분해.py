def soinsu(n):
    answer = []
    
    x = 2
    while x <= n:
        if n % x == 0:
            answer.append(x)
            n //= x
        else:
            x += 1
    return answer

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    answer = soinsu(n)
    print("#{} {} {} {} {} {}" .format(test_case, answer.count(2), answer.count(3), answer.count(5), answer.count(7), answer.count(11)))