answer = 0
def dfs(n, total, numbers, target): # 현재까지 더한 정수들의 수 n, 정수의 합 total
    global answer
    if n == len(numbers):
        if total == target:
            answer += 1
            return
        return
    dfs(n +1, total + numbers[n], numbers, target)
    dfs(n +1, total - numbers[n], numbers, target)
    

def solution(numbers, target):
    global answer
    
    dfs(0, 0, numbers, target)
    return answer