n = int(input())

def hanoi(start, end, n):
    if n == 1:
        print(start, end)
        return
    hanoi(start, 6-start-end, n-1)
    print(start, end)
    hanoi(6-start-end, end, n-1)

print(2**n - 1)
hanoi(1, 3, n)