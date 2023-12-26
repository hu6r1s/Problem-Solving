import sys
from itertools import permutations
input = sys.stdin.readline

print(len(list(permutations([i for i in range(int(input()))], 2))))