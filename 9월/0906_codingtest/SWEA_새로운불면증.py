# 이종은님이 제공해주신 풀이 

## 첫번째 풀이 

t = int(input())

for _ in range(t):
    n = input() # 1 문자열로 입력받음
    value = int(n) # 정수형으로 바꿔줌
    data = [0]*10 # 0이 10개인 리스트 만들어줌 # 0~9까지 다 있는 단계의 값을 구하는 것!
    # data = [0, 1, 2, 3 ]
    while True: # 범위 없이 반복
        for i in range(len(n)): # 문자열 길이만큼 반복 즉, 9까지는 1번반복
            data[int(n[i])] += 1 #문자열의 0번째의 값을 정수형으로 바꿔서, 데이터 배열 자리값에 1을 추가해줌
        if not data.count(0): # 추가해준 것에서 0이 없을 때 출력하고 반복문 멈춤
            print(f'#{_+1} {int(n)}')
            break

        n = str(value+int(n))


## 두번째 풀이

for _ in range(int(input())):
    n = int(input())
    co = set() # set는 중복이 허용되지 않음
    cnt = 1        
    while True:
        for number in list(str(n)): # 리스트로 만든걸 돌림
            co.add(number) # set 숫자 각 자리를 추가해줌
        if len(co) == 10: # set에 숫자가 10개 있다면 멈춤 => 10개는 모두 2를 곱한 것!
            break
        n = n//cnt # 나눈 몫을 => 나눠야 되는 이유는 아래서 인풋값인 몫을 곱해줘야 되기 때문 즉, 인풋 값을 만들려고!
        cnt += 1
        n = n*cnt # 1씩 추가 된 것과 곱함
    print(f'#{_+1} {int(n)}')
