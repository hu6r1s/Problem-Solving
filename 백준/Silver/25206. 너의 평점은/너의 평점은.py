l1 = []
dic = {
    "A+": 4.5,
    "A0": 4.0,
    "B+": 3.5,
    "B0": 3.0,
    "C+": 2.5,
    "C0": 2.0,
    "D+": 1.5,
    "D0": 1.0,
    "F": 0.0
}
result = 0
sum = 0

for _ in range(20):
    l1.append(input().split())

for i in range(20):
    if l1[i][2] != "P":
        result += float(l1[i][1]) * float(dic[l1[i][2]])
        sum += float(l1[i][1])

print(round(result/sum, 6))