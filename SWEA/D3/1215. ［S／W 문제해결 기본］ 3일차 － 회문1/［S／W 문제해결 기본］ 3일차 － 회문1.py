for test_case in range(1, 11):
    s = 8
    n = int(input())
    li = [list(input()) for _ in range(s)]
    li2 = list(zip(*li))
    count = 0

    for i in range(s):
        for j in range(s - n + 1):
            if li[i][j:j + n] == li[i][j:j + n][::-1]:
                count += 1
            if li2[i][j:j + n] == li2[i][j:j + n][::-1]:
                count += 1

    print("#{} {}".format(test_case, count))