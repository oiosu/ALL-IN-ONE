#다행스럽게도 일곱 난쟁이의 키의 합이 100이 됨을 기억
#아홉 난쟁이의 키가 주어졌을 때, 백설공주를 도와 일곱 난쟁이를 찾는 프로그램을 작성
#아홉 개의 줄에 걸쳐 난쟁이들의 키가 주어진다. 주어지는 키는 100을 넘지 않는 자연수이며,
#아홉 난쟁이의 키는 모두 다르며, 가능한 정답이 여러 가지인 경우에는 아무거나 출력한다.
#일곱 난쟁이의 키를 오름차순으로 출력한다. 일곱 난쟁이를 찾을 수 없는 경우는 없다.


import sys
sys.stdin = open(r"C:\Users\LGE\Desktop\01-ALGORITHM\1회차\임수경\20220808\일곱난쟁이.txt", "r", encoding="utf-8")

# 접근방법 : 9명의 난쟁이 키 합 - 가짜 난쟁이 키 합 = 100
# 9명의 난쟁이 키 합 = 140
# 140 - 40 = 100
# 가짜 난쟁이 키 합이 40인것을 알 수 있고 
# 9명의 난쟁이 키 합 중 40이 되는 값이 15와 25인 것을 확인 
# 15와 25를 제외한 출력의 값을 오름순으로 print()하면 됨 

# 키를 모두 리스트에 저장하고 
height = [] 
for i in range(9):  # 9명 난쟁이 
    height.append(int(input())) # int 하여 input로 담아두기 
    print(height)
    #[20]
    #[20, 7]
    #[20, 7, 23]
    #[20, 7, 23, 19]
    #[20, 7, 23, 19, 10]
    #[20, 7, 23, 19, 10, 15]
    #[20, 7, 23, 19, 10, 15, 25]
    #[20, 7, 23, 19, 10, 15, 25, 8]
    #[20, 7, 23, 19, 10, 15, 25, 8, 13]
for i in height: 
    for j in height:
        if sum(height) - i - j == 100 and i != j: # 9명의 난쟁이 키 합 - 가짜 난쟁이 키 합 = 100
            # del vs remove
            # del : 인덱스로 삭제 
            # remove () 함수 : 값으로 삭제 
            print(sum(height)) # 140
            print(i) # 15
            print(j) # 25
            height.remove(i) 
            height.remove(j)
            
height.sort() # 오름차순으로 정렬            
for i in height:
    print(i)

# 7
# 8
# 10
# 13
# 19
# 20
# 23


# about remove 
# array의 요소를 삭제
# array.remove(x) 형태로 사용
# 괄호( ) 안에 삭제하고자 하는 값을 입력
# 단, array 안에서 삭제하고자 하는 값이 여러 개가 있다 하더라도 첫 번째 값에 대해서만 삭제
# remove 함수를 사용하여 모든 값을 삭제할 때는 for문을 이용할 수도 있다.



#최종
# height = [] 
# for i in range(9):
#     height.append(int(input())) 
# for i in height: 
#     for j in height:
#         if sum(height) - i - j == 100 and i != j:
#             height.remove(i) 
#             height.remove(j)
        
# height.sort()          
# for i in height:
#     print(i)

