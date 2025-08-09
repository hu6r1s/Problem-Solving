import sys
input = sys.stdin.readline

s = input().strip()
cnt = dict()
for i, cow in enumerate(s):
    if cow not in cnt:
        cnt[cow] = [i]
    else:
        cnt[cow].append(i)

cows = list(cnt.keys())
result = 0
for i in range(len(cows)):
    for j in range(i+1, len(cows)):
        a1, a2 = cnt[cows[i]]
        b1, b2 = cnt[cows[j]]

        if a1 < b1 < a2 < b2 or b1 < a1 < b2 < a2:
            result += 1

print(result)