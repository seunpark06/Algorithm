# 모든 노드를 탐험하고자 하는 경우는 DFS를 사용한다
# DFS 는 주로 stack 또는 재귀함수 사용
answer = 0

def dfs(k, cnt, dungeons, visited):
    global answer
    answer = max(answer, cnt)
    
    for i in range(len(dungeons)):
        if visited[i] == 0 and k >= dungeons[i][0]: #현재 피로도가 최소 피로도보다 크다면
            visited[i] = 1
        
            dfs(k-dungeons[i][1], cnt + 1, dungeons, visited)
            visited[i] = 0 #이전 노드로 back할때 방문 노드를 초기화시켜준다
    
def solution(k, dungeons): #현재 피로도와 던전 배열이 주어짐
    global answer
    visited = len(dungeons) * [0] # 방문한 던전 기록
    
    dfs(k, 0, dungeons, visited) #현재 피로도, 방문한 던전 개수, 던전 배열,방문한 던전 기록
    
    return answer

