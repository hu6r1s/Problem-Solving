n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]
count = {-1: 0, 0: 0, 1: 0}

def solve(x, y, z):
    for i in range(x, x+z):
        for j in range(y, y+z):
            if graph[x][y] != graph[i][j]:
                for i in range(3):
                    for j in range(3):
                        solve(x+i*(z//3), y+j*(z//3), z//3)
                return
    count[graph[x][y]] += 1


solve(0, 0, n)
print(count[-1])
print(count[0])
print(count[1])