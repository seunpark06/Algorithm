#다이나믹 프로그래밍 구현문제
def solution(land):
    dp = land 
    
    for i in range(1, len(dp)):
        for j in range(len(dp[0])):
            dp[i][j] += max(dp[i-1][:j] + dp[i-1][j+1:]) #직전 리스트 중 가장 큰 수를 더한 수
    
    answer = max(dp[len(dp)-1])

    return answer