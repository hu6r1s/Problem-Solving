for test_case in range(10):
    n = int(input())
    li = [list(map(int, input().split())) for _ in range(100)]
    li2 = list(zip(*li))
    result = []
    count = 0
    for i in range(100):
        count += li[i][100-i-1]
    result.append(count)
    count = 0
    for i in range(100):
        count += li[i][i]
    result.append(count)
    for i in range(100):
        result.append(sum(li[i]))
        result.append(sum(li2[i]))

    print("#{} {}".format(n, max(set(result))))