import sys
import math
input = sys.stdin.readline

def star(n):
  if n == 1:
    return ['*']

  stars = star(n//3)
  L=[]

  for s in stars:
    L.append(s*3)
  for s in stars:
    L.append(s+' '*(n//3)+s)
  for s in stars:
    L.append(s*3)

  return L

n = int(input())
print('\n'.join(star(n)))