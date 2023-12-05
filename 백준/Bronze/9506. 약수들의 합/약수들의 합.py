while True:
    n = int(input())
    li = []
    if n == -1:
        break
    for i in range(1, n):
        if n % i == 0:
            li.append(i)
    li.sort()
    if sum(li) == n:
        print(n, "=", " + ".join(map(str, li)))
    else:
        print(n, "is NOT perfect.")