import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a, b = dict(), dict()
count = 0
li = list(input().split())
for i in li:
    a[i] = True
li = list(input().split())
for i in li:
    b[i] = True

for i in a.keys():
    if i in b.keys():
        count += 1
print((len(a)-count) + (len(b)-count))