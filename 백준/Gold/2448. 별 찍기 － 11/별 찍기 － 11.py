n = int(input())
stars = [[" "]*(2*n-1) for _ in range(n)]
def solve(x, y, n):
    if n == 3:
        stars[x][y] = "*"
        stars[x+1][y-1] = "*"
        stars[x+1][y+1] = "*"
        for j in range(y-2, y+3):
            stars[x+2][j] = "*"
        return
    solve(x, y, n//2)
    solve(x+n//2, y-n//2, n//2)
    solve(x+n//2, y+n//2, n//2)

solve(0, n-1, n)
for star in stars:
    print("".join(star))