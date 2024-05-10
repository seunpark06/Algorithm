from collections import deque

def solution(dirs):
    answer = 0
    way_dict = { 'U': (0, 1), 'D': (0, -1), 'R': (1, 0), 'L':(-1, 0)}
    sets = set()
    x, y = 0, 0 #시작 위치 초기화
    
    for d in dirs:
        dx, dy = way_dict[d]
        nx = x + dx
        ny = y + dy
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            sets.add(((x,y), (nx, ny))) #이동 거리 (간선 저장)
            sets.add(((nx, ny), (x, y)))
            x = nx
            y = ny
            
    answer = len(sets)//2
    return answer