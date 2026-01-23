s, p = map(int, input().split())
dna = list(input())
limit_cnt = list(map(int, input().split()))
limit_word = {
    "A": limit_cnt[0],
    "C": limit_cnt[1],
    "G": limit_cnt[2],
    "T": limit_cnt[3]
}
cnt = 0

check = dict.fromkeys('ACGT', 0)

for i in range(p):
    check[dna[i]] += 1

if (check["A"] >= limit_word["A"] and
    check["C"] >= limit_word["C"] and
    check["G"] >= limit_word["G"] and
    check["T"] >= limit_word["T"]):
    cnt += 1

for i in range(p, s):
    check[dna[i]] += 1
    check[dna[i-p]] -= 1

    if (check["A"] >= limit_word["A"] and
            check["C"] >= limit_word["C"] and
            check["G"] >= limit_word["G"] and
            check["T"] >= limit_word["T"]):
        cnt += 1

print(cnt)