import math

n = int(input())
f = str(math.factorial(n))
rev_f = str(int(f[::-1]))
print(len(f) - len(rev_f))