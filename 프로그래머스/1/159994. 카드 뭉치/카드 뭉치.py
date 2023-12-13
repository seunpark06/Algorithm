import queue

def solution(cards1, cards2, goal):
    queue1 = cards1
    queue2 = cards2
    answer = 'Yes'
    for word in goal:
        if(len(queue1) != 0 and queue1[0] == word):
            queue1.pop(0)
        elif(len(queue2) != 0 and queue2[0] == word):
            queue2.pop(0)
        else:
            answer = 'No'
    
    return answer