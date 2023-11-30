alpa = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
string = input()
count = 0
for a in alpa:
    if a in string:
        string = string.replace(a, "0")
print(len(string))