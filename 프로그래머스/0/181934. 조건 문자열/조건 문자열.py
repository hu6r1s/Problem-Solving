def solution(ineq, eq, n, m):
    if n <= m and ineq == '<' and eq == '=':
        return 1
    elif n >= m and ineq == '>' and eq == '=':
        return 1
    elif n > m and ineq == '>' and eq == '!':
        return 1
    elif n < m and ineq == '<' and eq == '!':
        return 1
    else:
        return 0