#각 사분면과 축에 점이 몇 개 있는지를 예제 출력과 같은 형식으로 출력

import sys
sys.stdin = open(r"C:\Users\LGE\Desktop\01-ALGORITHM\1회차\임수경\20220809\사분면.txt", "r", encoding="utf-8")

n = int(input())
axis = 0
q1 = 0
q2 = 0
q3 = 0
q4 = 0


# x가 0이거나 y가 0이면 점이 축에 존재하기 때문에 axis에 해당한다.
# x가 0보다 크고 y가 0보다 크면 둘 다 양수이므로 Q1에 해당한다.
# x가 0보다 작고 y가 0보다 크면 Q2에 해당한다.
# x가 0보다 작고 y가 0보다 작으면 둘 다 음수이므로 Q3에 해당한다.
# x가 0보다 크고 y가 0보다 작으면 Q4에 해당한다.



for _ in range(n) :
  x, y = map(int, input().split())
  
  if x == 0 or y == 0 :
    axis += 1
  elif x > 0 and y > 0 :
    q1 += 1
  elif x < 0 and y > 0 :
    q2 += 1
  elif x < 0 and y < 0 :
    q3 += 1
  else :
    q4 += 1

print("Q1:", q1)
print("Q2:", q2)
print("Q3:", q3)
print("Q4:", q4)
print("AXIS:", axis)