def solution(x):
    
    zari_sum = 0
    for s in str(x):
        zari_sum += int(s)
    
    
    if(x % zari_sum == 0):
        return True
    else:
        return False
    return 0
    