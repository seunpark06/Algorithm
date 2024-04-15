import copy
from collections import deque

n = int(input())

graph = []
for _ in range(n):
    graph.append(list(input()))

w_graph = copy.deepcopy(graph)
for i in range(n):
    for j in range(n):
        if(w_graph[i][j] == 'R'):
            w_graph[i][j] = 'G'

#상하좌우 좌표 표시
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

visited1 = [[0] * (n*1) for i in range(n)]
visited2 = [[0] * (n*1) for i in range(n)]

#적록색약이 아닌 사람이 보는 구역의 수
def bfs(i, j):
    q = deque()
    q.append((i, j))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if(nx < 0 or nx >= n or ny < 0 or ny >= n):
                continue
            if graph[x][y] == graph[nx][ny] and visited1[nx][ny] == 0: #같은 구역이 있다면
                q.append((nx, ny))
                visited1[nx][ny] = 1 # 방문 기록

def color_weak(i, j):
    q = deque()
    q.append((i, j))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if(nx < 0 or nx >= n or ny < 0 or ny >= n):
                continue
            if w_graph[x][y] == w_graph[nx][ny] and visited2[nx][ny] == 0: #같은 구역이 있다면
                q.append((nx, ny))
                visited2[nx][ny] = 1 # 방문 기록
cnt1 = 0
cnt2 = 0
for i in range(n):
    for j in range(n):
        if visited1[i][j] == 0:
            bfs(i, j)
            cnt1 += 1
        if visited2[i][j] == 0:
            color_weak(i, j)
            cnt2 += 1

print(cnt1, cnt2)