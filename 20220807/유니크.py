# 상근이와 친구들은 이 게임을 3번 했다. 각 플레이어가 각각 쓴 수가 주어졌을 때, 3번 게임에서 얻은 총 점수를 구하는 프로그램을 작성하시오.
# 각 플레이어가 3번의 게임에서 얻은 총 점수를 입력으로 주어진 순서대로 출력한다.

import sys
sys.stdin = open(r"C:\Users\LGE\Desktop\01-ALGORITHM\1회차\임수경\20220803\유니크.txt", "r", encoding="utf-8")

n = int(input()) # 2차원 리스트로 n 명이 입력한 숫자를 입력한다. 
score = [[], [], []]  # 3x3 행렬
sum = []
 
for i in range(n): # 각각 따로 리스트를 만들어 입력을 받아주기 
    a, b, c = map(int, input().split())
    score[0].append(a)
    score[1].append(b)
    score[2].append(c)
    
for i in range(n): 
    get = 0   # 각 열의 값 중 입력한 값이 자기 자신밖에 없다면 합 리스트에 추가해준다. 
    for j in range(3):  # for문을 사용하여 합을 구해준다. 
        if score[j].count(score[j][i]) == 1:
            get += score[j][i]
    sum.append(get)    # get 이라는 변수에 더해주기  & 더한 숫자를 sum이라는 리스트에 담아주기!
for i in sum:  
    print(i)  # sum 안에 들어 있는 숫자 출력 