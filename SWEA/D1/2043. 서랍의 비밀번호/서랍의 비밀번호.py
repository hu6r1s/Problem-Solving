p, k = map(int, input().split())
count = 1

while p != k:
    k += 1
    count += 1
print(count)