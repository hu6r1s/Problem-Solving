d = {
    '0': 0,
    '1': 0,
    '2': 0,
    '3': 0,
    '4': 0,
    '5': 0,
    '6': 0,
    '7': 0,
    '8': 0,
    '9': 0
}

n = str(int(input()) * int(input()) * int(input()))
for i in n:
    d[i] += 1

print(*(d.values()), sep= "\n")