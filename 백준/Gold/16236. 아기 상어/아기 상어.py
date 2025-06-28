from collections import deque

n = int(input())

# 물고기 정보를 지도에 저장
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

size = 2
ate = 0
time = 0

# 이동할 수 있는 좌표
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# 아기 상어의 시작 위치 찾기
start = (0,0)
for x in range(n):
    for y in range(n):
        if graph[x][y] == 9:
            start = (x,y)
            graph[x][y] = 0 #상어의 시작 위치 초기화


while True:
# 초기화 로직
    visited = [[False] * n for _ in range(n)]
    q = deque()
    q.append((start[0], start[1], 0)) # 좌표, 거리
    visited[start[0]][start[1]] = True
    fish_list = []

    while q:
        x, y, dist = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 그래프 내에 있으면서 방문하지 않은 좌표
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if graph[nx][ny] <= size: #지나갈 수 있는 좌표
                    q.append((nx, ny, dist + 1)) #좌표, 거리
                    visited[nx][ny] = True
                    if 0 < graph[nx][ny] < size:
                        fish_list.append((dist+1, nx, ny)) #튜플 형태로 집어넣어주어야함

    if not fish_list: #BFS 순회 후 더 먹을 물고기가 없다면
        break

    fish_list.sort() #제일 가까운 거리 순으로 물고기 정렬
    d, fx, fy = fish_list[0]

    #물고기를 먹는다
    graph[fx][fy] = 0 #먹은 물고기가 있던 좌표를 비운다
    start = (fx, fy) #상어를 이동시킨다 (여기서부터 다시 탐색)
    time += d #이동거리만큼 시간을 증가시킨다
    ate += 1 #물고기 먹은 갯수 증가
    if ate == size: #상어가 크는지 확인
        size += 1
        ate = 0

print(time)
