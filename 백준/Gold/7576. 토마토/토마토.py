from collections import deque

# 상자의 가로길이 m, 상자의 세로길이 n
m, n = map(int, input().split())

# 토마토 격자에 저장
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

# 상하좌우 방향 설정
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

q = deque()
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            q.append((i, j))

def bfs():
    while q: #큐가 비어있을때까지 순환
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 0:
                q.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1 #방문한 노드 표시

result = 0
bfs()
for p in graph: #안익은 토마토가 있으면
    for q in p:
        result = max(result, q)
        if q == 0:
            print(-1)
            exit(0)

print(result-1)