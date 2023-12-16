a1, b1 = map(int, input().split())
a2, b2 = map(int, input().split())
c1, c2 = a1*b2+a2*b1, b1*b2
while c1 % c2 != 0:
    c1, c2 = c2, c1 % c2
print((a1*b2+a2*b1)//c2, b1*b2//c2)