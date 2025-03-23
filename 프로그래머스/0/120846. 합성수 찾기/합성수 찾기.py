def yaksu(n):
    a = []
    for i in range(1, n+1):
        if not n % i:
            a.append(i)
    return a

def solution(n):
    count = 0
    for i in range(1, n+1):
        if len(yaksu(i)) >= 3:
            count += 1
    return count