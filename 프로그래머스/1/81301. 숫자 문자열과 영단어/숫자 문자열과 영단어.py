def solution(s):
    answer = 0
    num_dict = {'one':'1', 
                'two':'2',
                 'three':'3',
                 'four':'4',
                 'five':'5',
                 'six':'6',
                 'seven':'7',
                 'eight':'8',
                 'nine':'9',
                 'zero':'0'}
    for index, num in enumerate(num_dict):
        if num in s:
            s = s.replace(num, num_dict[num])
            
    return int(s)