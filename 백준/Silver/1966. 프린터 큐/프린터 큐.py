t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    lst = list(map(int, input().split()))

    enum = list(enumerate(lst))
    count = 0

    while True:
        if enum[0][1] == max(enum, key=lambda x: x[1])[1]:
            count += 1
            if m == enum[0][0]:
                print(count)
                break
            else:
                enum.pop(0)
        else:
            enum.append(enum.pop(0))