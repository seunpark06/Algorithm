from collections import deque

#한 변의 길이
n = int(input())

#지도 저장
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

def bfs(x, y): #반환값 : 단지의 넓이 (count)
    # 좌표의 상하좌우 지정
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    q = deque()
    q.append((x, y))
    graph[x][y] = 0
    count = 1  # 한 단지 내에 있는 집의 수

    while q: #큐가 비어있을 때까지 순환

        x, y = q.popleft() #큐의 첫 번째 요소를 출력
        for i in range(4): #상하좌우 방향 체크
            nx = x + dx[i]
            ny = y + dy[i]

            if(nx <0 or nx >= n or ny < 0 or ny >= n): #지도범위에서 벗어나는지 체크
                continue
            #같은 단지에 있는 경우
            if(graph[nx][ny] == 1):
                graph[nx][ny] = 0  # 방문한 노드는 0으로 변환
                q.append((nx, ny))
                count += 1

    return count


cnt = [] #단지의 넓이를 저장함
for i in range(n):
    for j in range(n):
        if(graph[i][j] == 1):
            cnt.append(bfs(i, j))

cnt.sort()
print(len(cnt)) #단지가 몇개있는지 출력
for i in cnt:
    print(i)