t = int(input())
for _ in range(t):
    s = ""
    string = "abcdefghijklmnopqrstuvwxyz"
    n = int(input())
    li = list(map(int, input().split()))
    for i in range(n):
        s += string[li[i]]
        string = string[li[i]] + string.replace(string[li[i]], "")
    print(s)