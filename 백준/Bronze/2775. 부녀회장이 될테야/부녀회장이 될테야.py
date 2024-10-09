T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())
    init = [i for i in range(1, n+1)]

    for _ in range(k):
        for i in range(1, n):
            init[i] += init[i-1]
    print(init[-1])