# 최대 점수, 최소 점수, 점수 차이를 구하는 프로그램을 작성
# 첫째 줄에는 "Class X"를 출력한다. X는 반의 번호이며 입력으로 주어진 순서대로 1부터 증가한다.
# 둘째 줄에는 가장 높은 점수, 낮은 점수, 성적을 내림차순으로 정렬했을 때 가장 큰 인접한 점수 차이를 
# 예제 출력과 같은 형식으로 출력한다.

#예제 
# 2
# 5 30 25 76 23 78
# 6 25 50 70 99 70 90

#출력 
# Class 1
# Max 78, Min 23, Largest gap 46
# Class 2
# Max 99, Min 25, Largest gap 25

# 풀이 과정 
# 입력받은 점수를 내림차순으로 정렬 후 
# 내장함수 max와 min을 사용하여 가장 큰값과 작은 값을 구한다. 
# 반복문을 사용하여 큰 점수와 작은 점수의 차이가 큰 값을 gap_val 에 넣고 
# 반복이 끝나면 차이가 가장 큰 값이 gap_val에 저장되어있는 것을 확인한다. 

k = int(input())
class_num = 1
for _ in range(k):
    arr = list(map(int, input().split()))
    cnt = arr[0]
    score = sorted(arr[1::], reverse = True)

    max_val = max(score) # 큰값
    min_val = min(score) # 작은값
    gap_val = score[0] - score[1] # gap초기화
    for i in range(2, len(score)):
        gap_val = max(gap_val, score[i-1]-score[i])

    print('Class', class_num)
    print('Max', max_val, end=", ")
    print('Min', min_val, end=", ")
    print('Largest gap', gap_val)
    class_num += 1