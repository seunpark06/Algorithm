def solution(players, callings):
    result = {player: i for i, player in enumerate(players)}
    for person in callings:
        index = result[person] ## 호명된 선수의 등수
        result[person] -= 1
        result[players[index-1]] += 1
        
        players[index], players[index-1] = players[index-1], players[index] ## 추월한 선수의 위치 교환
        
        
    answer = players
    return answer