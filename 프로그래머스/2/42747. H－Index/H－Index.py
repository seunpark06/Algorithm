def solution(citations):
    answer = 0
    citations.sort(reverse = True)
    for i, c in enumerate(citations):
        if i+1 > c:
            return i
    return len(citations)