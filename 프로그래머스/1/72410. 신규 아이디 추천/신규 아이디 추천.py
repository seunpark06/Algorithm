import re

def solution(new_id):
    answer = ''
    # 1. 모든 대문자를 소문자로 변환
    new_id = new_id.lower()
    # 2. 규칙에 맞지 않는 문자를 제거
    result = ''
    for i in new_id:
        if i.isalnum() or i in '-_.': #isalnum() => 알파벳, 숫자에 포함되는지 여부를 알려준다
            result += i
    new_id = result
    
    # 3. 마침표가 2번이상 연속된 부분을 하나의 마침표로 치환
    while ('..' in new_id):
        new_id = new_id.replace('..', '.')
        
    # 4. 마침표가 처음이나 끝에 위치한다면 제거
    if new_id[0:1] == '.': new_id = new_id[1:] 
    if new_id[-1:] == '.': new_id = new_id[:-1]
        
    # 5. new_id가 빈 문자열이라면 new_id에 'a' 대입
    if(len(new_id) == 0): new_id = 'a'
    
    # 6. new_id 길이가 16자 이상이면, 첫 15개의 문자 제외한 나머지 문자 제거
    # 제거 후 마침표가 new_id의 끝에 위치한다면 마침표 제거
    if(len(new_id) >= 16): new_id = new_id[0:15]
    if(new_id[-1:] == '.'): new_id = new_id[:-1]
    
    # 7. new_id 2자 이하라면, 마지막 문자를 길이가 3이 될 때까지 반복
    while len(new_id) <= 2: 
        last = new_id[-1:]
        new_id += last
        
    return new_id