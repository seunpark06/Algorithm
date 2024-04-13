from collections import deque
import sys
input = sys.stdin.readline

n , m = map(int, input().split())

graph = list([0] * (n + 1) for _ in range(n + 1))

for i in range(m):
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1

visited = [False] * (n + 1)

def bfs(v):
    q = deque()
    q.append(v)
    visited[v] = True

    while q:
        v = q.popleft()
        for i in range(1, n + 1):
            if graph[v][i] == 1 and not visited[i]: # 해당 노드를 방문하지 않고, v값과 연결이 되어 있으면
                q.append(i)
                visited[i] = True

count = 0
for k in range(1, n+1):
    if not visited[k]:
        bfs(k)
        count += 1

print(count)