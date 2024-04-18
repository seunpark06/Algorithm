def solution(want, number, discount):
    answer = 0
    want_list = []
    for w, n in zip(want, number):
        for _ in range(n):
            want_list.append(w)
    want_list.sort()
    
    sales = []
    for d in range(len(discount)-9):
        sales = discount[d:d+10]
        sales.sort()
        if sales == want_list:
            answer += 1
    
    return answer