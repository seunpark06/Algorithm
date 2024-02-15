def solution(s, skip, index):
    list_s = list(s)
       
    ## index 사용하기위해 enumerate 사용
    for (idx, letter) in  enumerate(s):
        ## ascii 코드 변환 함수
        ascii_s = ord(letter)
        for i in range(0, index):
            ascii_s += 1
            ## 문자열 z + 1인경우 a로 바꿔준다
            if(ascii_s == 123):
                ascii_s = 97
            ##skip 안에 있는경우 한번더 증가
            while(chr(ascii_s) in skip):
            ##if(chr(ascii_s) in skip):                
                ascii_s += 1
                if(ascii_s == 123):
                    ascii_s = 97
            list_s[idx] = chr(ascii_s)              
         
        s = ''.join(list_s)
    
    return s