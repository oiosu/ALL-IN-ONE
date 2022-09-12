# 입력 
# 총 10개의 테스트 케이스가 주어지며, 각 테스트 케이스의 첫 번째 줄에는 덤프 횟수가 주어진다. 
# 그리고 다음 줄에 각 상자의 높이값이 주어진다.

# 출력 
# #부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 테스트 케이스의 최고점과 최저점의 높이 차를 출력

N = 10 #TC 개수
for i in range(1, N + 1):
    M = int(input()) # 상자 이동 가능 횟수
    arr = list(map(int, input().split())) # 상자 배열
    for j in range(M): # 상자 이동 가능 횟수 동안
        maxVal = max(arr) # 최댓값
        minVal = min(arr) # 최솟값
        minIdx = arr.index(minVal) # 최솟값 idx
        maxIdx = arr.index(maxVal) # 최댓값 idx
        arr[minIdx] += 1 # 최댓값 idx의 값에서 1 빼기
        arr[maxIdx] -= 1 # 최소값 idx의 값에서 1 더하기
    answer = max(arr) - min(arr) # 최댓값 - 최소값을 출력 결과로 
    print("#", i, " ", answer, sep='')
