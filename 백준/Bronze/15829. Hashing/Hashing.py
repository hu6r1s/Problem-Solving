l = int(input())
lst = list(input())
rst = 0

for i in range(l):
    rst += (ord(lst[i]) - 96) * 31 ** i

print(rst % 1234567891)