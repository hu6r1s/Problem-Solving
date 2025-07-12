import copy

n, m = map(int, input().split())

graph = [list(input()) for _ in range(n)]
result = copy.deepcopy(graph)

for i in range(n-1):
    for j in range(m-1):
        if graph[i][j] == "#":
            result[i][j] = "#"
            result[i+1][j] = "#"
            result[i+1][j+1] = "#"
            result[i][j+1] = "#"

for i in result:
    print("".join(i))