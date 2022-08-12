# 세 자연수 S, K, H가 공백으로 구분
# 참여도의 합이 100 이상이면 일처리가 잘 되고 있기에 안심
# 100 미만이면 창호는 참여도가 가장 낮은 대학의 동아리에게 무언의 압박을 넣을 예정
# 첫 번째 줄에 일처리가 잘 되고 있어 무언의 압박이 필요가 없으면 (따옴표를 제외하고) “OK”를 출력
# 그 외에는 첫 번째 줄에 무언의 압박이 필요한 동아리가 속한 대학의 영문 이름의 첫 단어를 출력

import sys
sys.stdin = open(r"C:\Users\LGE\Desktop\01-ALGORITHM\1회차\임수경\20220811\와글와글.txt", "r", encoding="utf-8")


S, K, H = map(int, input().split()) # 3개의 대학교 


# 참여도가 100 이상일 때 
if S + K + H >= 100:  
    print("OK") # 일처리가 잘 되고 있기에 OK 를 출력해준다. 

# 참여도가 100미만일때 무언가 압박을 넣음 
else:
    if S == min(S, K, H):  # 최솟값이 숭실대일 경우 
        print("Soongsil")  # 숭실대에게 무언의 압박 

    elif K == min(S, K, H): # 최솟값이 고려대일 경우 
        print("Korea")      # 고려대에게 무언의 압박

    else:                      
        print("Hanyang")    # 최솟값이 한양대일 경우, 한양대에게 무언의 압박 


# 백준에서는 통과이지만 vscode에서는 오류가 발생하여 다음과 같이 해결한 과정을 기록한 내용입니다. 

# (1)
# ValueError: not enough values to unpack (expected 3, got 1) 오류 발생 
# unpack 하기에 값이 부족하다라는 오류 
# s, k, h를 나눠서 input값을 받아줌 

#(2)
# TypeError: int() argument must be a string, a bytes-like object or a number, not 'list'

#(3)
# ValueError: invalid literal for int() with base 10: '20000 5'

# 오류 다 해결함 = 원인 : sys.stdin text 파일 경로 수정하지 않음으로 발생한 오류 
