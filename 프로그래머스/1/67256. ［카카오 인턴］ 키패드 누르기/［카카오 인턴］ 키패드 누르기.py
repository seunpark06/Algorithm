## 두 좌표간 거리 계산하는 함수
def dist(point1, point2):
    x1 = point1[0]
    y1 = point1[1]
    x2 = point2[0]
    y2 = point2[1]
    
    return abs(y2 -y1) + abs(x2 - x1)
def solution(numbers, hand):
    answer = ''
    
    ## 키패드에 가상의 좌표를 부여하여 거리 계산
    key_dict = {'1':[0,0], '2':[1,0], '3':[2,0], '4':[0,1],
               '5':[1,1], '6':[2,1], '7':[0,2], '8':[1,2],
               '9':[2,2], '*':[0,3], '0':[1,3], '#':[2,3]}
    left = [1, 4, 7]
    right = [3, 6, 9]
    # 왼손 엄지의 위치
    l_cur = [0,3]
    # 오른손 엄지의 위치
    r_cur = [2,3]

    for index, num in enumerate(numbers):
        if(num in left):
            answer += 'L'
            l_cur = key_dict[str(num)]
        elif(num in right):
            answer += 'R'
            r_cur = key_dict[str(num)]
        else: 
            if dist(key_dict[str(num)], l_cur) > dist(key_dict[str(num)], r_cur):
                answer += 'R'
                r_cur = key_dict[str(num)]
            elif dist(key_dict[str(num)], l_cur) < dist(key_dict[str(num)], r_cur):
                answer += 'L'
                l_cur = key_dict[str(num)]
            else:
                answer += hand[0:1].upper()
                if(hand[0:1].upper() == 'L'):
                    l_cur = key_dict[str(num)]
                else:
                    r_cur = key_dict[str(num)]
                
                
            
    return answer