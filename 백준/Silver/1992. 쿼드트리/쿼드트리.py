n = int(input())

graph = [list(map(int, list(input()))) for _ in range(n)]
result = ""

def solve(x, y, k):
    global result
    for i in range(x, x+k):
        for j in range(y, y+k):
            if graph[x][y] != graph[i][j]:
                result += "("
                solve(x, y, k//2)
                solve(x, y+k//2, k//2)
                solve(x+k//2, y, k//2)
                solve(x+k//2, y+k//2, k//2)
                result += ")"
                return
    if graph[x][y]:
        result += "1"
    else:
        result += "0"


solve(0, 0, n)
print(result)