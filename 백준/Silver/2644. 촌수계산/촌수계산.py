from collections import deque
#촌수 == 그래프에서 두 정점 간 최단거리 이므로 bfs로 풀이

# 전체 사람의 수
n = int(input())

# 촌수를 계산해야 하는 서로 다른 두 사람의 번호 a, b
a, b = map(int, input().split())

# 관계의 개수 m
m = int(input())

#정점들의 연결 상태를 나타내는 행렬 그래프 생성
graph = [[]*(n+1) for _ in range(n + 1)]

# 정점 간 연결된 번호 표시
for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

#방문한 정점 기록
visited = [0] * (n+1)
distance = [0] * (n+1)

def bfs(v):
    q = deque()
    q.append(v)
    visited[v] = 1 #방문한 정점 표시

    while q:
        x = q.popleft()
        for i in graph[x]: #연결된 모든 노드 탐색
            if not visited[i]: #방문 안한경우
                visited[i] = 1 #방문 표시
                distance[i] = distance[x] + 1 #현재 촌수 + 1
                q.append(i)
bfs(a)

if distance[b] == 0:
    print(-1)
else:
    print(distance[b])