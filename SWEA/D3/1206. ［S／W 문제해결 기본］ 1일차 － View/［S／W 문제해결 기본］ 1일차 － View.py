for test_case in range(1, 11):
    n = int(input())
    li = list(map(int, input().split()))
    count = 0
    for i in range(2, n - 2):
        if li[i] > li[i+1] and li[i] > li[i+2] and li[i] > li[i-1] and li[i] > li[i-2]:
            count += li[i] - max(max(li[i-1], li[i-2]), max(li[i+1], li[i+2]))
    print("#{} {}" .format(test_case, count))