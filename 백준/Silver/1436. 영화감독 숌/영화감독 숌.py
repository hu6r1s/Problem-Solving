n = int(input())
count = 0
m = 666
while True:
    if '666' in str(m):
        count += 1
    if count == n:
        print(m)
        break
    m += 1