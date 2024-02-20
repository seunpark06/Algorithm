
def solution(number, limit, power):
    div = [1]
    
    for i in range(2, number+1):
        count = 0
        ## 시간초과가 되지 않도록 범위를 제곱근까지로 지정
        for num in range(1, int(i**(1/2)+1)):
            if(i % num == 0):    
                count += 1
                if(num ** 2 != i):
                     count += 1
        if(count > limit):
            div.append(power)
        else:
            div.append(count)
    
    return sum(div)