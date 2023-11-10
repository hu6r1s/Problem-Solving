T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    r = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    money = {
        50000: 0,
        10000: 0,
        5000: 0,
        1000: 0,
        500: 0,
        100: 0,
        50: 0,
        10: 0,
	}
    
    for i in r:
        if n // i:
            money[i] += n // i
            n %= i
    print("#{}".format(test_case))
    for _, value in money.items():
        print(value, end=" ")
    print()