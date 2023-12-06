n = int(input())
pot_x = []
pot_y = []
for i in range(n):
    x, y = map(int, input().split())
    pot_x.append(x)
    pot_y.append(y)

print((max(pot_x) - min(pot_x)) * (max(pot_y) - min(pot_y)))