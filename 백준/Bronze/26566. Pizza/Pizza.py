n = int(input())
for _ in range(n):
    a1, p1 = map(int, input().split())
    r1, p2 = map(int, input().split())

    a1, p1 = a1 * 8, p1 * 8
    r1 = r1 ** 2 * 3.14

    print("Slice of pizza" if a1/p1 > r1/p2 else "Whole pizza")