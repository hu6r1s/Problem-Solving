import math
import string

def convert(n, k):
    tmp = string.digits+string.ascii_lowercase
    q, r = divmod(n, k)
    if q == 0:
        return tmp[r]
    else:
        return convert(q, k) + tmp[r]
    
def isPrime(n):
    if n == 0 or n == 1:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True


def solution(n, k):
    count = 0
    a = convert(n, k)
    arr = a.split("0")
    for i in arr:
        if i and isPrime(int(i)):
            count += 1
    return count