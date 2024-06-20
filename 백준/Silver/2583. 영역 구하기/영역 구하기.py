from collections import deque

m, n, k = map(int, input().split())
graph = [[0] * m for _ in range(n)]
visited = [[0] * m for _ in range(n)]

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            graph[i][j] = 1
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

area_arr = []  #각 영역의 넓이 저장

 #넓이
def bfs(x, y):
    q = deque()
    q.append((x, y))
    area_num = 1
    while q:  #큐가 비어 있을 때까지 순환
        x, y = q.popleft()
        visited[x][y] = 1 #방문 노드 표시

        for i in range(4):  # 좌표의 상하좌우 탐색
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:  #좌표를 벗어나는 범위
                continue
            if graph[nx][ny] == 0 and visited[nx][ny] == 0:  #방문한 적 없는 빈칸일때
                q.append((nx, ny))
                visited[nx][ny] = 1  # 방문한 노드는 1로 변경
                area_num += 1
    return area_num

for p in range(n):
    for q in range(m):
        if graph[p][q] == 0 and visited[p][q] == 0: #빈 영역이라면
            area_arr.append(bfs(p, q))

print(len(area_arr))  #분리된 영역의 수
area_arr.sort()
for a in area_arr:
    print(a, end=' ')

