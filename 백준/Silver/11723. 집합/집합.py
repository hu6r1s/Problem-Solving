import sys
input = sys.stdin.readline

m = int(input())
s = set()

for _ in range(m):
    lst = input().split()

    if lst[0] == "add":
        s.add(int(lst[1]))
    elif lst[0] == "remove":
        if int(lst[1]) in s:
            s.remove(int(lst[1]))
        else:
            pass
    elif lst[0] == "check":
        if int(lst[1]) in s:
            print(1)
        else:
            print(0)
    elif lst[0] == "toggle":
        if int(lst[1]) in s:
            s.remove(int(lst[1]))
        else:
            s.add(int(lst[1]))
    elif lst[0] == "all":
        s = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}
    elif lst[0] == "empty":
        s = set()