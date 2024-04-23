answer = 0
alphabet = ['A', 'E', 'I', 'O', 'U']
def dfs(target, string):
    global answer
    answer += 1
    if target == string:
        return True
    if len(string) == 5:
        return False
    
    for a in alphabet:
        if dfs(target, string + a):
            return True
        
def solution(word):
    global answer
    for i in alphabet:
        if dfs(word, i):
            return answer
