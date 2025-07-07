n, f = input(), input()
n = n[:-2] + "00"

while True:
    if int(n) % int(f) == 0:
        break
    n = str(int(n) + 1)
print(n[-2:])