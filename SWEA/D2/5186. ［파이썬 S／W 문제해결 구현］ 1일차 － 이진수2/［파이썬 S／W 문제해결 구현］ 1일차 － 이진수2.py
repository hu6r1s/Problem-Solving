def sosu_bin(n):
    bin = ""
    while len(bin) <= 12:
        n *= 2
        s = str(n).split(".")
        bin += s[0]
        
        if not int(s[1]):
            return bin
        n = float('0.' + s[1])
    else:
        return 'overflow'
    

T = int(input())
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    n = float(input())
    print("#{} {}".format(test_case, sosu_bin(n)))
    # ///////////////////////////////////////////////////////////////////////////////////
