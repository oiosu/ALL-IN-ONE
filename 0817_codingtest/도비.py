import sys
sys.stdin = open(r"C:\Users\LGE\Desktop\코딩테스트 합격\Algorithm_J\8월\0817_codingtest\도비.txt", "r", encoding="utf-8")


# 소문자로 바꿔서 비교 

while True:
    n = int(input())
    if n == 0:  
        break 
    words = []

    for _ in range(n):
        word = input()
        words.append((word.lower(), word))  #왜 word가 들어야가야하는지
        words.sort()  #sort
    print(words[0][1])  #이중리스트   # 왜 [0][1] 인지 


# while True:
    n = int(input())
    if n == 0:
        break
    else:
        lis = []
        for _ in range(n):
            word = input()
            lis.append(word)
        lis.sort(key=str.lower)

        print(lis[0])

#이중리스트 없이 풀이 방법 현성님이 공유해주심 




# def maxmax():
#     max_value = 0
#     max_idx = 0
#     for i in range(len(data)):
#         if data[i] > max_value: # 리스트의 앞에가 작아야 됨 => 할당 값이 작아야 됨(0)
#             max_value = data[i]
#             max_idx = i
#     return max_idx # 최대값의 인덱스 값 구하기 

# def minmin():
#     min_value = 123456 # 처음에는 높이보다 클 것 같은 값 넣어줌
#     min_idx = 0
#     for k in range(len(data)):
#         if data[k] < min_value: # 리스트의 앞에가 커야 됨 => 할당 값이 커야 됨
#             min_value = data[k]
#             min_idx = k
#     return min_idx

# for j in range(1, 11):
#     N = int(input())
#     data = list(map(int, input().split()))

#     for h in range(N): # 두 번 반복 위해 다시 함수쪽으로 올라감
#         data[maxmax()] -= 1 #최대값 인덱스 자리에서 -1, 함수를 위해 다시 올라갔다가 내려옴
#         data[minmin()] += 1 # 최솟값 인덱스 자리에서 +1

#     print(f'#{j} {data[maxmax()] - data[minmin()]}')