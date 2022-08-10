# 다섯 개의 자연수가 주어질 때 이들의 평균과 중앙값을 구하는 프로그램을 작성하시오.
# 첫째 줄에는 평균을 출력하고, 둘째 줄에는 중앙값을 출력한다. 평균과 중앙값은 모두 자연수이다.

import sys
sys.stdin = open(r"C:\Users\LGE\Desktop\01-ALGORITHM\1회차\임수경\20220809\대표값2.txt", "r", encoding="utf-8")

li = []
for _ in range(5):
    li.append(int(input()))
    # print(li) # 중간점검
    # [10]
    # [10, 40]
    # [10, 40, 30]
    # [10, 40, 30, 60]
    # [10, 40, 30, 60, 30]

avg = sum(li) // 5 # 평균 = 수들의 합 / 수들의 개수 
# print(sum(li)) #170    
# 170 // 5 => 36

li.sort() # 리스트 sort를 사용하면 중앙값을 쉽게 사용할 수 있다. 

print(avg) #평균값 
print(li[2]) # 중앙값


# 개인공부 
# sort vs sorted

#(1) about sort
# sort 함수는 인덱스의 값을 교환하여 목록을 제자리에 정렬
# 새 목록이 반환되지 않습니다. / 동일한 목록이 정렬
# sort 함수에는 정렬을 위해 고려할 값을 정의하는 데 사용할 수 있는 key라는 또 다른 매개변수가 있습니다. 

#(2) about sorted 
# sorted도 목록을 정렬하는 데 사용됩니다. 그러나 sorted 함수는 동일한 목록을 제자리에 정렬하는 대신 새 목록을 반환함
# 두 매개변수, 즉 reverse 및 key도 이 기능에서 사용할 수 있습니다. 



# 더 짧은 코드 
# li = sorted([int(input()) for _ in range(5)])
# print(sum(li)//5)
# print(li[2])