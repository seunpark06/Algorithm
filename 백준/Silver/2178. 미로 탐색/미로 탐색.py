from collections import deque

# 최단거리 경로를 찾는 문제 => BFS(너비우선탐색)로 해결
n, m = map(int, input().split())
graph = []

# 미로 저장
for i in range(n):
    graph.append(list(map(int, input())))

def bfs(x, y):
    # 이동할 상, 하, 좌, 우 방향 정의
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    q = deque()
    q.append((x, y))
    while q: #큐가 비어있을 때까지 순환
        x, y = q.popleft() #큐의 첫번째 요소 출력
        # 현재 위치에서 상하좌우 4가지 방향 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로에서 벗어나면 안되므로 조건을 추가해줌
            if nx<0 or nx>= n or ny < 0 or ny >= m:
                continue
            # 지나갈 수 있는 경우
            if(graph[nx][ny] == 1):
                q.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1 #value 자체를 이동 횟수로 사용
                
    return graph[n-1][m-1]

print(bfs(0,0))



