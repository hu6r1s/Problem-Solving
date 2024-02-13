def solution(n, left, right):
    result = []
    for i in range(left, right+1):
        mx = max(i//n, i%n)+1
        result.append(mx)
    return result