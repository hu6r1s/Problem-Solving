lst = list(map(int, input().split()))
result = all(i == 1 or i == 0 for i in lst)
print('S' if result else 'F')