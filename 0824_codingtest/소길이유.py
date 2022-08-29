import sys
sys.stdin = open(r"C:\Users\LGE\Desktop\코딩테스트 합격\Algorithm_J\8월\0824_codingtest\소길이유.txt", "r", encoding="utf-8")
from sys import stdin 

n = int(input()) #관찰 횟수 n , (100이하의 정수)정수형 변환

# 소들의 위치를 리스트로 받아줍니다. 
# 존이 가지고 있는 소들은 총 10마리 이며 이 소들의 위치는 아직 모르기 때문에 none으로 지정해줍니다. 
cows = [None] * 10 

# 소가 길을 건너간 횟수를 count를 통해 알아볼 것입니다. 
count = 0 

# 관찰 횟수 n 만큼 for문을 통해 반복 
for watch_idx in range(n):
    cow_num, left_right = map(int, stdin.readline().split(' ')) # 소의 번호, 위치 공백으로 구분해 입력하기 
    #print(cow_num)
    #print(left_right)
    prev_cow_position = cows[cow_num -1] #소의 이전 위치를 저장하는 변수 선언 
    cows[cow_num -1] = left_right # 입력된 소의 번호에 입력된 위치로 초기화 

    if prev_cow_position != None and prev_cow_position != left_right: # 소의 위치가 none이 아니면서, 이전의 위치와 현재의 위치가 다르다면, 
        count += 1 # 소가 이동한 것이므로 count 에 1을 더해준다. 

print(count) # 소가 길을 건너간 횟수 




# 개인 공부 
# input()대신 sys.stdin.readline()을 사용하는 이유
# : 반복문으로 여러줄을 입력 받아야 할 때는 input()으로 입력 받는다면 시간초과가 발생가능성 높음 
# : 반복문으로 여러줄 입력받는 상황에서는 반드시 sys.stdin.readline()을 사용해야 시간초과가 발생하지 않습니다.'
# (1) 한 개의 정수를 입력받을 때 : a = int(sys.stdin.readline())
# (2) 정해진 개수의 정수를 한줄에 입력받을 때 : a,b,c = map(int,sys.stdin.readline().split())
# (3) 임의의 개수의 정수를 한줄에 입력받아 리스트에 저장할 때 : data = list(map(int,sys.stdin.readline().split()))
# (4) 임의의 개수의 정수를 n줄 입력받아 2차원 리스트에 저장할 때 : data.append(list(map(int,sys.stdin.readline().split())))
# (5) 문자열 n줄을 입력받아 리스트에 저장할 때 : data = [sys.stdin.readline().strip() for i in range(n)]




#다른방법 
# n = int(input())
 
# arr = {}
# count = 0
 
# for i in range(n):
#     a,b = map(int, input().split())
#     if a not in arr:
#         arr[a] = b
#     else:
#         if arr[a] != b:
#             count +=1
#             arr[a] = b
 
# print(count)


#풀이 방법 
# (1) 관찰 횟수 n번 입력 받기
# (2) 소의 번호와 위치를 저장할 딕셔너리 arr 선언
# (3) 소가 길을 건넌 횟수를 셀 변수 count 선언
# (4) n번 만큼 반복문을 돌려 소의 번호와 움직인 위치(왼, 오) 를 a,b로 입력받기
# (5) 만약 키 값 a (소의 번호)가 딕셔너리 arr에 없다면 키(a)값과 밸류(b)값을 arr에 저장
# (6) 키 값 a(소의 번호)가 이미 딕셔너리 arr에 있다면 밸류 값 b(소가 움직인 위치)가 같은지 다른지 판별
# (7) 만약 같다면 길을 건너지 않은 것이므로 다시 반복문으로 돌아가기
# (8) 같지 않다면 길을 건넌 것이므로 숫자를 1 카운트 해주고 저장 & 그 값을 다시 딕셔너리에 넣기
# (9) (4)~(8)의 과정을 반복해서 실행
# (10) 소가 길을 건너간 최소 횟수(count) 출력


# 주석이 없는 최종코드 
# n = int(input())
# cows = [None] * 10 
# count = 0 
# for watch_idx in range(n):
#     cow_num, left_right = map(int, stdin.readline().split(' ')) 
#     prev_cow_position = cows[cow_num -1] 
#     cows[cow_num -1] = left_right

#     if prev_cow_position != None and prev_cow_position != left_right: 
#         count += 1 

# print(count)