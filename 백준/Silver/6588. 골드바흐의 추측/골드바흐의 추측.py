import sys

prime = [True] * 1000001
prime[0] = prime[1] = False

for i in range(2, int(1000001**0.5)+1):
    if prime[i]:
        for j in range(i*i, 1000001, i):
            prime[j] = False

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break

    stop = False
    for i in range(3, n//2+1, 2):
        if prime[i] and prime[n-i]:
            print("{} = {} + {}".format(n, i, n-i))
            stop = True
            break

    if not stop:
        print("Goldbach's conjecture is wrong.")