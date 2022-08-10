#모음은 'a', 'e', 'i', 'o', 'u'이며 대문자 또는 소문자
#입력의 끝에는 한 줄에 '#' 한 글자만이 주어진다.
#각 줄마다 모음의 개수를 세서 출력

import sys
sys.stdin = open(r"C:\Users\LGE\Desktop\01-ALGORITHM\1회차\임수경\20220809\모음의 개수.txt", "r", encoding="utf-8")

result = ['a','e','i','o','u']  # 리스트 형태 
while True:
    count = 0 
    s = list(input().lower()) # 리스트, 소문자 형태로 받기. 
    # s = list(input().upper()) #이렇게 바로 upper 한다면 값이 0이 나온다. result에 대문자가 없기 때문 
    # print(s)

    if s[0] == '#': #만약 #이라면 break [0] => 첫글자 
        break

    # s의 문자열에 result에 해당하는 문자열이 있을 경우 cnt 1씩 추가
    for i in s:
        if i in result:
            count += 1
    print(count)



# 문자열 대문자로 변경하는 함수 (string.upper)
# 문자열 소문자로 변경하는 함수 (string.lower)
# 문자가 대문자인지 확인하는 함수 (string.isupper)
# 문자가 소문자인지 확인하는 함수 (string.islower)


#방법 2
string = input()
vowel = 'AaEeIiOoUu'

while string != '#':
    answer = 0
    for i in string:
        if i in vowel:
            answer += 1
    print(answer)
    string = input()