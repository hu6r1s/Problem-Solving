def solution(n, arr1, arr2):
    a = []
    for i in range(n):
        s = bin(arr1[i] | arr2[i])[2:].zfill(n)
        tmp = ''
        for j in s:
            if j == '1':
                tmp += '#'
            else:
                tmp += ' '
        print(tmp)
        a.append(tmp)
    return a