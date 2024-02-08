n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]
count = {0: 0, 1: 0}

def solve(x, y, k):
    for i in range(x, x+k):
        for j in range(y, y+k):
            if graph[x][y] != graph[i][j]:
                c = k // 2
                for a in range(2):
                    for b in range(2):
                        solve(x+a*c, y+b*c, c)
                return
    count[graph[x][y]] += 1


solve(0, 0, n)
print(count[0])
print(count[1])