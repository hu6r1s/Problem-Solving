def solution(n):
    result = 0
    
    for i in range(1, n+1):
        count = 0
        while count < n:
            count += i
            i += 1
            
            if count == n:
                result += 1
                break
        
    return result