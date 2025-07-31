import sys
input = sys.stdin.readline

def is_consecutive_increasing(s):
    for i in range(1, len(s)):
        if ord(s[i]) - ord(s[i - 1]) != 1:
            return False
    return True


n = int(input())
li = list(map(int, input().split()))
prod_set = set()
for i in range(n-1):
    for j in range(i+1,n):
        t = li[i] * li[j]
        if is_consecutive_increasing(str(t)):
            prod_set.add(li[i] * li[j])

print(max(prod_set) if prod_set else -1)