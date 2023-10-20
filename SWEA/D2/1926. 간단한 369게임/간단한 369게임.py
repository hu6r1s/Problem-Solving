n = int(input())
l = []
for i in range(1, n + 1):
    l.append(i)

for i in l:
    c = 0
    if "3" in str(i) or "6" in str(i) or "9" in str(i):
        c += str(i).count("3")
        c += str(i).count("6")
        c += str(i).count("9")
        print("-" * c, end=" ")
    else:
        print(i, end=" ")