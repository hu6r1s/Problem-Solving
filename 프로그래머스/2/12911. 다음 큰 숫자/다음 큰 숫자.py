def solution(n):
    bin_n = bin(n)
    while True:
        n += 1
        next_bin = bin(n)
        if next_bin.count("1") == bin_n.count("1"):
            return n