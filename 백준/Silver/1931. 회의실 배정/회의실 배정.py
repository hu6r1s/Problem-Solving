n = int(input())
meet = [list(map(int, input().split())) for _ in range(n)]
meet.sort(key=lambda x: (x[1], x[0]))
count = 0
a = 0
for i, j in meet:
  if i >= a:
    count += 1
    a = j
print(count)