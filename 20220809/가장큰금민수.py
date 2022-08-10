# N이 주어졌을 때, N보다 작거나 같은 금민수 중 가장 큰 것을 출력하는 프로그램을 작성
# 첫째 줄에 N보다 작거나 같은 금민수 중 가장 큰 것을 출력

import sys
sys.stdin = open(r"C:\Users\LGE\Desktop\01-ALGORITHM\1회차\임수경\20220809\가장큰금민수.txt", "r", encoding="utf-8")

# 접근 방법 
# 금민수는 7과 4로 이루어진 가장 큰 수 이다. 따라서 입력받은 수와 같은 자릿수의 7로 이루어진 수가 가장 큰 수 일 것.
# 해당 수부터 차례로 4로 바꾸면서 입력받는 수보다 처음으로 작아지는 수가 제일 큰 수 일 것.
# 예를 들어 4자리의 수가 입력이 되면 7777 부터 7774 7747 7744 7477 순서로 점점 작아지면서 입력 수보다 작은 처음 수를 탐색한다. 

# 0 : 7 7 7 7 
# 1 : 7 7 7 4
# 2 : 7 7 4 7 
# 3 : 7 7 4 4
# 4 : 7 4 7 7 
# 5 : 7 4 7 4
# 6 : 7 4 4 7 
# 7 : 7 4 4 4
# 8 : 4 7 7 7 
# 9 : 4 7 7 4
# 10 : 4 7 4 7 
# 11 : 4 7 4 4
# 12 : 4 4 7 7 
# 13 : 4 4 7 4
# 14 : 4 4 4 7
# 15 : 4 4 4 4

# 수가 바뀌는 주기 : 2^3 2^2 2^1 2^0
# n 자릿수가 입력이 된면 총 2^n 번 반복이 된다.
# 만약 4444 미만의 수는 금민수가 4자릿수가 아닌 777인 세자리 수이므로 해당 과정을 통해서 찾지 못하면 
# 한 자리수 작은 7로 이루어진 은민수가 제일 큰 금민수이다.


# 백준에서는 틀린 코드라는 결과 
# vscode에서는 정답이 잘 출력됨 

N = input()
 
find = False
 
for i in range(2**len(N)):
    answer = ''
    for j in range(len(N)):
        if (i//(2**j)) % 2 == 0:
            answer += '7'+answer
        else:
            answer += '4'+answer
 
    if int(answer) <= int(N):
        find = True
        break
 
if not find:
    answer = ''
    for i in range(len(N)-1):
        answer += '7'
 
print(answer)





# 두번째 코드 
# if __name__ == '__main__':
#     n = int(input())

#     while True:
#         flag = True
#         for i in str(n):
#             if i != '4' and i != '7':
#                 flag = False
#                 n -= 1
#         if flag:
#             print(n)
#             break