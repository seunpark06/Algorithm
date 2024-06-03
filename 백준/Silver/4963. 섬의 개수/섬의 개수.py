from collections import deque
import sys
input = sys.stdin.readline

# dx = [0, 0, -1, 1, 1, 1, -1, -1]
# dy = [1, -1, 0, 0, 1, -1, 1, -1]
dx = [1, -1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, -1, 1, -1, 1, 1, -1]

def bfs(x, y):
    q = deque()
    graph[x][y] = 2
    q.append((x, y))

    while q:
        x, y = q.popleft()

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= h or ny < 0 or ny >= w:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = 2  # 방문한 노드는 2로 표시
                q.append((nx, ny)) #큐에 추가


# test case가 여러개이므로
while True: # 계속해서 입력 받는다
    # 지도의 너비 w, 높이 h
    w, h = map(int, input().split())

    if w == 0 and h == 0: break # 탈출조건
    graph = [] # 지도
    for _ in range(h):
        graph.append(list(map(int, input().split())))

    count = 0 # 땅의 개수
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1: # 땅이라면
                bfs(i, j)
                count += 1
    print(count)




