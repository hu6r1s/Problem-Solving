def solution(citations):
    citations.sort(reverse=True)
    i = 0
    for c in citations:
        if i >= c:
            return i
        i += 1
    return len(citations)