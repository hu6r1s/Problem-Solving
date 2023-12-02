n = int(input())
init = 1
count = 1
while init < n:
    init += count * 6
    count += 1
print(count)