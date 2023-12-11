n = list(input())
li = list(map(int, n))
li.sort(reverse=True)
print("".join(map(str, li)))