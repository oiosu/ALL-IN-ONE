# 첫째 줄에 가장 많이 나온 문자를 출력한다. 여러 개일 경우에는 알파벳 순으로 앞서는 것부터 모두 공백없이 출력
# 문자열 개념을 다시 복습할 수 있는 문제 

# 파이썬에서 eof(end of file) 까지 입력 받는 방법 
# (1) sys.stdin.read() 이용하기 
# : 입력받을 때 sys.stdin.read()을 하게 되면, eof까지 모든 문자열을 받을 수 있다. 

# (2) try, except 구문 이용하기 
# : 무한 반복을 이용하여, eof error 발생시 break 해주기 

# (3) 알파벳을 아스키 코드를 이용해서 배열에 담기 
# : 문자열을 다룰떄 많이 쓰는 테크닉 중 하나 아스키코드 "97 == a", "65 == A" 암기하기 
# 문자열 => 아스키 코드 : ord(문자열)
# 아스키코드 => 문자열 : chr(아스키코드 )


import sys
sys.stdin = open(r"C:\Users\LGE\Desktop\01-ALGORITHM\1회차\임수경\20220809\많은글자.txt", "r", encoding="utf-8")

lines = sys.stdin.read()  #sys.stdin.read() 이용하기 
alpha = [0 for _ in range(26)]
for line in lines:
    if line.islower():  #소문자라면
        alpha[ord(line)-97] += 1

for i in range(26):
    if alpha[i] == max(alpha):  #최댓값 
        print(chr(i+97), end= " ")
