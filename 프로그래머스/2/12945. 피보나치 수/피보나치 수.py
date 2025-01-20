def fibo(num):
    if num <= 1:
        return num
    else:
        return fibo(num-1) + fibo(num-2)
    
def solution(n):
    pre = 0
    cur = 1
    for i in range(n-1):
        temp = cur
        cur = pre + cur
        pre = temp
    
    answer = cur % 1234567
    return answer