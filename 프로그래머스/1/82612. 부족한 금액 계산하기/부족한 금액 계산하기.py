def solution(price, money, count):
    answer = -1
    total = 0
    for i in range(1, count+1):
        total = total + price * i
    
    if(total > money):
        return total - money
    else:
        return 0

    