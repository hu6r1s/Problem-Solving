n, m = map(int, input().split())
basket = [0 for _ in range(n+1)]
for _ in range(m):
    i, j, k = map(int, input().split())
    for b in range(i, j+1):
        basket[b] = k
for b in range(1, len(basket)):
    print(basket[b], end=" ")