def solution(people, limit):
    people.sort()
    start = 0
    end = len(people) -1
    answer = 0
    #사람들을 몸무게순으로 정렬한뒤 가장 가벼운사람과 가장 무거운 사람을 태운다
    while start <= end:
        if people[start] + people[end] <= limit:
            start += 1
            end -= 1
        else: #무게를초과한다면 무거운사람만 태운다
            end -=1
            
        answer += 1
    return answer