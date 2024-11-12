n = int(input())
m = int(input())
p = ""
for i in range(2 * n + 1):
    if i % 2:
        p += "O"
    else:
        p += "I"

s = input()
cnt = 0
for i in range(m-len(p)+1):
    if p == s[i:len(p)+i]:
        cnt += 1

print(cnt)