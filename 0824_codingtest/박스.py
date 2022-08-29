import sys
sys.stdin = open(r"C:\Users\LGE\Desktop\코딩테스트 합격\Algorithm_J\8월\0824_codingtest\박스.txt", "r", encoding="utf-8")

# 행이 아닌, 열 별로 박스의 위치를 2차원 리스트에 저장한다. _ 2차원 리스트에 대한 공부가 많이 필요함 
# 열별로 박스의 개수를 구하고 바닥을 행의 개수로 설정한다. 
# 열의 박스의 위치를 역순으로 탐색하며 상자를 만나면 바닥과의 차이(박스의 이동거리)를 구하여 이동 거리에 합하고, 바닥은 1 높인다. 
# 모든 열을 돌며 2~3 과정을 반복한다. 
# 모든 박스가 이동한 거리를 출력한다. 

for _ in range(int(input())):
    n, m = map(int,input().split())
    box = [input().split() for _ in range(n)] # 전체 리스트 생성
    ans = 0
    for j in range(m):
        cnt = 0
        for i in range(n-1,-1,-1): # 맨 뒤 리스트부터 거꾸로 탐색
            if field[i][j] == '1':
                ans += cnt
            else:
                cnt += 1 # 인덱스 값을 찾는 대신, 0이 나올 때마다 1씩 임시 카운트 값(cnt)을 추가해주면 된다.
    print(ans)