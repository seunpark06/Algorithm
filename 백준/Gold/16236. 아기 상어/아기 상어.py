from collections import deque

n = int(input())

# 물고기 정보를 격자에 저장
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

# 아기상어의 이동좌표값
dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

# 상어의 시작 위치 찾기(9)
start = (0, 0)
for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            start = (i, j)
            graph[i][j] = 0  ## 9는 시작표시 확인용이므로 초기화해준다

# 상어의 시작 크기 2
size = 2
# 상어가 먹은 물고기의 수
ate = 0
# 엄마 상어를 호출하기까지의 시간
time = 0

while True:
    # 방문한 노드 기록
    visited = [[False] * n for _ in range(n)]
    visited[start[0]][start[1]] = True  # 시작 노드 방문표시
    # 먹을 수 있는 물고기 후보 리스트
    fish = []

    q = deque()
    q.append((start[0], start[1], 0))  # 좌표, 거리 형태로 저장

    #BFS 탐색
    while q:
        x, y, dist = q.popleft()  #좌표, 거리
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:  # 그래프 내 범위 안에 있고
                if graph[nx][ny] <= size and not visited[nx][ny]:  #이동 가능한 경우
                    q.append((nx, ny, dist + 1))
                    visited[nx][ny] = True
                    if 0 < graph[nx][ny] < size:  #먹을 수 있는 경우
                        fish.append((dist + 1, nx, ny)) #정렬을 위해 거리를 가장 앞 원소로 배치

    #BFS 탐색 후 먹을 수 있는 물고기가 없는 경우 끝
    if not fish:
        break

    # 물고기가 있는 경우
    fish.sort() #우선순위가 가장 높은 물고기
    d, fx, fy = fish[0] #거리와 좌표

    #물고기를 먹는다
    graph[fx][fy] = 0
    ate += 1
    start = (fx, fy) #여기서부터 다시 탐색한다
    time += d #이동한 거리만큼 시간이 증가한다

    # 물고기를 먹은 뒤 상어가 커지는지 확인
    if ate == size:
        size += 1
        ate = 0

print(time)
