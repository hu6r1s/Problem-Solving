n = int(input())
first = list(input())
li = [list(input()) for _ in range(n-1)]
for word in li:
    for i in range(len(first)):
        if first[i] != word[i]:
            first[i] = "?"

print("".join(first))