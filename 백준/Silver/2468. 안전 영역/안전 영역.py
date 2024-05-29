import sys
input = sys.stdin.readline
from collections import deque

n = int(input())

# graph = [(n * [0]) for _ in range(n)]
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(k, x, y): # k = 장마철 비의 양
    q = deque()
    q.append((x, y))
    visited[x][y] = 1

    while q:
        x, y = q.popleft() #큐의 첫 번째 요소 출력

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx <0 or nx >= n or ny < 0 or ny >= n:
                continue

            if visited[nx][ny] == 0 and graph[nx][ny] > k: # 물에 잠기지 않은 영역이라면
                visited[nx][ny] = 1
                q.append((nx, ny))


rain_max = 0 # 최대 물높이
rain_min = 1
for i in range(n):
    rain_max = max(rain_max, max(graph[i]))

# 물높이에 따른 안전 영역의 갯수
temp = []
for r in range(0, rain_max):
    visited = [n*[0] for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0 and graph[i][j] > r:
                bfs(r, i, j)
                cnt += 1
    temp.append(cnt)

print(max(temp))