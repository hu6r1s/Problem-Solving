i = 1
size = 1.86 * (10 ** 6)
while True:
    s = int(input())

    if s == 0:
        break

    s //= 2
    s += s // 2
    print(f"File #{i}")
    print(f"John needs {int(s // size) + 1} floppies.", end="\n\n")
    i += 1