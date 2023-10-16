import string

tmp = string.digits + string.ascii_uppercase
n, b = map(int, input().split())

def convert(num, base):
    q, r = divmod(num, base)
    if q == 0:
        return tmp[r]
    else:
        return convert(q, base) + tmp[r]

print(convert(n, b))