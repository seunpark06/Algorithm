from collections import deque

# 수빈의 위치 n, 동생의 위치 k
n, k = map(int, input().split())

MAX = 100000
# 좌표
graph = [0] * (MAX +1)

def bfs(x):
    q = deque()
    q.append(x)

    while q: #큐가 비어있을 때까지 순환
        x = q.popleft()
        #동생을 찾은 경우
        if x == k:
            print(graph[x])
            break

        for i in (x-1, x+1, x*2):
            if(i >= 0 and i <= MAX) and not graph[i]:
                q.append(i)
                graph[i] = graph[x] + 1

# print(graph)
bfs(n)


