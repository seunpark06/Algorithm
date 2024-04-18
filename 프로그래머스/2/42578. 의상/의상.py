def solution(clothes):
    clo_dict = { c[1]:0 for c in clothes }
    for c in clothes:
        k = c[1]
        clo_dict[k] += 1
    
    nums = list(clo_dict.values())
    answer = nums[0] + 1
    for num in range(len(nums)-1):
        answer = answer * (nums[num + 1] + 1)
    return answer -1