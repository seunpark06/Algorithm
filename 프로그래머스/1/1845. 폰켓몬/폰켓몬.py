from collections import Counter

def solution(nums):
    n_counter = Counter(nums) ## 폰켓몬의 종류
    max_num = len(nums)/2  ## 가질 수 있는 폰켓몬의 수
    if len(n_counter) <= max_num: ## 폰켓몬 종류가 2/N 개보다 적은 경우
        answer = len(n_counter)
    else:
        answer = max_num
    return answer