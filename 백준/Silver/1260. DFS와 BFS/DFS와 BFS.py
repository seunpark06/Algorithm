from collections import deque
## DFS 깊이 우선 탐색, 멀리 있는 노드 우선 탐색 (Stack 사용)
## BFS 가까운 노드부터 탐색 (Queue 사용)

##BOJ 1260, BFS와 DFS 구현

## 정점의 개수 N, 간선의 개수 M, 탐색 시작 번호 V
n, m, v = map(int, input().split())

## 노드 정보가 담긴 행렬 그래프
graph = [ [0] * (n + 1) for _ in range(n+1) ]

# 각 정점의 연결 정보 저장
for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1 #연결된 정점 표시
    graph[b][a] = 1

visited1 = [0] * (n+1) #dfs 방문기록
visited2 = [0] * (n+1) #bfs 방문기록

# 깊이 우선 탐색
# 깊게 탐색하는 과정이므로 재귀함수 이용
# 현재 노드에서 연결된 노드가 있으면 더 탐색한다
def dfs(x):
    visited1[x] = 1 #방문한 노드 표시
    print(x, end=" ")
    for i in range(1, n+1): #현재 방문한 노드(x)에서 연결된 노드가 있는지 확인한다
        if visited1[i] == 0 and graph[i][x]: #방문하지 않은 노드가 연결되어 잇으면
            dfs(i)

def bfs(x):
    q = deque([x])
    visited2[x] = 1 # 방문한 노드 표시

    while q: #큐가 비어있을때까지 계속 탐색한다
        v = q.popleft()
        print(v, end=" ") #방문한 노드 출력

        for i in range(1, n+1):
            if visited2[i] == 0 and graph[i][v]: #방문하지 않은 노드 중 연결된 노드가 있는 경우
                q.append(i)
                visited2[i] = 1 #방문 처리


dfs(v)
print()
bfs(v)