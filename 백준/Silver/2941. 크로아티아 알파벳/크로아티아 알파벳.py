alpa = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

s= input()

for i in alpa:
    s = s.replace(i, "*")
print(len(s))