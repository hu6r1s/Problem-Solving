s = input()
li = set()
for i in range(len(s)):
    for j in range(i, len(s)):
        li.add(s[i:j+1])
print(len(li))