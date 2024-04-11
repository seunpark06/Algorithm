# 백준 1260번
from collections import deque

#DFS는 보통 재귀함수로 구현한다
#BFS는 보통 queue로 구현한다

# 정점의 개수 n, 간선의 개수 m, 탐색을 시작할 정점의 번호 v
n, m, v = map(int, input().split())

graph = [[False] * (n+1) for i in range(n + 1)]

for k in range(m):
    a,b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True

visited1 = [False] * (n+1) # dfs의 방문기록
visited2 = [False] * (n+1) # bfs의 방문기록

# 너비 우선 탐색
def bfs(V):
    q = deque([V])
    visited2[V] = True #방문 처리

    while q: #q가 비어있을때까지 계속 순환한다
        v = q.popleft() #큐에 있는 첫번째 값을 꺼낸다
        print(v, end=" ")
        for i in range(1, n+1):
            if not visited2[i] and graph[i][v]: #해당 i값을 방문하지 않았고, v와 연결이 되어 있다면
                q.append(i)
                visited2[i] = True
# 깊이 우선 탐색
def dfs(V):
    visited1[V] = True
    print(V, end=" ")
    for i in range(1, n+1):
        if not visited1[i] and graph[i][V]: #해당 i값을 방문하지 않았고, v와 연결이 되어 있다면
            dfs(i)

dfs(v)
print()
bfs(v)