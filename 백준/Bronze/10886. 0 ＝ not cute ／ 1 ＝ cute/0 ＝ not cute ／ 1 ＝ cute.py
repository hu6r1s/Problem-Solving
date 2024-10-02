n = int(input())
lst = []

for _ in range(n):
    lst.append(int(input()))

if lst.count(0) > lst.count(1):
    print("Junhee is not cute!")
elif lst.count(0) < lst.count(1):
    print("Junhee is cute!")