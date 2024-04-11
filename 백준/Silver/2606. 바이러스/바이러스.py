from collections import deque

# 전체 노드 탐색 -> DFS 재귀함수 이용

#컴퓨터의 수 n
n = int(input())

#간선의 수 m
m = int(input())

graph = [[False] * (n+1) for i in range(0, n+1)]
for k in range(m):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True

#방문한 노드 기록
visited = [False] * (n + 1)
result = 0
def dfs(v):
    global result
    visited[v] = True
    result += 1
    for i in range(1, n + 1):
        if not visited[i] and graph[v][i]: #방문하지 않은 노드가 해당 노드와 연결이 되어 있다면
            dfs(i)

dfs(1)
print(result -1) #1번 컴퓨터 제외