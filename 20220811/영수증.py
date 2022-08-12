# 구매한 물건의 가격과 개수로 계산한 총 금액이 영수증에 적힌 총 금액과 일치하면 Yes를 출력한다. 
# 일치하지 않는다면 No를 출력한다.

import sys
sys.stdin = open(r"C:\Users\LGE\Desktop\01-ALGORITHM\1회차\임수경\20220811\영수증.txt", "r", encoding="utf-8")

x = int(input()) # 영수증에 적힌 총 금액 x
n = int(input()) # 구매한 물건의 종류의 수 n
sum = 0 # 총금액 

for i in range(n):
    a, b = map(int, input().split()) # 각 물건의 가격 a, 개수 b
    sum += a * b
    # print(sum)
    # 100000
    # 160000
    # 220000
    # 260000
    # print(a)
    # 20000
    # 30000
    # 10000
    # 5000 
    # print(b)
    # 5
    # 2
    # 6
    # 8
if x == sum:    # 만약 영수증에 적힌 총 금액과 구매한 물건의 총 금액이 같다면
    # print(x) 260000
    # print(sum) 260000
    print("YES")  # YES 를 출력하고 
else:           # 같지 않다면 
    print("NO") # NO 를 출력하라. 


# 첫번째 예제 : YES
# 두번째 예제 : NO


# 주석이 없는 최종 코드 
x = int(input())
n = int(input())
sum = 0

for i in range(n):
    a, b = map(int, input().split())
    sum += a * b
if x == sum: 
    print("Yes")
else: 
    print("No")