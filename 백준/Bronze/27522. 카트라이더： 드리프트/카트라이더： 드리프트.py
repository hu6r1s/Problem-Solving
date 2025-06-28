teams = []

for _ in range(8):
    time, team = input().split()
    M, S, s = map(int, time.split(":"))
    teams.append([(M, S, s), team])

teams.sort(key=lambda x: x[0])
R_cnt = 0
B_cnt = 0
cnt = {0: 10, 1: 8, 2: 6, 3: 5, 4: 4, 5: 3, 6: 2, 7: 1}
for i in range(8):
    if teams[i][1] == "R":
        R_cnt += cnt[i]
    else:
        B_cnt += cnt[i]

print("Red" if R_cnt > B_cnt else "Blue")