def palindrome(li, v):
    for l in li:
        for i in range(n-v+1):
            if l[i:i+v] == l[i:i+v][::-1]:
                return True
    return False


T = 10
for test_case in range(1, T+1):
    _ = int(input())
    n = 100
    li = [list(input()) for _ in range(n)]
    li2 = list(zip(*li))

    for i in range(n, 1, -1):
        if palindrome(li, i) or palindrome(li2, i):
            break

    print("#{} {}".format(test_case, i))